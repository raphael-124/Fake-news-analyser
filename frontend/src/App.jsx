import { useState, useEffect } from 'react';
import './index.css';
import Header from './components/Header';
import TabSwitcher from './components/TabSwitcher';
import AnalyzerForm from './components/AnalyzerForm';
import ResultCard from './components/ResultCard';
import HistorySidebar from './components/HistorySidebar';
import { useAnalysis } from './hooks/useAnalysis';

function App() {
  const [activeTab, setActiveTab] = useState('text'); // 'text' or 'url'
  const [inputValue, setInputValue] = useState('');
  const [modelType, setModelType] = useState('logistic');
  const [history, setHistory] = useState([]);
  
  const { isLoading, result, error, performAnalysis, setResult, setError } = useAnalysis();

  // Load history on mount
  useEffect(() => {
    const savedHistory = JSON.parse(localStorage.getItem('news_analyser_history') || '[]');
    setHistory(savedHistory);
  }, []);

  // Update history when result changes
  useEffect(() => {
    if (result) {
      const savedHistory = JSON.parse(localStorage.getItem('news_analyser_history') || '[]');
      setHistory(savedHistory);
    }
  }, [result]);

  const handleTabChange = (tab) => {
    setActiveTab(tab);
    setInputValue('');
    setResult(null);
    setError(null);
  };

  const handleModelChange = (type) => {
    setModelType(type);
    setResult(null);
    setError(null);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;
    performAnalysis(activeTab, inputValue, modelType);
  };

  const handleSelectHistory = (item) => {
    setResult(item);
    setActiveTab(item.type);
    setInputValue(item.query);
    setModelType(item.modelType);
  };

  const handleClearHistory = () => {
    localStorage.removeItem('news_analyser_history');
    setHistory([]);
  };

  return (
    <div className="app-container">
      <div className="glass-panel main-panel">
        <Header />

        <TabSwitcher 
          activeTab={activeTab} 
          setActiveTab={handleTabChange} 
        />

        <AnalyzerForm 
          activeTab={activeTab}
          inputValue={inputValue}
          setInputValue={setInputValue}
          modelType={modelType}
          setModelType={handleModelChange}
          handleSubmit={handleSubmit}
          isLoading={isLoading}
        />

        {error && <div className="error-msg">{error}</div>}

        {result && <ResultCard result={result} modelType={modelType} />}
      </div>

      <HistorySidebar 
        history={history} 
        onSelect={handleSelectHistory} 
        onClear={handleClearHistory} 
      />
    </div>
  );
}

export default App;
