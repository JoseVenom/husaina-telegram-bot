import os
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("ERROR: BOT_TOKEN not set!")
    exit(1)

print(f"Token starts with: {TOKEN[:10]}...")

async def start(update: Update, context):
    await update.message.reply_text("Bot is working!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Bot started...")
app.run_polling()