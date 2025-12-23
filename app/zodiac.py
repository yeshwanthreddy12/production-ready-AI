"""Zodiac sign data and calculation utilities."""

from datetime import datetime

ZODIAC_SIGNS = {
    "aries": {
        "symbol": "♈",
        "element": "Fire",
        "dates": "Mar 21 - Apr 19",
        "constellation": "🐏",
        "traits": ["bold", "ambitious", "energetic", "pioneering"]
    },
    "taurus": {
        "symbol": "♉",
        "element": "Earth",
        "dates": "Apr 20 - May 20",
        "constellation": "🐂",
        "traits": ["reliable", "patient", "practical", "devoted"]
    },
    "gemini": {
        "symbol": "♊",
        "element": "Air",
        "dates": "May 21 - Jun 20",
        "constellation": "👯",
        "traits": ["adaptable", "curious", "expressive", "witty"]
    },
    "cancer": {
        "symbol": "♋",
        "element": "Water",
        "dates": "Jun 21 - Jul 22",
        "constellation": "🦀",
        "traits": ["intuitive", "emotional", "protective", "nurturing"]
    },
    "leo": {
        "symbol": "♌",
        "element": "Fire",
        "dates": "Jul 23 - Aug 22",
        "constellation": "🦁",
        "traits": ["confident", "dramatic", "generous", "charismatic"]
    },
    "virgo": {
        "symbol": "♍",
        "element": "Earth",
        "dates": "Aug 23 - Sep 22",
        "constellation": "👼",
        "traits": ["analytical", "practical", "diligent", "modest"]
    },
    "libra": {
        "symbol": "♎",
        "element": "Air",
        "dates": "Sep 23 - Oct 22",
        "constellation": "⚖️",
        "traits": ["diplomatic", "gracious", "fair-minded", "social"]
    },
    "scorpio": {
        "symbol": "♏",
        "element": "Water",
        "dates": "Oct 23 - Nov 21",
        "constellation": "🦂",
        "traits": ["passionate", "resourceful", "brave", "mysterious"]
    },
    "sagittarius": {
        "symbol": "♐",
        "element": "Fire",
        "dates": "Nov 22 - Dec 21",
        "constellation": "🏹",
        "traits": ["optimistic", "adventurous", "philosophical", "honest"]
    },
    "capricorn": {
        "symbol": "♑",
        "element": "Earth",
        "dates": "Dec 22 - Jan 19",
        "constellation": "🐐",
        "traits": ["disciplined", "responsible", "ambitious", "practical"]
    },
    "aquarius": {
        "symbol": "♒",
        "element": "Air",
        "dates": "Jan 20 - Feb 18",
        "constellation": "🏺",
        "traits": ["progressive", "original", "independent", "humanitarian"]
    },
    "pisces": {
        "symbol": "♓",
        "element": "Water",
        "dates": "Feb 19 - Mar 20",
        "constellation": "🐟",
        "traits": ["compassionate", "artistic", "intuitive", "gentle"]
    }
}

ELEMENT_COLORS = {
    "Fire": {
        "primary": "#ff6b35",
        "secondary": "#f7931e",
        "glow": "rgba(255, 107, 53, 0.4)"
    },
    "Earth": {
        "primary": "#7cb342",
        "secondary": "#558b2f",
        "glow": "rgba(124, 179, 66, 0.4)"
    },
    "Air": {
        "primary": "#29b6f6",
        "secondary": "#0288d1",
        "glow": "rgba(41, 182, 246, 0.4)"
    },
    "Water": {
        "primary": "#7e57c2",
        "secondary": "#5e35b1",
        "glow": "rgba(126, 87, 194, 0.4)"
    }
}


def get_zodiac_sign(month: int, day: int) -> str:
    """Calculate zodiac sign from birth month and day."""
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "aquarius"
    else:
        return "pisces"


def get_sign_data(sign: str) -> dict:
    """Get all data for a zodiac sign."""
    return ZODIAC_SIGNS.get(sign, ZODIAC_SIGNS["aries"])


def get_element_colors(element: str) -> dict:
    """Get color scheme for an element."""
    return ELEMENT_COLORS.get(element, ELEMENT_COLORS["Fire"])

