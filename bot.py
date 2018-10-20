from telegram.ext import Updater, CommandHandler
message = 'ali'

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(message))


updater = Updater("779192354:AAFK48m0Mw8pzW7EjYR8JCeESanIOLt8fyM")

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
