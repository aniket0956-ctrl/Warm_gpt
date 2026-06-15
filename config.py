import os
from dotenv import load_dotenv
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required")

ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", "0"))

# Channels to join
REQUIRED_CHANNELS = [
    {
        "name": "AI",
        "url": "https://t.me/annu_proo",
        "chat_id": "@annu_proo"
    }
]

# Developer info
DEVELOPER_USERNAME = "@ANNU_NG"

# Welcome message
WELCOME_MESSAGE = "🎉 *Welcome to Worm GPT NaNo12a AI* 🎉\n\nYour advanced AI assistant is ready to help you\\!"

# Venice AI Configuration
VENICE_AI_HEADERS = {
    'authority': 'outerface.venice.ai',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://venice.ai',
    'referer': 'https://venice.ai/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-venice-version': 'interface@20250626.212124+945291c',
}

VENICE_AI_COOKIES = {}
