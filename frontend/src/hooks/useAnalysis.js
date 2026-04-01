import { useState } from 'react';
import { analyzeText, analyzeUrl } from '../services/api';

export const useAnalysis = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const performAnalysis = async (type, value, modelType) => {
    setIsLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = type === 'text' 
        ? await analyzeText(value, modelType)
        : await analyzeUrl(value, modelType);
      
      const newResult = {
        ...data,
        id: Date.now(),
        timestamp: new Date().toISOString(),
        query: value,
        type: type,
        modelType: modelType
      };

      setResult(newResult);

      // Persist to history in localStorage
      const existingHistory = JSON.parse(localStorage.getItem('news_analyser_history') || '[]');
      const updatedHistory = [newResult, ...existingHistory].slice(0, 10);
      localStorage.setItem('news_analyser_history', JSON.stringify(updatedHistory));
      
    } catch (err) {
      setError(err.message || 'An unexpected error occurred.');
    } finally {
      setIsLoading(false);
    }
  };

  return { isLoading, result, error, performAnalysis, setResult, setError };
};
