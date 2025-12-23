"""Main FastAPI application with route handlers."""

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from .zodiac import get_zodiac_sign
from .horoscope import generate_horoscope
from .templates import render_home_page, render_reading_page

app = FastAPI(
    title="Celestial Horoscope",
    description="AI-Powered Zodiac Readings",
    version="1.0.0"
)


@app.get("/", response_class=HTMLResponse)
def home():
    """Render the home page with birth details form."""
    return render_home_page()


@app.post("/horoscope", response_class=HTMLResponse)
def get_horoscope(
    name: str = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    year: int = Form(...),
    reading_type: str = Form("daily")
):
    """Generate and display a personalized horoscope."""
    # Calculate zodiac sign from birth date
    sign = get_zodiac_sign(month, day)
    
    # Generate AI-powered horoscope
    horoscope = generate_horoscope(
        name=name,
        sign=sign,
        birth_month=month,
        birth_day=day,
        birth_year=year,
        reading_type=reading_type
    )
    
    # Render the reading page
    return render_reading_page(
        name=name,
        sign=sign,
        reading_type=reading_type,
        horoscope=horoscope
    )

