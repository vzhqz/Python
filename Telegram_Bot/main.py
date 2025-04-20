from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import requests

# Get API keys from .env file
load_dotenv()
TOKEN: Final = os.getenv("TOKEN")
BOT_USERNAME: Final = "@coool_testing_bot"
GEMINI_API: Final = os.getenv("GEMINI_API")

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot started.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a useless ass chatbot that's still under development. I'll be useful one day.")

async def generate_useless_fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        fact = data["text"].strip('"')
        await update.message.reply_text(fact)
    else:
        await update.message.reply_text(f"Error code {response.status_code}")


# Responses
def handle_response(user_id: str, user_message: str) -> str:
    genai.configure(api_key=GEMINI_API)

    memory = user_memory.get(user_id, "")

    prompt = f"{memory}\n\nUser: {user_message}\nBot:"

    # Set up Gemini
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=(
            "You are a friendly and helpful Telegram bot."
            "Always act like a real human in conversations."
            "Write concise and understandable responses."
            "You remember details about the user like name, hobbies, preferences."
            "If the user says something new about themselves, extract and store it."
        )
    )

    response = model.generate_content(prompt)
    reply = response.text.strip()

    user_memory[user_id] = memory + f"\nUser: {user_message}\nBot: {reply}"
    save_memory(user_memory)

    return reply


def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f, indent=4)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    message_type = update.message.chat.type
    user_text = update.message.text.strip()

    print(f"User ({user_id}) in {message_type}: {user_text}")

    # Only respond in groups if bot is mentioned
    if message_type == "group":
        if BOT_USERNAME in user_text:
            user_text = user_text.replace(BOT_USERNAME, "").strip()
            response = handle_response(user_id, user_text)
        else:
            return
    else:
        response = handle_response(user_id, user_text)

    print("Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update: {update} caused error {context.error}")

if __name__ == "__main__":
    user_memory = load_memory()
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('useless_fact', generate_useless_fact))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=1)