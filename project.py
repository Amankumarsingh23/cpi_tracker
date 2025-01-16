# import pandas as pd
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# # from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
# # from telegram.ext.filters import Filters


# # Load the Excel sheets
# sheet1 = pd.read_excel("Copy of Y23 UG SPI_CPI IITK(1).xlsx")  # Replace with your file name
# sheet2 = pd.read_excel("Copy of Y23 UG SPI_CPI IITK(1).xlsx")  # Replace with your file name

# # Combine the sheets
# data = pd.concat([sheet1, sheet2], ignore_index=True)

# # Create a dictionary for quick lookup
# cgpa_dict = dict(zip(data['Roll Number'], data['2024-25 1']))  # Replace column names accordingly

# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("Welcome! Send me a roll number, and I'll return the CGPA.")

# def get_cgpa(update: Update, context: CallbackContext) -> None:
#     roll_no = update.message.text.strip()
#     if roll_no in cgpa_dict:
#         cgpa = cgpa_dict[roll_no]
#         update.message.reply_text(f"The CGPA for roll number {roll_no} is {cgpa}.")
#     else:
#         update.message.reply_text("Roll number not found. Please try again.")

# def main():
#     # Replace 'YOUR_BOT_TOKEN' with your actual bot token
#     updater = Updater("8110170267:AAEmmgqdJeKmjyNegqx2HSxiN5hmYoEJAUw")
#     dispatcher = updater.dispatcher

#     # Add command and message handlers
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_cgpa))

#     # Start the bot
#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()



import pandas as pd
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Load the Excel sheets
sheet1 = pd.read_excel("Copy of Y23 UG SPI_CPI IITK(1).xlsx")  # Replace with your file name
sheet2 = pd.read_excel("Copy of Y23 UG SPI_CPI IITK(1).xlsx")  # Replace with your file name

# Combine the sheets
data = pd.concat([sheet1, sheet2], ignore_index=True)

# Strip any leading or trailing spaces from column names
data.columns = data.columns.str.strip()

# Convert 'Roll Number' to string to ensure it matches the input type
data['Roll Number'] = data['Roll Number'].astype(str)

# Create a dictionary for quick lookup
cgpa_dict = dict(zip(data['Roll Number'], data['2024-25 1']))  # Replace column names accordingly

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Send me a roll number, and I'll return the CGPA.")

def get_cgpa(update: Update, context: CallbackContext) -> None:
    roll_no = update.message.text.strip()  # Clean the input roll number
    print(f"Received roll number: {roll_no}")  # Debugging: Check input

    # Ensure roll numbers in dictionary are strings
    if roll_no in cgpa_dict:
        cgpa = cgpa_dict[roll_no]
        update.message.reply_text(f"The CGPA for roll number {roll_no} is {cgpa}.")
    else:
        update.message.reply_text("Roll number not found. Please try again.")

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("8110170267:AAEmmgqdJeKmjyNegqx2HSxiN5hmYoEJAUw")
    dispatcher = updater.dispatcher

    # Add command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_cgpa))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
