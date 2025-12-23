"""
Celestial Horoscope - Entry Point for Vercel Deployment

This file serves as the entry point for Vercel's Python runtime.
The actual application logic is organized in the app/ package.
"""

from app.main import app

# Vercel looks for 'app' in this file
__all__ = ["app"]
