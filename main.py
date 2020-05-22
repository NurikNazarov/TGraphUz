import telebot
from config import *
import mysql.connector
import time
from time import sleep
from telebot import types

mydb = mysql.connector.connect(
    host = "eu-cdbr-west-03.cleardb.net",
    user = "bf26de8cfb0052",
    passwd = "68604d4a",
    database = "heroku_d8087c1fa8a1200"
)

cursor = mydb.cursor()

bot = telebot.TeleBot(token = "1079973341:AAHC9ReBLb6OBU-W0q4Ds-xAKiGijDWxe_A")


def extract_unique_code(text_message):
    # Extracts the unique_code from the sent /start command.
    return text_message.split()[ 1 ] if len(text_message.split()) > 1 else None


@bot.message_handler(commands = [ "start" ])
def start(message):
    unicode = extract_unique_code(message.text)
    if unicode:
        print(unicode)
        print(message.from_user.id)
        if unicode == str(message.from_user.id):
            bot.send_message(
                message.chat.id,
                main_text,
                parse_mode = 'html'
            )
            sleep(60)
            keyboard = types.InlineKeyboardMarkup()
            key = types.InlineKeyboardButton(text = "Accept", callback_data = "accept")
            keyboard.add(key)
            bot.send_message(message.chat.id, "Rozilik bildirish uchun pastdagi knopkani bosing:",
                             reply_markup = keyboard)
        else:
            bot.reply_to(message,
                         "Bu knopka siz uchun emasdi =)\nKnopka ekan deb bosavermaydida endi...")
    else:
        bot.send_message(
            message.chat.id,
            text = start_private,
            reply_to_message_id = message.message_id,
            parse_mode = 'html'
        )


@bot.message_handler(content_types = ['new_chat_members'])
def new_member(message):
    if message.new_chat_members[ 0 ].last_name is not None:
        fullname = f'{message.new_chat_members[ 0 ].first_name} ' \
                   f'{message.new_chat_members[ 0 ].last_name} '
    else:
        fullname = f'{message.new_chat_members[ 0 ].first_name}'
    name = f"<a href='tg://user?id={message.new_chat_members[ 0 ].id}'>{fullname}</a>"
    bot.send_message(
        chat_id = message.chat.id,
        text = hello_member.format(name),
        parse_mode = 'HTML'
    )

'''
    try:
        stat = bot.get_chat_member(message.chat.id, message.new_chat_members[0].id)
        sql = "INSERT INTO user (id, status) VALUES (%s, %s)"
        val = (message.new_chat_members[0].id, stat.status)
        cursor.execute(sql, val)
        mydb.commit()
        if message.new_chat_members[0].last_name is not None:
            fullname = f'{message.new_chat_members[0].first_name} ' \
                       f'{message.new_chat_members[0].last_name} '
        else:
            fullname = f'{message.new_chat_members[0].first_name}'
        name = f"<a href='tg://user?id={message.new_chat_members[0].id}'>{fullname}</a>"
        keyb = types.InlineKeyboardMarkup()
        key = types.InlineKeyboardButton(text = "Sinovdan o'tish",
                                         url = "t.me/tgraphuz_bot?start={0}".format(message.new_chat_members[0].id))
        keyb.add(key)
        msg = bot.send_message(
              message.chat.id,
              new_m.format(name),
              parse_mode = 'html',
              reply_markup = keyb
        )
        sql = "UPDATE user SET invite_msg = %s WHERE id = %s"
        val = (msg.message_id, message.new_chat_members[0].id)
        cursor.execute(sql, val)

        mydb.commit()
        bot.restrict_chat_member(
            message.chat.id,
            message.new_chat_members[0].id
        )
    except mysql.connector.errors.IntegrityError:
        if message.new_chat_members[0].last_name is not None:
            fullname = f'{message.new_chat_members[0].first_name} ' \
                       f'{message.new_chat_members[0].last_name} '
        else:
            fullname = f'{message.new_chat_members[0].first_name}'
        name = f"<a href='tg://user?id={message.new_chat_members[0].id}'>{fullname}</a>"
        bot.send_message(
            message.chat.id,
            friend_come.format(name),
            parse_mode = 'html'
        )
'''


@bot.message_handler(content_types = ['text'])
def text(message):
    user = bot.get_chat_member(message.chat.id, message.from_user.id)
    if message.text == "!telegraph":
        bot.send_document(
            chat_id = message.chat.id,
            data = tgraph,
            caption = tgraph_text,
            reply_to_message_id = message.message_id,
            parse_mode = "HTML"
        )
    elif message.text == "!telegraph2":
        bot.send_document(
            chat_id = message.chat.id,
            data = tgraph2,
            caption = tgraph2_text,
            reply_to_message_id = message.message_id,
            parse_mode = "HTML"
        )
    elif message.text == "!telegraph3":
        bot.send_document(
            chat_id = message.chat.id,
            data = tgraph3,
            caption = tgraph3_text,
            reply_to_message_id = message.message_id,
            parse_mode = "HTML"
        )
    elif message.text == "!telegraph mod":
        bot.send_document(
            chat_id = message.chat.id,
            data = tgraph_mod,
            caption = tgraph_mod_text,
            reply_to_message_id = message.message_id,
            parse_mode = "HTML"
        )
    elif message.text == "!ru":
        bot.send_document(
            chat_id = message.chat.id,
            data = rus,
            caption = rus_text,
            reply_to_message_id = message.message_id,
            parse_mode = "HTML"
        )
    elif "kaunt" in str(message.text).lower():
        for i in [ "o'chir", "ochir", "ocir", "o'cir", "delet", "udalt", "udalit" ]:
            if i in str(message.text).lower():
                bot.send_message(
                    chat_id = message.chat.id,
                    text = del_accaunt,
                    parse_mode = 'html',
                    reply_to_message_id = message.message_id,
                    disable_web_page_preview = True
                )
        for j in [ "yawir", "yasir", "yashir", "korinma", "ko'rinma", "hide", "hidden" ]:
            if j in str(message.text).lower():
                bot.send_message(
                    chat_id = message.chat.id,
                    text = hide_accaunt,
                    parse_mode = 'HTML',
                    reply_to_message_id = message.message_id,
                    disable_web_page_preview = True
                )
    elif "bildirishnoma" in str(message.text).lower():
        bot.send_message(
            chat_id = message.chat.id,
            text = notification,
            reply_to_message_id = message.message_id
        )
    elif "7.7 versiya" in str(message.text).lower():
        bot.send_message(
            chat_id = message.chat.id,
            text = "https://t.me/TGraphUz/865",
            reply_to_message_id = message.message_id
        )
    elif "7.7.1 versiya" in str(message.text).lower():
        bot.send_message(
            chat_id = message.chat.id,
            text = "https://t.me/TGraphUz/900",
            reply_to_message_id = message.message_id
        )
    elif "mod haqida" in str(message.text).lower():
        bot.send_message(
            chat_id = message.chat.id,
            text = "https://t.me/TGraphUz/934",
            reply_to_message_id = message.message_id
        )
    elif message.text == "!?":
        bot.send_message(
            chat_id = message.chat.id,
            text = "Savolingizni to'liq va tushunarli qilib yozing!",
            reply_to_message_id = message.reply_to_message.message_id
        )
    elif user.status in [ 'administrator', 'creator' ]:
        if message.text == "!":
            if message.reply_to_message.from_user.last_name is not None:
                fullname = f'{message.reply_to_message.from_user.first_name} ' \
                           f'{message.reply_to_message.from_user.last_name} '
            else:
                fullname = f'{message.reply_to_message.from_user.first_name}'
            name = f"<a href='tg://user?id={message.reply_to_message.from_user.id}'>{fullname}</a>"
            bot.restrict_chat_member(
                chat_id = message.chat.id,
                user_id = message.reply_to_message.from_user.id,
                until_date = time.time() + 600
            )
            bot.send_message(
                message.chat.id,
                f"{name}\nSiz guruh qoidalarini buzganlikda ayblanib, 10 minutga read-only rejimiga tushurildingiz!",
                reply_to_message_id = message.reply_to_message.message_id,
                parse_mode = "html"
            )
            try:
                bot.delete_message(message.chat.id, message.message_id)
                sleep(30)
                bot.delete_message(message.chat.id, message.reply_to_message.message_id)
            except:
                return

        elif message.text == "!qoida":
            if message.reply_to_message.from_user.last_name is not None:
                fullname = f'{message.reply_to_message.from_user.first_name} ' \
                           f'{message.reply_to_message.from_user.last_name} '
            else:
                fullname = f'{message.reply_to_message.from_user.first_name}'
            name = f"<a href='tg://user?id={message.reply_to_message.from_user.id}'>{fullname}</a>"
            bot.send_message(
                chat_id = message.chat.id,
                text = f"{name}{qoida}",
                reply_to_message_id = message.reply_to_message.message_id,
                parse_mode = "HTML"
            )
        elif message.text == "!ro":
            if message.reply_to_message.from_user.last_name is not None:
                fullname = f'{message.reply_to_message.from_user.first_name} ' \
                           f'{message.reply_to_message.from_user.last_name} '
            else:
                fullname = f'{message.reply_to_message.from_user.first_name}'
            name = f"<a href='tg://user?id={message.reply_to_message.from_user.id}'>{fullname}</a>"
            bot.restrict_chat_member(
                chat_id = message.chat.id,
                user_id = message.reply_to_message.from_user.id,
                until_date = time.time() + 600 * 6
            )
            bot.send_message(
                message.chat.id,
                f"{name}\nSiz guruh qoidalarini buzganlikda ayblanib, 1 soatga read-only rejimiga tushurildingiz!",
                reply_to_message_id = message.reply_to_message.message_id,
                parse_mode = "html"
            )
            try:
                bot.delete_message(message.chat.id, message.message_id)
                sleep(30)
                bot.delete_message(message.chat.id, message.reply_to_message.message_id)
            except:
                return
        elif message.text == "!ban":
            bot.kick_chat_member(
                chat_id = message.chat.id,
                user_id = message.reply_to_message.from_user.id
            )
            bot.delete_message(message.chat.id, message.message_id)

'''
@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == "accept":
        chat = bot.get_chat("@tgraphbottest")
        bot.restrict_chat_member(
            chat_id = chat.id,
            user_id = call.from_user.id,
            can_send_messages = True,
            can_send_other_messages = True,
            can_add_web_page_previews = True,
            can_send_media_messages = True,
            can_invite_users = False
        )
        sql = "SELECT invite_msg FROM user WHERE id = %s"
        val = (call.from_user.id,)
        cursor.execute(sql)

        result = cursor.fetchall()
        print(result)
'''


if __name__ == "__main__":
    bot.polling(
        none_stop = True
    )
