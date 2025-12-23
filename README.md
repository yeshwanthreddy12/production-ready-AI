# Celestial Horoscope 🌙

A horoscope app that actually feels personal. Enter your birth date, pick a reading type, and get AI-generated insights tailored to your zodiac sign.

Built with FastAPI + OpenAI. Deploys to Vercel in one click.

---

## What it does

You enter your name and birthday. The app figures out your zodiac sign and generates a reading based on what you're looking for — daily guidance, love life, career stuff, health, or a bit of everything.

The readings adapt to your sign's element (fire, earth, air, water) with matching colors and vibes. You also get lucky numbers and colors because why not.

---

## Running locally

```bash
git clone https://github.com/yeshwanthreddy12/production-ready-AI.git
cd deploy

pip install -r requirements.txt

export OPENAI_API_KEY="your-key"

uvicorn app.main:app --reload
```

Then open `localhost:8000`.

---

## Deploying

Push to GitHub, import into Vercel, add your `OPENAI_API_KEY` as an environment variable, done.

---

## Project layout

```
app/
  main.py        → routes
  zodiac.py      → sign calculations + data
  horoscope.py   → AI generation logic
  templates.py   → HTML/CSS

instant.py       → Vercel entry point
requirements.txt
vercel.json
```

---

## Stack

- **FastAPI** for the backend
- **OpenAI GPT-4o-mini** for generating readings
- **Vercel** for hosting
- Plain CSS for the starfield animations and styling

---

## Notes

The AI is prompted to be insightful but not generic. It references your sign's traits and gives actual advice instead of vague fortune cookie stuff.

Element colors:
- Fire signs → orange/red tones
- Earth signs → greens
- Air signs → blues/cyans  
- Water signs → purples

---

MIT License. Do whatever you want with it.
