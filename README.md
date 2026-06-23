# Misinformation Risk Analyser 🔍

A rule-based Python tool that analyses news text and assigns a credibility risk level — **LOW**, **MEDIUM**, or **HIGH** — based on linguistic indicators commonly found in misinformation.

> 📚 Academic capstone project — Semester 2 | This repository contains my individual contribution to the group project.

---

## 💡 How it works

The analyser scans input text across **6 detection checks**:

| Check | What it looks for |
|---|---|
| Emotional manipulation | Words like "shocking", "terrifying", "explosive" |
| Clickbait phrases | "you won't believe", "share before it's deleted" |
| Excessive punctuation | Multiple `!!` or `??` in text |
| Missing credible sources | Absence of references to known outlets (BBC, WHO, Reuters etc.) |
| Vague attribution | "sources say", "insiders claim", "rumor has it" |
| Claim-evidence mismatch | Strong claims ("proven", "confirmed") with no supporting evidence |

Each check adds to a **risk score**, which maps to a final verdict:

```
Score 0–2  →  LOW     "Likely credible. No major red flags."
Score 3–5  →  MEDIUM  "Needs verification. Some suspicious signals."
Score 6+   →  HIGH    "Likely misleading. Multiple red flags detected."
```

---

## 🚀 Running it

No installation needed — pure Python, no external libraries.

```bash
python "Risk analyzer.py"
```

Then type any news headline or paragraph and press Enter. Type `quit` to exit.

**Example output:**
```
==================================================
         MISINFORMATION RISK ANALYSIS
==================================================
 Input Text : You won't believe what they are hiding...
--------------------------------------------------
 Risk Score : 4 / 9
 Risk Level : MEDIUM
 Verdict    : Needs verification. Some suspicious signals.
--------------------------------------------------
 Indicators Detected:
   - Clickbait phrase detected: you won't believe
   - Vague attribution detected: they are hiding
==================================================
```

---

## 🧠 My Contribution

This module was my individual contribution to a group capstone project. I designed and implemented:

- The full rule-based detection engine (`analyze_risk` function)
- All 5 indicator dictionaries (emotional words, clickbait, vague claims, credibility signals, claim words)
- The scoring and risk-level classification system
- The display and CLI interface

---

## 👥 Full Project

This is part of a larger **AI-powered Misinformation Detection System** built as a group capstone project. The complete project includes additional modules built by my teammates.

> 🔗 Full project repo: *(link coming soon)*
> 
> 📊 [View Project Presentation](https://docs.google.com/presentation/d/1muWbsVyf5uiexqH148uKk8LnsyOBVhO2/edit?usp=sharing&ouid=102696365172910796975&rtpof=true&sd=true)

---

## 🛠️ Built With

- Python 3 (standard library only — `re` module)
- No external dependencies

---

## 👩‍💻 Author

**Aalya Gupta**
B.Tech CSE @ Manipal University Jaipur | BS-MS AI & Cybersecurity @ IIT Patna
