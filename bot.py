import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

keyboard = [
    ["🚗 Rent", "📋 Availability"],
    ["💰 Pricing", "📄 Requirements"],
    ["📞 Contact", "📦 Status"],
    ["🎁 Referral"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

WELCOME = """
🚗 Welcome to Dasher Rental Accounts!

Choose an option below to get started.

We offer fast approvals, reliable accounts, and responsive support.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME, reply_markup=reply_markup)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    responses = {
        "🚗 Rent": "📝 Rental Application\n\nPlease contact support to begin your rental application.",
        "📋 Availability": "📋 Available Accounts\n\n• Daily Rentals\n• Weekly Rentals\n\nContact us for current availability.",
        "💰 Pricing": "💰 Pricing\n\nDaily: $XX\nWeekly: $XXX\n\nDM for current rates.",
        "📄 Requirements": "📄 Requirements\n\n✅ Valid Driver's License\n✅ Deposit (if required)\n✅ Telegram account",
        "📞 Contact": "📞 Customer Support\n\nMessage: @YourTelegramUsername",
        "📦 Status": "📦 To check your rental status, send your order number to support.",
        "🎁 Referral": "🎁 Referral Program\n\nInvite a friend and earn rewards after their first rental!"
    }

    await update.message.reply_text(responses.get(text, "Please choose an option from the menu."))

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("Bot is running...")
app.run_polling()
