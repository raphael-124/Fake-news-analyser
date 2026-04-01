const BASE_URL = 'http://localhost:8000/api';

export const analyzeText = async (text, modelType) => {
  const response = await fetch(`${BASE_URL}/predict/text`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_type: modelType })
  });
  return handleResponse(response);
};

export const analyzeUrl = async (url, modelType) => {
  const response = await fetch(`${BASE_URL}/predict/url`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url, model_type: modelType })
  });
  return handleResponse(response);
};

const handleResponse = async (response) => {
  let data;
  const contentType = response.headers.get("content-type");
  
  if (contentType && contentType.includes("application/json")) {
    data = await response.json();
  } else {
    const text = await response.text();
    throw new Error(text || `Server returned ${response.status}`);
  }

  if (!response.ok) {
    throw new Error(data.detail || data.error || 'Analysis failed');
  }

  return data;
};
