"""AI-powered horoscope generation service."""

import json
import random
from datetime import datetime
from openai import OpenAI

from .zodiac import get_sign_data

READING_TYPES = {
    "daily": {
        "description": "a daily horoscope with general guidance for today",
        "sections": ["general", "advice"]
    },
    "love": {
        "description": "a love and relationships focused horoscope",
        "sections": ["love", "advice"]
    },
    "career": {
        "description": "a career and financial guidance horoscope",
        "sections": ["career", "advice"]
    },
    "health": {
        "description": "a health and wellness focused horoscope",
        "sections": ["health", "advice"]
    },
    "comprehensive": {
        "description": "a comprehensive horoscope covering all life areas",
        "sections": ["general", "love", "career", "health", "advice"]
    }
}

READING_TITLES = {
    "daily": "Today's Cosmic Message",
    "love": "Love & Relationships",
    "career": "Career & Finance",
    "health": "Health & Wellness",
    "comprehensive": "Your Complete Reading"
}

SECTION_ICONS = {
    "general": "🌟",
    "love": "💫",
    "career": "🎯",
    "health": "🌿",
    "advice": "💎"
}


def get_reading_title(reading_type: str) -> str:
    """Get the display title for a reading type."""
    return READING_TITLES.get(reading_type, "Your Reading")


def get_section_icon(section: str) -> str:
    """Get the icon for a reading section."""
    return SECTION_ICONS.get(section, "✨")


def generate_horoscope(
    name: str,
    sign: str,
    birth_month: int,
    birth_day: int,
    birth_year: int,
    reading_type: str = "daily"
) -> dict:
    """Generate a personalized horoscope using AI."""
    
    sign_data = get_sign_data(sign)
    today = datetime.now().strftime("%B %d, %Y")
    
    reading_config = READING_TYPES.get(reading_type, READING_TYPES["daily"])
    sections_needed = reading_config["sections"]
    
    client = OpenAI()
    
    system_prompt = f"""You are an expert astrologer providing personalized horoscope readings. 
You combine traditional astrological wisdom with insightful, empowering guidance.

Today's date is {today}.

The person asking is named {name}, born on {birth_month}/{birth_day}/{birth_year}, making them a {sign.title()} ({sign_data["element"]} sign).
Key traits: {", ".join(sign_data.get("traits", []))}.

Provide {reading_config["description"]}.

Your response MUST be in this exact JSON format:
{{
    "sections": {{
        {", ".join([f'"{s}": "2-3 sentences of insightful content"' for s in sections_needed])}
    }},
    "lucky_number": <number between 1-99>,
    "lucky_color": "<a color name>",
    "energy_level": <number between 60-100>
}}

Guidelines:
- Be specific and insightful, not generic
- Reference {sign.title()} traits naturally
- Be encouraging but realistic
- Use vivid, evocative language
- Keep each section 2-3 meaningful sentences
- Return ONLY valid JSON, no other text"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Please provide my {reading_type} horoscope reading."}
    ]
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.8,
            max_tokens=500
        )
        horoscope = json.loads(response.choices[0].message.content)
    except Exception:
        # Fallback response if AI fails
        horoscope = _get_fallback_horoscope(sections_needed)
    
    return horoscope


def _get_fallback_horoscope(sections: list) -> dict:
    """Generate a fallback horoscope if AI is unavailable."""
    fallback_content = {
        "general": "The stars are aligning in your favor today. Trust your intuition and embrace the opportunities that come your way.",
        "love": "Your heart is open to new connections. Whether single or partnered, meaningful moments await.",
        "career": "Professional momentum is building. Your hard work is being noticed by those who matter.",
        "health": "Focus on balance today. Small acts of self-care will have lasting positive effects.",
        "advice": "Take time for self-reflection and remain open to unexpected blessings."
    }
    
    return {
        "sections": {s: fallback_content.get(s, fallback_content["general"]) for s in sections},
        "lucky_number": random.randint(1, 99),
        "lucky_color": random.choice(["Gold", "Silver", "Azure", "Emerald", "Violet", "Coral"]),
        "energy_level": random.randint(70, 95)
    }

