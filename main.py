import Key as keys
from telegram.ext import *
import response as R
print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Ciao! Hai bisogno di contattare un rappresentante?')
    
def help_command(update, context):
    update.message.reply_text('Hai bisogno di aiuto?')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")
    

def main():
    updater = Updater(keys.API_KEY, use_context= True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("Start", start_command))
    dp.add_handler(CommandHandler("Aiuto", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message)) 
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()
    
main()    
    





   
    
    
    
