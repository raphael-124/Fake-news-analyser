import React from 'react';

const AnalyzerForm = ({ activeTab, inputValue, setInputValue, modelType, setModelType, handleSubmit, isLoading }) => {
  return (
    <form onSubmit={handleSubmit}>
      <div className="input-group">
        <label>AI Model Selection</label>
        <select value={modelType} onChange={(e) => setModelType(e.target.value)}>
          <option value="logistic">Logistic Regression (TF-IDF)</option>
          <option value="random_forest">Random Forest (TF-IDF)</option>
          <option value="transformer">DistilRoBERTa (NLP Transformer)</option>
        </select>
      </div>

      <div className="input-group">
        <label>{activeTab === 'text' ? 'Article Text' : 'Article URL'}</label>
        {activeTab === 'text' ? (
          <textarea 
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Paste the news article here..."
          />
        ) : (
          <input 
            type="text" 
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="https://example.com/news-article"
          />
        )}
      </div>

      <button type="submit" className="btn-primary" disabled={isLoading || !inputValue.trim()}>
        {isLoading ? <div className="loader"></div> : 'Analyze News'}
      </button>
    </form>
  );
};

export default AnalyzerForm;
