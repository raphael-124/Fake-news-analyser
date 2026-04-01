# 📰 News Analyser: AI-Powered Fake News Detection

**News Analyser** is a powerful platform designed to detect and categorize misinformation in the digital age. By combining a **FastAPI** backend with a modern **React** frontend, it provides users with real-time analysis of news articles using multiple AI models.

---

## 🌟 Key Features

### 🔍 Analysis Options
- **URL-to-Insight**: Automatically scrapes and cleans news content from any live URL using **BeautifulSoup**.
- **Raw Text Analysis**: Paste raw text directly into the analyzer for instant linguistic verification.

### 🧠 AI Models
- **Logistic Regression**: High-speed traditional ML analysis.
- **Random Forest**: Robust ensemble learning for improved accuracy.
- **DistilRoBERTa Transformer**: State-of-the-art NLP for deep semantic understanding.

### 📜 Analysis History (New!)
- **Persistent Sidebar**: Automatically saves your last 10 analyses in a beautiful glassmorphism sidebar.
- **Data Persistence**: Uses `localStorage` to keep your history safe even after page refreshes.
- **Instant Reload**: Click any previous analysis to instantly view the results and model confidence again.

### 🎨 Modern UI
- **Glassmorphism Design**: High-end visual aesthetics with vibrant gradients and subtle blurs.
- **Responsive Layout**: Optimized for all screen sizes, from mobile to desktop.

---

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern, high-performance web framework for Python.
- **Hugging Face**: Powering the NLP Transformer models.
- **Scikit-Learn**: Traditional machine learning pipelines.
- **BeautifulSoup**: Robust web scraping.

### Frontend
- **React 19**: Modern UI development with hooks and state management.
- **Vite 6**: Next-generation frontend tooling for speed.
- **Vanilla CSS**: Custom glassmorphism design system.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- npm

### Installation & Run
You can use the provided `start.bat` file (Windows) to launch both servers simultaneously:

1.  **Clone the Repo**:
    ```bash
    git clone https://github.com/raphael-124/Fake-news-analyser.git
    cd Fake-news-analyser
    ```
2.  **Launch Servers**:
    Double-click on **`start.bat`**.

Alternatively, run them manually:
- **Backend**: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
- **Frontend**: `cd frontend && npm install && npm run dev`

---

## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 🤝 Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
