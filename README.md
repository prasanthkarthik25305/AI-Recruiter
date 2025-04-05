# 🤖 AI Recruiter - Multi-Agent AI Recruitment Assistant

Welcome to **AI Recruiter**, a multi-agent system designed to automate and streamline the recruitment process using LLMs and persistent memory via SQLite.

Built as part of a hackathon challenge, this project reads job descriptions (JDs), parses candidate CVs, computes match scores, shortlists qualified candidates, and sends personalized interview invitations — all with AI agents working in coordination.

---

## 🧠 Project Architecture

```text
  ┌────────────┐       ┌──────────────────────┐       ┌────────────────┐
  │ Job Inputs │──────▶│ JD Summarizer Agent  │──────▶│ Job DB         │
  └────────────┘       └──────────────────────┘       └────────────────┘
                                                           │
                                                           ▼
                      ┌────────────────────────────┐
                      │ Recruiting Agent           │◀─────┐
                      │ - CV parsing               │      │
                      │ - Info extraction          │      │
                      │ - Match score calculation  │      │
                      └────────────────────────────┘      │
                                                           │
      ┌─────────────────────┐                              │
      │ Candidate CVs       │──────────────────────────────┘
      └─────────────────────┘
               │
               ▼
  ┌──────────────────────────────┐
  │ Shortlister Agent            │───▶ Shortlisted Candidates
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
  Uses LLM to extract structured data like role, required skills, experience, and responsibilities from raw job descriptions.

- 📄 **Recruiting Agent**  
  Parses candidate CVs (PDF/DOCX), extracts key information (skills, education, experience), and stores it in a SQLite DB.

- 📊 **Match Scorer + Shortlister**  
  Calculates match score between JD and each candidate. Shortlists candidates above a configurable threshold (e.g., 80%).

- 📅 **Interview Scheduler Agent**  
  Generates and sends customized interview emails to shortlisted candidates with proposed time slots and interview mode.

- 🧠 **Persistent Memory**  
  Uses SQLite to store job descriptions, parsed candidate data, match scores, and status flags.

---

## ⚙️ Tech Stack

- **Language**: Python 3.10+
- **LLMs**: OpenAI GPT / Gemini Pro
- **PDF Parsing**: `pdfplumber`, `python-docx`
- **NLP**: `spaCy`, `fuzzywuzzy`, `transformers`
- **DB**: SQLite (in-memory or file-based)
- **Email**: `smtplib` or Gmail API (for < 100 mails/day)

---

## 🚀 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai-recruiter.git
cd ai-recruiter
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Keys (if using OpenAI/Gemini)

```bash
export OPENAI_API_KEY=your-api-key
# or for Gemini
export GOOGLE_API_KEY=your-api-key
```

### 4. Run the Pipeline

```bash
python main.py --jd ./data/jds/jd1.txt --cvs ./data/cvs/
```

---

## 🗃️ Project Structure

```text
ai-recruiter/
├── agents/
│   ├── jd_summarizer.py       # Summarizes job descriptions
│   ├── recruiter.py           # Parses and extracts CV info
│   ├── shortlister.py         # Filters candidates by score
│   └── scheduler.py           # Sends interview emails
├── data/
│   ├── jds/                   # Raw job descriptions
│   └── cvs/                   # Candidate CVs (PDF/DOCX)
├── db/
│   └── memory.sqlite          # SQLite database
├── utils/
│   ├── parser.py              # CV parsing utils
│   ├── matcher.py             # Matching logic
│   └── emailer.py             # Email sending logic
├── main.py                    # Main orchestration script
├── requirements.txt
└── README.md
```

---

## 📈 Scoring Logic (Example)

```python
score = (
  0.7 * skill_overlap(candidate.skills, jd.skills) +
  0.2 * education_match(candidate.education, jd.qualifications) +
  0.1 * experience_match(candidate.years_exp, jd.years_exp)
)
```

> Shortlist if score ≥ 0.8

---

## 📬 Email Example

```text
Subject: Interview Invitation - Backend Engineer Role

Hi John,

We were impressed by your profile and would like to invite you for an interview for the Backend Engineer position.

Proposed Time Slots:
- Monday 2:00 PM
- Tuesday 4:00 PM

Format: Google Meet

Regards,  
AI Recruiter Team
```

---

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License

---

## 🏆 Built With 💙 for the Hackathon

> Automating recruitment, one candidate at a time. 🚀
