import React from 'react';

const TabSwitcher = ({ activeTab, setActiveTab }) => (
  <div className="tabs">
    <button 
      type="button"
      className={`tab ${activeTab === 'text' ? 'active' : ''}`}
      onClick={() => setActiveTab('text')}
    >
      Paste Text
    </button>
    <button 
      type="button"
      className={`tab ${activeTab === 'url' ? 'active' : ''}`}
      onClick={() => setActiveTab('url')}
    >
      Enter URL
    </button>
  </div>
);

export default TabSwitcher;
