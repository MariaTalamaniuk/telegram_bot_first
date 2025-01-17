from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Howdy, goober. On your knees.')

def main():
    application = ApplicationBuilder().token("7658794690:AAH0mrnu9JahPQCwuu9nkAQKm1_DWM_jF0Q").build()
    application.add_handler(CommandHandler('start', start))
    print('The bot has been activated.')
    application.run_polling()

if __name__ == '__main__':
    main()