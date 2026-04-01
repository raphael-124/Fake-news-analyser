import React from 'react';

const HistorySidebar = ({ history, onSelect, onClear }) => {
  if (!history || history.length === 0) {
    return (
      <div className="history-sidebar empty">
        <h3>Analysis History</h3>
        <p>No past analyses yet.</p>
      </div>
    );
  }

  const formatTime = (isoString) => {
    return new Date(isoString).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className="history-sidebar">
      <div className="sidebar-header">
        <h3>Recent Analyses</h3>
        <button className="clear-btn" onClick={onClear}>Clear</button>
      </div>
      <div className="history-list">
        {history.map((item) => (
          <div 
            key={item.id} 
            className={`history-item ${item.prediction === 'Real News' ? 'real-border' : 'fake-border'}`}
            onClick={() => onSelect(item)}
          >
            <div className="item-main">
              <span className="item-label">{item.type.toUpperCase()}</span>
              <span className="item-time">{formatTime(item.timestamp)}</span>
            </div>
            <div className="item-query truncate">
              {item.query}
            </div>
            <div className={`item-prediction ${item.prediction === 'Real News' ? 'real-text' : 'fake-text'}`}>
              {item.prediction} - {item.confidence}%
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HistorySidebar;
