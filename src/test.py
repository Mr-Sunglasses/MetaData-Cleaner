import time

from API import API_KEY
import telebot
from exif import Image

bot = telebot.TeleBot(API_KEY)


# Handle Messages with /start and /help
@bot.message_handler(commands=['help', 'start'])
def send_message_with_these_commands(message):
    bot.reply_to(message, """\
    Hey I'm Image Secure Bot, I am Here to Save you from hackers, start with these commands\n
    /image_clear - to clear the metadata of the Image\n
    /image_read - to read the metadata of the Image\n
    Our Goal is to secure and respect your privacy that is why we doesn't save any of your metadata of your image and we also have an enable encryption for the send and receiving of your metadata and we are also Open-Source so you can check the source code by yourself.\
    """)


@bot.message_handler(commands=['image_read', 'img_read'])
def send_message_for_image_read(message):
    msg = bot.reply_to(message, """\
    Please Send Me the Picture Which You want to Read the Metadata
    """)
    bot.register_next_step_handler(msg, image_saver)


@bot.message_handler(content_types=['photo'])
def image_saver(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    msg = bot.reply_to(message, "Please Wait while We are Reading the Image, Enter Yes if you want us to read the image")
    # bot.register_next_step_handler(msg, image_reader)
    time.sleep(10)
    with open("image.jpg", "rb") as image_file:
        my_image = Image(image_file)
    if my_image.has_exif:
        bot.reply_to(message, "This file has exif Data")
    else:
        bot.reply_to(message, "This file Does not have any Exif Data")

# def image_reader(message):
#     chat_id = message.chat.id
#     confirm = message.text
#     # if confirm == u'Yes' or confirm == u'No':
#     #     confirm = confirm
#
#     if confirm == 'Yes':
#         with open("image.jpg", "rb") as image_file:
#             my_image = Image(image_file)
#         if my_image.has_exif:
#             bot.reply_to(message, "This file has exif Data")
#         else:
#             bot.reply_to(message, "This file Does not have any Exif Data")
#     else:
#         bot.send_message(chat_id, "Thanks for using the Bot")




# bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()

bot.infinity_polling()
