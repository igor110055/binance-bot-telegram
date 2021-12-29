import telebot # pip install pyTelegramBotAPI
from binance.client import Client # pip install python-binance

binance_api_key = 'wFqCyHdnaygcjy4W4refvi6Jo4qdlLb0OUOIeWjcCUZ5F53s7DM05ShS7Kzv9YM7'
binance_api_secret = '4gmQwHlieQwQGHuHdsN7KILZWCxQdLXutTaOCjy7wwOi7QddRVebNueaEpeSETIj'
telegram_api_key = "5047585678:AAFkIdh39y4Sya8IylYExlEfzLM2WChj1sg"

client = Client(binance_api_key, binance_api_secret)

bot =telebot.TeleBot(telegram_api_key)
message_chat_id = ""
PERCENTAGE = 1
LEVERAGE = 10


@bot.message_handler(commands=["test"])
def test(message):
    print("testing ..")
    print(message_chat_id)
    bot.reply_to(message, "bot working fine !")

@bot.message_handler(commands=["start-bot"])
def start_check(message):
    global message_chat_id
    message_chat_id = message.chat.id
    print(message_chat_id)
    bot.send_message(message.chat.id, "Bot started")

@bot.message_handler(commands=["get-percentage"])
def test(message):
    print(PERCENTAGE)
    bot.reply_to(message, str(PERCENTAGE))

@bot.message_handler(commands=["set-percentage"])
def book(message):
    try:
        print(message.text)
        global PERCENTAGE
        PERCENTAGE = int(message.text.split(" ")[1].strip())
        print("PERCENTAGE:"+str(PERCENTAGE))
        bot.reply_to(message, "PERCENTAGE change to: "+str(PERCENTAGE))
    except:
        print("Wrong format")
        bot.reply_to(message, "Wrong format")

@bot.message_handler(regexp="coin:")
def handle_message(message):
    msg = message.text
    print("Raw message ->")
    print(msg)

    try:
        msg_content =[]
        for row in msg.split("\n"):
            key = row.split(":")[0].strip()
            value = row.split(":")[1].strip()
            msg_content.append([key,value])
        msg_coin = ""
        if(msg_content[0][0]=="coin"):
            msg_coin=msg_content[0][1]
        msg_entry_min = ""
        msg_entry_max = ""
        if (msg_content[1][0] == "buying"):
            msg_entry_min = min(float(msg_content[1][1].split("-")[0].strip()), float(msg_content[1][1].split("-")[1].strip()))
            msg_entry_max = max(float(msg_content[1][1].split("-")[0].strip()), float(msg_content[1][1].split("-")[1].strip()))
        msg_target = ""
        if (msg_content[2][0] == "T1"):
            msg_target = float(msg_content[2][1])
        msg_stoploss = ""
        if (msg_content[3][0] == "stoploss"):
            msg_stoploss = float(msg_content[3][1])

        print("Data get from the message ->")
        print("msg_coin:" + str(msg_coin))
        print("msg_entry_min:" + str(msg_entry_min))
        print("msg_entry_max:" + str(msg_entry_max))
        print("msg_target:" + str(msg_target))
        print("msg_stoploss:" + str(msg_stoploss))

        if(msg_coin!="" and msg_entry_min!="" and msg_entry_max!="" and msg_target!="" and msg_stoploss!=""):
            print("Get all data needed, continuing the create order process")
            bot.reply_to(message, "Get all data needed, continuing the create order process")
        else:
            print("Message not provided all data")
            bot.reply_to(message, "Message not provided all data")

    except:
        print("This message is not in correct format")
        bot.reply_to(message, "This message is not in correct format")
        return

    SYMBOL = msg_coin.upper()+"USDT"
    print("SYMBOL: "+SYMBOL)
    cheapest_price = float(client.futures_mark_price(symbol=SYMBOL)["markPrice"])
    print("cheapest_price: " + str(cheapest_price))

    # creating 8 orders
    reduce_val = (cheapest_price-msg_entry_min)/msg_entry_max

    for i in range(0,8):
        order_amount = cheapest_price - i*reduce_val
        print(order_amount)
        # if(order_amount>0)




bot.polling()