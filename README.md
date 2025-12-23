# ✨ Celestial Horoscope

> *Discover What the Stars Have Written for You*

A beautiful, AI-powered horoscope application that generates personalized zodiac readings based on your birth details.

![Powered by GPT-4o-mini](https://img.shields.io/badge/Powered%20by-GPT--4o--mini-purple?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel)

---

## 🌟 Features

- **🎂 Birth Date Analysis** — Automatically calculates your zodiac sign from your birth date
- **🔮 Multiple Reading Types:**
  - Daily Horoscope
  - Love & Relationships
  - Career & Finance
  - Health & Wellness
  - Comprehensive Reading
- **🎨 Element-Themed Design** — Colors adapt to your sign's element (Fire, Earth, Air, Water)
- **🤖 AI-Powered Insights** — GPT-4o-mini generates personalized, meaningful horoscopes
- **✨ Lucky Numbers & Colors** — Get your daily cosmic guidance

---

## ♈ Supported Zodiac Signs

| Sign | Dates | Element |
|------|-------|---------|
| ♈ Aries | Mar 21 - Apr 19 | 🔥 Fire |
| ♉ Taurus | Apr 20 - May 20 | 🌍 Earth |
| ♊ Gemini | May 21 - Jun 20 | 💨 Air |
| ♋ Cancer | Jun 21 - Jul 22 | 💧 Water |
| ♌ Leo | Jul 23 - Aug 22 | 🔥 Fire |
| ♍ Virgo | Aug 23 - Sep 22 | 🌍 Earth |
| ♎ Libra | Sep 23 - Oct 22 | 💨 Air |
| ♏ Scorpio | Oct 23 - Nov 21 | 💧 Water |
| ♐ Sagittarius | Nov 22 - Dec 21 | 🔥 Fire |
| ♑ Capricorn | Dec 22 - Jan 19 | 🌍 Earth |
| ♒ Aquarius | Jan 20 - Feb 18 | 💨 Air |
| ♓ Pisces | Feb 19 - Mar 20 | 💧 Water |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/deploy.git
cd deploy

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# Run the development server
uvicorn instant:app --reload --port 8000
```

Visit `http://localhost:8000` to get your horoscope!

---

## 🌐 Deploy to Vercel

1. **Push to GitHub** (if not already)
2. **Import to Vercel** at [vercel.com/new](https://vercel.com/new)
3. **Add Environment Variable:**
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
4. **Deploy!**

---

## 🎭 How It Works

1. **Enter Your Details** — Name, birth date, and reading type
2. **Zodiac Calculation** — Your sun sign is automatically determined
3. **AI Generation** — GPT-4o-mini creates a personalized horoscope
4. **Styled Results** — Beautiful, element-themed reading with lucky numbers

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | High-performance Python web framework |
| **OpenAI GPT-4o-mini** | AI-powered horoscope generation |
| **Vercel** | Serverless deployment platform |
| **Pure CSS** | Starfield animations & responsive design |

---

## 📁 Project Structure

```
deploy/
├── instant.py       # Main FastAPI application
├── requirements.txt # Python dependencies
├── vercel.json      # Vercel deployment config
└── README.md        # You are here
```

---

## 🎨 Design

- **Theme:** Deep space with twinkling stars
- **Colors:** Gold accents on cosmic blue/purple
- **Typography:** Playfair Display (headings) + Raleway (body)
- **Element Colors:**
  - 🔥 Fire signs: Orange/Red
  - 🌍 Earth signs: Green
  - 💨 Air signs: Cyan/Blue
  - 💧 Water signs: Purple

---

## 📜 License

MIT License — Feel free to fork and customize!

---

<p align="center">
  <em>⭐ May the stars guide your path ⭐</em>
</p>
