import React from 'react';

const ResultCard = ({ result, modelType }) => {
  const badgeClass = result?.prediction === 'Real News' ? 'Real' : 'Fake';
  const modelLabel = modelType === 'logistic' ? 'Logistic Regression' : 
                     modelType === 'random_forest' ? 'Random Forest' : 
                     'DistilRoBERTa NLP Transformer';

  return (
    <div className={`result-card ${badgeClass}`}>
      <div className="result-header">
        <span className={`prediction-badge ${badgeClass}`}>{result.prediction}</span>
        <span className="confidence-score">{result.confidence}% Match</span>
      </div>
      
      <p>
        Based on linguistic analysis using <strong>{modelLabel}</strong>, this content is highly likely to be <strong>{result.prediction.toLowerCase()}</strong>.
      </p>

      {result.scraped_text_preview && (
        <div className="preview-text">" {result.scraped_text_preview} "</div>
      )}
    </div>
  );
};

export default ResultCard;
