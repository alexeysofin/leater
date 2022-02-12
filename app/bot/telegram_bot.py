import logging

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    Filters,
)
from telegram import Update

from app.ingest.tasks import ingest_document
from app.settings import TELEGRAM_BOT_KEY


updater = Updater(token=TELEGRAM_BOT_KEY)
dispatcher = updater.dispatcher

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def message(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    ingest_document.delay(text=update.message.text)
    update.message.reply_text("Saved successfully")



def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message))

def run():
    updater.start_polling()
    updater.idle()

