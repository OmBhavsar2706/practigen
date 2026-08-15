# PractiGen

> AI-powered practical file assistant for MSBTE Diploma Students

PractiGen helps diploma students instantly generate:
- ✅ Practical file **Conclusion**
- ✅ **Answers** to Practical Related Questions

Built with Python, Flask, and Google Gemini API.

---

## What Problem Does It Solve?

Every MSBTE diploma student has to manually write conclusions
and question answers for each practical in their file.
This is repetitive and time-consuming.

PractiGen automates this — enter your subject, practical name,
and paste your questions. Get clean, ready-to-copy content
in seconds.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + Flask |
| AI | Google Gemini API (gemini-3.1-flash-lite) |
| Frontend | HTML + CSS + JavaScript |
| Config | python-dotenv |

---

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/practigen.git
cd practigen
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key
Create a `.env` file in the root folder:
Get your free API key at: https://aistudio.google.com

### 5. Run the app
```bash
python app.py
```

Open your browser and go to: `http://localhost:5000`

---

## How to Use

1. Enter your **Subject** (e.g. Cloud Computing)
2. Enter your **Practical Name** (e.g. Practical No.3 - Create VMs)
3. Paste your **Practical Related Questions** from the booklet
4. Click **Generate Practical Content**
5. Copy the **Conclusion** into your practical file
6. Copy each **Answer** into the question answer space

> ⚠️ For questions that require program output or screenshots —
> run the practical yourself and attach the actual printout.
> AI answers are reference only.

---

## Important Notes

- This tool generates reference content only
- Always review before copying into your practical file
- For questions requiring actual program output — you must
  run the practical and attach real screenshots/printouts
- Built for MSBTE diploma students (Maharashtra, India)

---

## Developer

**Om Bhavsar**
Diploma in AI & ML · MSBTE
AI/ML Intern · SoftCrowd Technologies, Nashik

---

## License

This project is open source and free to use for educational
purposes.
