from API import API_KEY
import telebot

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
    bot.register_next_step_handler(msg, process_name_step)

@bot.message_handler(content_types=['photo'])
def process_name_step(message):
    # try:
    chat_id = message.chat.id
    name = message.photo
    msg = bot.send_photo(message, photo=name)
    # except Exception as e:
    #     bot.reply_to(message, 'oooops')


bot.infinity_polling()
