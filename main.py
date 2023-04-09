import telebot
from telebot import types
import Config
import BooksList

bot = telebot.TeleBot(Config.TOKEN)
current_menu = 1
feedback_writer = False
last_message = str


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     "Welcome " + str(message.from_user.username) +
                     ". Choose one option\U00002199", reply_markup=main_menu())


def main_menu():
    global current_menu
    markup_reply_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Books\U0001F4DA")
    item2 = types.KeyboardButton("Send Feedback")
    item3 = types.KeyboardButton("Feedbacks")
    item4 = types.KeyboardButton("Our Instagram")
    markup_reply_main.add(item1, item2, item3, item4)
    current_menu = 1
    return markup_reply_main


def books():
    global current_menu
    markup_reply_submenu1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Horror")
    item2 = types.KeyboardButton("Historical Fiction")
    item3 = types.KeyboardButton("In Russian language")
    item4 = types.KeyboardButton("Fantasy")
    item5 = types.KeyboardButton("Novels")
    item6 = types.KeyboardButton("All Catalog")
    item7 = types.KeyboardButton("Back")
    markup_reply_submenu1.add(item1, item2, item3, item4, item5, item6, item7)
    current_menu = 2
    return markup_reply_submenu1


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "If you have some problems with bot,"
                                      "please contact \U0001F4E8 with @Kutman07, and tell him your problem.")


@bot.message_handler(content_types=['text'])
def handler(message):
    global current_menu
    global feedback_writer
    global last_message
    last_message = message.text

    if message.text == "Books\U0001F4DA":
        bot.send_message(message.chat.id, text="Choose a type:", reply_markup=books())
    elif message.text == "Our Instagram":
        markup_inline = types.InlineKeyboardMarkup()
        open_link = types.InlineKeyboardButton(text="megabookskg", url="https://www.instagram.com/megabookskg/")
        markup_inline.add(open_link)
        bot.send_message(message.chat.id, "⬇️Our Instagram Page \U0001F4F7", reply_markup=markup_inline)
        feedback_writer = True
    elif message.text == "Horror":
        current_menu = 3
        bot.send_message(message.chat.id, "Horror", reply_markup=BooksList.catalog(0, 3))
    elif message.text == "Historical Fiction":
        current_menu = 3
        bot.send_message(message.chat.id, "Historical Fiction", reply_markup=BooksList.catalog(3, 6))
    elif message.text == "In Russian language":
        current_menu = 3
        bot.send_message(message.chat.id, "In Russian language", reply_markup=BooksList.catalog(6, 9))
    elif message.text == "Fantasy":
        current_menu = 3
        bot.send_message(message.chat.id, "Fantasy", reply_markup=BooksList.catalog(9, 12))
    elif message.text == "Novels":
        current_menu = 3
        bot.send_message(message.chat.id, "Novels", reply_markup=BooksList.catalog(12, 15))
    elif message.text == "All Catalog":
        current_menu = 3
        bot.send_message(message.chat.id, "All Books:", reply_markup=BooksList.catalog(0, 22))
    elif message.text == "Harry Potter":
        current_menu = 4
        bot.send_message(message.chat.id, "Harry Potter:", reply_markup=BooksList.catalog(15, 22))
    elif message.text == "Back":
        if current_menu == 2:
            bot.send_message(message.chat.id, "Back", reply_markup=main_menu())
        elif current_menu == 3:
            bot.send_message(message.chat.id, "Back", reply_markup=books())
        else:
            bot.send_message(message.chat.id, "Back", reply_markup=main_menu())
    elif message.text in BooksList.books:
        inline_markup = types.InlineKeyboardMarkup()
        open_link1 = types.InlineKeyboardButton(text="Yes", callback_data="buy_yes")
        inline_markup.add(open_link1)
        bot.send_photo(message.chat.id, BooksList.books[message.text][1])
        bot.send_message(message.chat.id, text="Do you want to read?", reply_markup=inline_markup)
    elif message.text == "Feedbacks":
        with open("feedback.txt", "r", encoding="utf-8") as file:
            bot.send_message(message.chat.id, file.read())
    elif message.text == "Send Feedback":
        bot.send_message(message.chat.id,
                         "Type your feedback or recommendation below\U0001F447")
        feedback_writer = True
    elif feedback_writer:
        with open("feedback.txt", "a", encoding="utf-8") as file:
            file.write(message.from_user.first_name + "\n")
            file.write(message.text + "\n")
            file.write("\n\n")
            bot.send_message(message.chat.id, "Thank you for your feedback, We will try to make it better")
            feedback_writer = False
    else:
        bot.send_message(message.chat.id, 'Please choose one option in options!, if you need help type: /help')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global last_message
    if call.data == "buy_yes":
        bot.send_document(call.message.chat.id, BooksList.books[last_message][0])
        bot.send_message(call.message.chat.id, "If everything is OK, please send Feedback about your experience!")
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                  text="If everything is OK, please send Feedback about your experience!")


# RUN
bot.polling(none_stop=True)
