
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, ContextTypes, filters
from datetime import datetime
from config import TOKEN, ADMIN_IDS
from database import add, agree, export_csv
from pdf_generator import create_pdf

NAME, PASSPORT, NATIONALITY, DATE = range(4)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["recruiter"] = context.args[0] if context.args else "direct"
    await update.message.reply_text("Full Name?")
    return NAME

async def n(update, context):
    context.user_data["full_name"]=update.message.text
    await update.message.reply_text("Passport/NIC?")
    return PASSPORT

async def p(update, context):
    context.user_data["passport"]=update.message.text
    await update.message.reply_text("Nationality?")
    return NATIONALITY

async def nat(update, context):
    context.user_data["nationality"]=update.message.text
    await update.message.reply_text("Start Date?")
    return DATE

async def d(update, context):
    u = update.effective_user
    context.user_data["start_date"]=update.message.text
    context.user_data["telegram_id"]=str(u.id)
    context.user_data["username"]=u.username or ""
    add(context.user_data)

    pdf = f"{u.id}_agreement.pdf"
    create_pdf(pdf, context.user_data)

    kb=[[InlineKeyboardButton("✅ I Agree", callback_data="agree")]]
    await update.message.reply_document(document=open(pdf,"rb"))
    await update.message.reply_text("Review agreement and accept.", reply_markup=InlineKeyboardMarkup(kb))
    return ConversationHandler.END

async def accept(update, context):
    q=update.callback_query
    await q.answer()
    agree(str(q.from_user.id), datetime.utcnow().isoformat())
    await q.edit_message_text("Agreement accepted. Welcome.")
    for admin in ADMIN_IDS:
        try:
            await context.bot.send_message(admin, f"New accepted applicant: @{q.from_user.username}")
        except:
            pass

async def export_cmd(update, context):
    if update.effective_user.id not in ADMIN_IDS:
        return
    path = export_csv()
    await update.message.reply_document(document=open(path,"rb"))

app = Application.builder().token(TOKEN).build()

conv = ConversationHandler(
entry_points=[CommandHandler("start", start)],
states={
NAME:[MessageHandler(filters.TEXT & ~filters.COMMAND, n)],
PASSPORT:[MessageHandler(filters.TEXT & ~filters.COMMAND, p)],
NATIONALITY:[MessageHandler(filters.TEXT & ~filters.COMMAND, nat)],
DATE:[MessageHandler(filters.TEXT & ~filters.COMMAND, d)]
},
fallbacks=[]
)

app.add_handler(conv)
app.add_handler(CallbackQueryHandler(accept, pattern="agree"))
app.add_handler(CommandHandler("export", export_cmd))

if __name__ == "__main__":
    app.run_polling()
