from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import scraper

TOKEN = "INSERT API TOKEN HERE"
BOT_USERNAME = "INSERT BOT USERNAME HERE"

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Enter a carplate to check vehicle details!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Enter vehicle plate number to get vehicle info")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Custom")



# Responses
def handle_response(text: str) -> None:
    text_lower: str = text.lower()

    # Checksum checker
    status_msg, valid_plate = checksum.plate_check(text_upper)

    if valid_plate == True:
        result = scraper.main(text_upper)
        return result
    else: 
        return status_msg



# Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_type: str = update.message.chat.type
    message_text: str = update.message.text

    print(f"Message from user ({update.message.chat.id}) in {message_type}: '{message_text}'")

    # Check if message from group or direct messaging
    if message_type == "group" or message_type == "supergroup":
        if BOT_USERNAME in message_text:
            new_text: str = message_text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(message_text)
    
    print("Bot: ", response)
    await update.message.reply_text(response)



# Error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"Update {update} caused error {context.error}")



def main() -> None:
    # Create app and pass bot's token
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handlers
    app.add_error_handler(error)

    # Polls bot
    print("Polling...")
    app.run_polling(poll_interval = 3)


if __name__ == "__main__":
    main()
