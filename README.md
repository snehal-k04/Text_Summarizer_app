# Text Summarizer App

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-T5-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/t5-small)

> A web app that summarizes dialogue and text using a fine-tuned T5 model, served via FastAPI with an HTML frontend.

---

## How It Works

## Stack

| Layer | Technology |
|-------|-----------|
| Model | T5 (fine-tuned, via HuggingFace Transformers) |
| Backend | FastAPI + Pydantic |
| Frontend | HTML |
| Inference | PyTorch (CPU / CUDA / MPS) |

## Run Locally

```bash
git clone https://github.com/snehal-k04/Text_Summarizer_app.git
cd Text_Summarizer_app
pip install -r requirements.txt
uvicorn app:app --reload
```

Then open `http://localhost:8000` in your browser.

## API

`POST /summarize/` — accepts `{ "dialogue": "your text here" }`, returns `{ "summary": "..." }`
