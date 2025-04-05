# 🤖 AI Recruiter - On-Prem Multi-Agent AI Recruitment Assistant

**AI Recruiter** is a fully on-premise, privacy-focused recruitment automation system powered by **Ollama LLMs**, **embedding models**, and a **multi-agent architecture**. It automates job description analysis, candidate CV matching, shortlisting, and interview scheduling — all while keeping your data local and secure.

---

## 🧠 System Architecture

```text
  ┌────────────┐       ┌──────────────────────┐       ┌────────────────┐
  │ Job Inputs │──────▶│ JD Summarizer Agent  │──────▶│ Jobs DB        │
  └────────────┘       └──────────────────────┘       └────────────────┘
                                                           │
                                                           ▼
                      ┌────────────────────────────┐
                      │ Recruiting Agent           │◀─────┐
                      │ - CV parsing               │      │
                      │ - Info extraction (LLM/ML) │      │
                      └────────────────────────────┘      │
                                                           │
      ┌─────────────────────┐                              │
      │ Candidate CVs       │──────────────────────────────┘
      └─────────────────────┘
               │
               ▼
  ┌──────────────────────────────┐
  │ Embedding + Matching Agent   │───▶ Similarity Score
  └──────────────────────────────┘
               │
               ▼
  ┌──────────────────────────────┐
  │ Shortlister Agent            │───▶ Final Candidates
  └──────────────────────────────┘
               │
               ▼
  ┌──────────────────────────────┐
  │ Interview Scheduler Agent    │───▶ Personalized Emails
  └──────────────────────────────┘
```

---

## 💡 Features

- 🧾 **JD Summarizer Agent**
  - Extracts role, skills, qualifications, experience, and responsibilities using Ollama LLMs.

- 📄 **Recruiting Agent**
  - Parses CVs with a hybrid of traditional parsing (`pdfplumber`, `docx`) and ML/LLM extraction.

- 🧠 **Embedding-based Matching Agent**
  - Uses **Ollama embedding models** for vector similarity matching between candidate profiles and JDs.

- 📊 **Shortlister**
  - Selects top candidates based on match score threshold (e.g. ≥ 80%).

- 📅 **Interview Scheduler Agent**
  - Generates human-like emails using LLMs and sends them through local SMTP or logs them for review.

- 🗃️ **SQLite Memory**
  - Stores long-term structured data for JDs, candidates, match scores, and agent states.

---

## ⚙️ Tech Stack

| Component             | Stack                                 |
|----------------------|----------------------------------------|
| LLMs & Embeddings    | [Ollama](https://ollama.com) (local)  |
| Multi-Agent Control  | Custom Agent Framework (modular)      |
| CV Parsing           | `pdfplumber`, `python-docx`, ML model |
| Matching             | Ollama embeddings + cosine similarity |
| Storage              | SQLite                                 |
| Scheduling & Email   | Local SMTP / Simulated mailer         |
| Add-ons              | Web scraper, custom ML, API plugins   |

---

## 🚀 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai-recruiter.git
cd ai-recruiter
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Start Ollama Locally

Make sure you have [Ollama](https://ollama.com) installed and a model pulled.

```bash
ollama run llama2
# or pull embedding model
ollama run nomic-embed-text
```

### 4. Run the Pipeline

```bash
python main.py --jd ./data/jds/jd1.txt --cvs ./data/cvs/
```

---

## 📁 Project Structure

```text
ai-recruiter/
├── agents/
│   ├── jd_summarizer.py
│   ├── recruiter.py
│   ├── matcher.py
│   ├── shortlister.py
│   └── scheduler.py
├── data/
│   ├── jds/
│   └── cvs/
├── db/
│   └── memory.sqlite
├── embeddings/
│   └── embedder.py
├── tools/
│   ├── cv_parser.py
│   ├── emailer.py
│   ├── web_scraper.py
│   └── ml_model.py
├── utils/
│   └── prompt_templates.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 Matching Logic (Sample)

```python
def calculate_match_score(jd_embed, candidate_embed):
    return cosine_similarity(jd_embed, candidate_embed)
```

> Candidates with score ≥ 0.8 are shortlisted.

---

## 📬 Email Output (Example)

```text
Subject: Interview Invitation - Data Analyst Role

Hi Priya,

Thank you for applying for the Data Analyst position. Based on your qualifications and experience, we’re excited to invite you for an interview.

Proposed Time Slots:
- Tuesday, 10:00 AM IST
- Wednesday, 2:00 PM IST

Interview Format: Zoom / Google Meet

Best regards,  
AI Recruiter Team
```

---

## 🛡️ Privacy & Local-first Approach

No data leaves your machine. Everything — from parsing to LLM usage — runs on your local system via **Ollama**. Perfect for enterprise and data-sensitive applications.

---

## 📄 License

MIT License

---

## 🏁 Built For

> 🔥 Hack the Future — A GenAI sprint powered by Data.

---

Let me know if you want:
- 🧪 Unit test support
- 🖥️ Lightweight web UI
- 🧩 Prebuilt JD/CV examples
- 📦 Packaging for offline deployment
