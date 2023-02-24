import telebot
from telebot import types

bot = telebot.TeleBot("5639983988:AAFOeQR2F1iJZ_FihRHltjqosrCDcF9JigA")

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Question 1!")
    item2 = types.KeyboardButton("Question 2!")
    item3 = types.KeyboardButton("Question 3!")
    item4 = types.KeyboardButton("Question 4!")
    item5 = types.KeyboardButton("Question 5!")
    item6 = types.KeyboardButton("Question 6!")
    item7 = types.KeyboardButton("Question 7!")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id,
                     "Welcome, {0.first_name}!\nI am - <b>{1.first_name}</b>, "
                     "The music quiz bot. I will test your knowledge about the great art of music. Lets begin!!!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def dialog(message):
    if message.chat.type == 'private':
        if message.text == 'Question 1!':
            bot.send_message(message.chat.id, "Ok , first question: ")
            bot.send_message(message.chat.id, "What band was Harry Styles in before his solo career?")
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("One direction", callback_data='good')
            item2 = types.InlineKeyboardButton("Bts", callback_data='bad')
            item3 = types.InlineKeyboardButton("Big time rush", callback_data='bad')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Hope you get it right!', reply_markup=markup)
        elif message.text == 'Question 2!':
            bot.send_message(message.chat.id, "Next question: ")
            bot.send_message(message.chat.id, "Who sings Never gonna give you up ?")
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("SixNine", callback_data='bad')
            item2 = types.InlineKeyboardButton("Carla's Dreams", callback_data='bad')
            item3 = types.InlineKeyboardButton("Rick Astley", callback_data='good')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Hope you get it right!', reply_markup=markup)

        elif message.text == 'Question 3!':
            bot.send_message(message.chat.id, "Next question: ")
            bot.send_message(message.chat.id, "Where is Cleopatra Stratan from?")
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Romania", callback_data='bad')
            item2 = types.InlineKeyboardButton("Italy", callback_data='bad')
            item3 = types.InlineKeyboardButton("Republic of Moldova", callback_data='good')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Hope you get it right!', reply_markup=markup)

        elif message.text == 'Question 4!':
            bot.send_message(message.chat.id, "Next question: ")
            bot.send_message(message.chat.id, "Wich one of these was an Iconic Singer?")
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Leonardo Dicaprio", callback_data='bad')
            item2 = types.InlineKeyboardButton("Michael Jackson", callback_data='good')
            item3 = types.InlineKeyboardButton("Arnold Schwarzenegger", callback_data='bad')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Hope you get it right!', reply_markup=markup)

        elif message.text == 'Question 5!':
            bot.send_message(message.chat.id, "Next question: ")
            bot.send_message(message.chat.id, "Its beatbox considered music ?")
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("No", callback_data='bad')
            item2 = types.InlineKeyboardButton("Yes", callback_data='good')

            markup.add(item1, item2,)

            bot.send_message(message.chat.id, 'Hope you get it right!', reply_markup=markup)

        elif message.text == 'Question 6!':
            bot.send_message(message.chat.id, "Next question: ")
            bot.send_message(message.chat.id, "Where is the Alternosfera band from?")
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("United Kingdom", callback_data='bad')
            item2 = types.InlineKeyboardButton("Republic of Moldova", callback_data='good')
            item3 = types.InlineKeyboardButton("United states of America", callback_data='bad')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Hope you get it right!', reply_markup=markup)

        elif message.text == 'Question 7!':
            bot.send_message(message.chat.id, "Next question: ")
            bot.send_message(message.chat.id, "In which year did Republic of Moldova win 3rd place at Eurovision ?")
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("2005", callback_data='good')
            item2 = types.InlineKeyboardButton("1990", callback_data='bad')
            item3 = types.InlineKeyboardButton("30 October 2006", callback_data='bad')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Hope you get it right!', reply_markup=markup)
            bot.send_message(message.chat.id, "You finished the quiz ! Congratulations !!!")

        else:
            bot.send_message(message.chat.id, "I don't have an answer fot that 😢")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Correct 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'No, thats not correct =((')

            # show alert
            """bot.answer_callback_query(callback_query_id=call.id,
                                      show_alert=True,
                                      text="You finished the quiz! Congratulations !!!")"""

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)