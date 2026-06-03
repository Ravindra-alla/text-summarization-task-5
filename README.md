# AETHER // AI Text Summarizer

Aether is a premium, modern, and responsive web application that summarizes long text documents, articles, or paragraphs into clear and concise summaries. The application leverages a state-of-the-art NLP model (`facebook/bart-large-cnn`) run locally via Hugging Face Transformers and PyTorch, housed within a lightweight Flask backend and a sleek Glassmorphic user interface.

![Aether Interface Mockup](https://raw.githubusercontent.com/username/repository/main/static/screenshot.png) *(Note: Replace with actual screenshot of your running app)*

---

## ✨ Features

- **Advanced AI Summarization**: Uses the state-of-the-art `facebook/bart-large-cnn` model for high-quality abstractive summarization.
- **Glassmorphic UI Design**: Visually stunning dashboard interface utilizing modern CSS variables, gradients, card-glows, and micro-animations.
- **Real-Time Analytics**:
  - Word count tracking (input and output)
  - Character count tracking (input and output)
  - Compression/reduction ratio percentage
  - Inference duration in seconds
- **Responsive Layout**: Designed for optimal viewing on desktop, tablet, and mobile screens.
- **Interactive Controls**:
  - One-click copy to clipboard with success feedback state
  - Clear workspace button to reset inputs and outputs
  - Real-time length validators with shake-animation error dialogs
- **Performance Optimized**: Restricts input to 800 words to ensure faster inference.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, PyTorch, Hugging Face Transformers, NumPy
- **Frontend**: HTML5 (Semantic), CSS3 (Modern tokens, flexbox/grid layout, custom scrollbars, animations), Vanilla JavaScript (ES6)

---

## 🚀 Installation & Setup

Follow these steps to run the application locally:

### 1. Prerequisites
Make sure you have **Python 3.8+** installed.

### 2. Clone the Repository
```bash
git clone <your-repository-url>
cd <repository-directory-name>
```

### 3. Create a Virtual Environment
It is highly recommended to run this in a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install all the required Python packages:
```bash
pip install -r requirements.txt
```

> **Note**: The first time you run the application or load the model, it will download the model files (`facebook/bart-large-cnn`) which are approximately 1.6 GB. Ensure you have a stable internet connection.

### 5. Start the Application
Run the Flask server:
```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 📂 Project Structure

```text
├── app.py                  # Flask backend containing API routes and NLP model pipeline
├── requirements.txt        # Python dependency list
├── .gitignore              # Standard git ignore file for Python/Flask
├── templates/
│   └── index.html          # Web UI layout and client-side JavaScript logic
└── static/
    └── style.css           # Styling rules, design tokens, and CSS animations
```

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
