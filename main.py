import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return

    user = update.effective_user

    text = (
        f"👤 نام: {user.full_name}\n"
        f"📛 یوزرنیم: @{user.username if user.username else 'ندارد'}\n"
        f"🆔 آیدی: {user.id}"
    )

    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=text
    )

    await context.bot.copy_message(
        chat_id=OWNER_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id,
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, save))

print("Bot is running...")

app.run_polling()
