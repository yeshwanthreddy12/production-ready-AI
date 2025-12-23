"""HTML templates and styling for the horoscope app."""

from datetime import datetime
from .zodiac import ZODIAC_SIGNS, get_element_colors
from .horoscope import get_reading_title, get_section_icon


def get_base_styles() -> str:
    """Return the base CSS styles."""
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Raleway:wght@300;400;500;600&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --deep-space: #0d0d1a;
            --cosmic-blue: #1a1a2e;
            --stellar-purple: #16213e;
            --gold-accent: #ffd700;
            --soft-white: #f0e6d3;
            --muted-lavender: #b8b8d1;
        }
        
        body {
            font-family: 'Raleway', sans-serif;
            background: var(--deep-space);
            min-height: 100vh;
            color: var(--soft-white);
            overflow-x: hidden;
        }
        
        .starfield {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            background: 
                radial-gradient(ellipse at 10% 90%, rgba(75, 0, 130, 0.15) 0%, transparent 50%),
                radial-gradient(ellipse at 90% 10%, rgba(0, 100, 150, 0.15) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 50%, rgba(255, 215, 0, 0.03) 0%, transparent 60%),
                linear-gradient(180deg, #0d0d1a 0%, #1a1a2e 50%, #0d0d1a 100%);
        }
        
        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background-image: 
                radial-gradient(1px 1px at 50px 50px, #fff, transparent),
                radial-gradient(1px 1px at 100px 150px, #ffd700, transparent),
                radial-gradient(1.5px 1.5px at 200px 100px, #fff, transparent),
                radial-gradient(1px 1px at 300px 250px, #b8b8d1, transparent),
                radial-gradient(1px 1px at 400px 50px, #ffd700, transparent),
                radial-gradient(1.5px 1.5px at 500px 200px, #fff, transparent),
                radial-gradient(1px 1px at 150px 300px, #fff, transparent),
                radial-gradient(1px 1px at 250px 400px, #ffd700, transparent),
                radial-gradient(1px 1px at 350px 350px, #fff, transparent),
                radial-gradient(1.5px 1.5px at 450px 450px, #b8b8d1, transparent);
            background-size: 550px 500px;
            animation: twinkle 6s ease-in-out infinite;
        }
        
        @keyframes twinkle {
            0%, 100% { opacity: 0.6; }
            50% { opacity: 1; }
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 50px 25px;
            min-height: 100vh;
        }
        
        header {
            text-align: center;
            margin-bottom: 50px;
        }
        
        .logo {
            font-size: 3rem;
            margin-bottom: 15px;
            animation: float 4s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
        
        h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2rem, 5vw, 3rem);
            font-weight: 700;
            margin-bottom: 10px;
            background: linear-gradient(135deg, var(--gold-accent) 0%, #fff 50%, var(--gold-accent) 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 3s linear infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: 200% center; }
            100% { background-position: -200% center; }
        }
        
        .tagline {
            font-size: 1.1rem;
            color: var(--muted-lavender);
            font-weight: 300;
            letter-spacing: 2px;
        }
        
        .form-card {
            background: rgba(26, 26, 46, 0.8);
            border: 1px solid rgba(255, 215, 0, 0.15);
            border-radius: 20px;
            padding: 40px;
            backdrop-filter: blur(10px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
        }
        
        .form-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            text-align: center;
            margin-bottom: 30px;
            color: var(--gold-accent);
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: var(--soft-white);
            font-size: 0.95rem;
        }
        
        input, select {
            width: 100%;
            padding: 15px 20px;
            font-family: 'Raleway', sans-serif;
            font-size: 1rem;
            color: var(--soft-white);
            background: rgba(13, 13, 26, 0.8);
            border: 1px solid rgba(255, 215, 0, 0.2);
            border-radius: 10px;
            outline: none;
            transition: all 0.3s ease;
        }
        
        input:focus, select:focus {
            border-color: var(--gold-accent);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.15);
        }
        
        input::placeholder {
            color: var(--muted-lavender);
            opacity: 0.6;
        }
        
        select option {
            background: var(--cosmic-blue);
            color: var(--soft-white);
        }
        
        .date-row {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 15px;
        }
        
        button {
            width: 100%;
            padding: 18px;
            font-family: 'Playfair Display', serif;
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--deep-space);
            background: linear-gradient(135deg, var(--gold-accent) 0%, #f0c800 100%);
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.4s ease;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-top: 10px;
        }
        
        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(255, 215, 0, 0.3);
        }
        
        .zodiac-wheel {
            display: flex;
            justify-content: center;
            gap: 8px;
            margin: 40px 0;
            flex-wrap: wrap;
        }
        
        .zodiac-icon {
            font-size: 1.5rem;
            opacity: 0.4;
            transition: all 0.3s ease;
        }
        
        .zodiac-icon:hover {
            opacity: 1;
            transform: scale(1.3);
        }
        
        .reading-card {
            background: rgba(26, 26, 46, 0.9);
            border: 1px solid rgba(255, 215, 0, 0.2);
            border-radius: 20px;
            padding: 50px 40px;
            backdrop-filter: blur(10px);
            animation: fadeIn 0.8s ease-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .sign-header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 30px;
            border-bottom: 1px solid rgba(255, 215, 0, 0.15);
        }
        
        .sign-symbol {
            font-size: 5rem;
            margin-bottom: 15px;
            display: block;
        }
        
        .sign-name {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            text-transform: capitalize;
            margin-bottom: 10px;
        }
        
        .sign-meta {
            display: flex;
            justify-content: center;
            gap: 30px;
            color: var(--muted-lavender);
            font-size: 0.95rem;
        }
        
        .sign-meta span {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .element-badge {
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
        }
        
        .greeting {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-style: italic;
            color: var(--gold-accent);
            text-align: center;
            margin-bottom: 30px;
        }
        
        .reading-section {
            margin-bottom: 35px;
        }
        
        .reading-section h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
            color: var(--gold-accent);
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .reading-text {
            font-size: 1.1rem;
            line-height: 1.9;
            color: var(--soft-white);
        }
        
        .cosmic-numbers {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 40px;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 215, 0, 0.15);
        }
        
        .cosmic-number {
            text-align: center;
            padding: 20px;
            background: rgba(255, 215, 0, 0.05);
            border-radius: 12px;
        }
        
        .cosmic-number .label {
            font-size: 0.8rem;
            color: var(--muted-lavender);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        
        .cosmic-number .value {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            color: var(--gold-accent);
        }
        
        .back-link {
            display: inline-block;
            margin-top: 40px;
            color: var(--muted-lavender);
            text-decoration: none;
            font-size: 0.95rem;
            transition: color 0.3s ease;
        }
        
        .back-link:hover {
            color: var(--gold-accent);
        }
        
        footer {
            text-align: center;
            margin-top: 50px;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 215, 0, 0.1);
            color: var(--muted-lavender);
            font-size: 0.85rem;
        }
        
        @media (max-width: 600px) {
            .container { padding: 30px 20px; }
            .form-card, .reading-card { padding: 30px 20px; }
            .date-row { grid-template-columns: 1fr; }
            .sign-meta { flex-direction: column; gap: 10px; }
            .cosmic-numbers { grid-template-columns: 1fr; }
        }
    </style>
    """


def render_home_page() -> str:
    """Render the home page HTML."""
    zodiac_icons = "".join([
        f'<span class="zodiac-icon">{data["symbol"]}</span>' 
        for data in ZODIAC_SIGNS.values()
    ])
    
    months = "".join([
        f'<option value="{i}">{datetime(2000, i, 1).strftime("%B")}</option>' 
        for i in range(1, 13)
    ])
    days = "".join([f'<option value="{i}">{i}</option>' for i in range(1, 32)])
    current_year = datetime.now().year
    years = "".join([
        f'<option value="{y}">{y}</option>' 
        for y in range(current_year, current_year - 100, -1)
    ])
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Celestial Horoscope · Your Daily Star Guide</title>
        <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⭐</text></svg>">
        {get_base_styles()}
    </head>
    <body>
        <div class="starfield"></div>
        <div class="stars"></div>
        
        <div class="container">
            <header>
                <div class="logo">✨🌙✨</div>
                <h1>Celestial Horoscope</h1>
                <p class="tagline">Discover What the Stars Have Written for You</p>
            </header>
            
            <div class="zodiac-wheel">
                {zodiac_icons}
            </div>
            
            <div class="form-card">
                <h2 class="form-title">Enter Your Birth Details</h2>
                
                <form action="/horoscope" method="post">
                    <div class="form-group">
                        <label for="name">Your Name</label>
                        <input type="text" id="name" name="name" placeholder="Enter your name" required>
                    </div>
                    
                    <div class="form-group">
                        <label>Date of Birth</label>
                        <div class="date-row">
                            <select name="month" required>
                                <option value="">Month</option>
                                {months}
                            </select>
                            <select name="day" required>
                                <option value="">Day</option>
                                {days}
                            </select>
                            <select name="year" required>
                                <option value="">Year</option>
                                {years}
                            </select>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="reading_type">Type of Reading</label>
                        <select id="reading_type" name="reading_type">
                            <option value="daily">Daily Horoscope</option>
                            <option value="love">Love & Relationships</option>
                            <option value="career">Career & Finance</option>
                            <option value="health">Health & Wellness</option>
                            <option value="comprehensive">Comprehensive Reading</option>
                        </select>
                    </div>
                    
                    <button type="submit">Reveal My Horoscope ✨</button>
                </form>
            </div>
            
            <footer>
                ⭐ Powered by AI & Ancient Astrological Wisdom ⭐
            </footer>
        </div>
    </body>
    </html>
    """


def render_reading_page(
    name: str,
    sign: str,
    reading_type: str,
    horoscope: dict
) -> str:
    """Render the horoscope reading page HTML."""
    sign_data = ZODIAC_SIGNS[sign]
    element = sign_data["element"]
    colors = get_element_colors(element)
    
    # Build sections HTML
    sections_html = ""
    for section, content in horoscope["sections"].items():
        icon = get_section_icon(section)
        title = section.replace("_", " ").title()
        sections_html += f"""
        <div class="reading-section">
            <h3>{icon} {title}</h3>
            <p class="reading-text">{content}</p>
        </div>
        """
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{name}'s {sign.title()} Horoscope · Celestial Horoscope</title>
        <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⭐</text></svg>">
        {get_base_styles()}
        <style>
            .sign-symbol {{ color: {colors["primary"]}; text-shadow: 0 0 30px {colors["glow"]}; }}
            .sign-name {{ color: {colors["primary"]}; }}
            .element-badge {{ background: {colors["glow"]}; color: {colors["primary"]}; }}
        </style>
    </head>
    <body>
        <div class="starfield"></div>
        <div class="stars"></div>
        
        <div class="container">
            <div class="reading-card">
                <div class="sign-header">
                    <span class="sign-symbol">{sign_data["symbol"]}</span>
                    <h1 class="sign-name">{sign.title()}</h1>
                    <div class="sign-meta">
                        <span>{sign_data["constellation"]} {sign_data["dates"]}</span>
                        <span class="element-badge">{element} Sign</span>
                    </div>
                </div>
                
                <p class="greeting">Welcome, {name}. The cosmos has a message for you...</p>
                
                <h2 style="text-align: center; font-family: 'Playfair Display', serif; color: var(--gold-accent); margin-bottom: 30px;">
                    {get_reading_title(reading_type)}
                </h2>
                
                {sections_html}
                
                <div class="cosmic-numbers">
                    <div class="cosmic-number">
                        <div class="label">Lucky Number</div>
                        <div class="value">{horoscope["lucky_number"]}</div>
                    </div>
                    <div class="cosmic-number">
                        <div class="label">Lucky Color</div>
                        <div class="value">{horoscope["lucky_color"]}</div>
                    </div>
                    <div class="cosmic-number">
                        <div class="label">Cosmic Energy</div>
                        <div class="value">{horoscope["energy_level"]}%</div>
                    </div>
                </div>
                
                <a href="/" class="back-link">← Get Another Reading</a>
            </div>
            
            <footer>
                ⭐ Powered by AI & Ancient Astrological Wisdom ⭐
            </footer>
        </div>
    </body>
    </html>
    """

