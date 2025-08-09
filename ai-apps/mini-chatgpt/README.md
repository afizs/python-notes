# Mini-ChatGPT (Streamlit + GitHub Models)

A lightweight Streamlit chat app powered by **GitHub Models** via `langchain-azure-ai`.  
It supports:

- ✅ **GitHub token input** in the UI (no hard-coding needed)  
- ✅ **System prompt customization**  
- ✅ **Chat history** that persists for the session  
- ✅ **Multiple model choices**  
- ✅ **Safe token handling** (stored only in session state)  
- ✅ **Clear chat** functionality  

---

## 🚀 Getting Started

### 1. Install dependencies using `uv`

```bash
uv init
uv add streamlit langchain-azure-ai
```
## 2. Provide your GitHub Token
First get your GitHub access token from https://github.com/settings/apps.

You have two options to provide the token in the app:
1. Easiest (local testing) – Paste it in the sidebar when running the app.
2. Environment variable
```
export GITHUB_TOKEN="ghp_...your_token..."
```

## 3. Run the app
```bash
uv run streamlit run app.py
```

## 🖥 Usage
1. Start the app (above command).
2. Open the URL shown in your terminal (usually http://localhost:8501).