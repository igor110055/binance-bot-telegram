import telebot # pip install pyTelegramBotAPI
from binance.client import Client # pip install python-binance
import time
from threading import Thread

#bot0
binance_api_key = 'wFqCyHdnaygcjy4W4refvi6Jo4qdlLb0OUOIeWjcCUZ5F53s7DM05ShS7Kzv9YM7'
binance_api_secret = '4gmQwHlieQwQGHuHdsN7KILZWCxQdLXutTaOCjy7wwOi7QddRVebNueaEpeSETIj'
telegram_api_key = "5047585678:AAFkIdh39y4Sya8IylYExlEfzLM2WChj1sg"

#bot1
# binance_api_key = 'Mm7ai1Sri20YjysrLm5DpzP3AHFIt80edsxzMvtZjrsfstlqqTtzADIlH1Qynmmm'
# binance_api_secret = 'Qp6pJKzPmq2LtTpk5rE3xE0y3xQX4UuIA6ira6hMhsyRmslV7eI9GgDscEQ3Hohn'
# telegram_api_key = "5065993300:AAFzp5-c4-TaD0MVYnNYsdP59BjO-Yqo5KY"

#bot2
# binance_api_key = 'zXx32EFAKAIwoVl45DopUqF6TYsTAqN7rzEq78gbc75pWO9mT9Kl4K7L7YVHAzUR'
# binance_api_secret = 'gbwJG2E8zz01eui9orYw3ntTlv1dKf8fSMCGYfqSCiL3gPyuh6hwEi3cVASSFimf'
# telegram_api_key = "5041025310:AAHtDa9p8EfAYUfoqmfmQsaZH5BUsrzJGts"

client = Client(binance_api_key, binance_api_secret)

bot =telebot.TeleBot(telegram_api_key)
PERCENTAGE = 1
LEVERAGE = 10
TAKE_PROFIT = "t1"

@bot.message_handler(commands=["check-take-profit"])
def check_take_profit(message):
    print(TAKE_PROFIT)
    bot.reply_to(message, str(TAKE_PROFIT))

@bot.message_handler(commands=["set-take-profit"])
def set_take_profit(message):
    try:
        print(message.text)
        global TAKE_PROFIT
        val = message.text.split(" ")[1].strip().lower()
        if(val=="t1" or "%" in val):
            TAKE_PROFIT = val
            bot.reply_to(message, "TAKE_PROFIT value change to: " + str(TAKE_PROFIT))
        else:
            error_msg = "take profit value should be in these formats, ex: t1, 2%, 3.5%"
            print(error_msg)
            bot.reply_to(message, error_msg)

    except Exception as e:
        print("Wrong format -> " + str(e))
        bot.reply_to(message, "Wrong format -> " + str(e))

def check_for_target(thread_data):
    try:
        symb = thread_data[0]
        target = thread_data[1]
        stoploss = thread_data[2]
        msg = thread_data[3]
        while(True):
            price_now = float(client.futures_mark_price(symbol=symb)["markPrice"])
            print("price_now for "+symb+": " + str(price_now))
            if(price_now>target):
                bot.reply_to(msg, "price reached target")
                print("price reached target for "+symb)
                try:
                    print(client.futures_cancel_all_open_orders(symbol=symb))
                except Exception as e:
                    error_msg = "issue in cancel all orders after reaching target 1 -> " + str(e)
                    print(error_msg)
                    bot.reply_to(msg, error_msg)
                break
            elif (price_now < stoploss):
                bot.reply_to(msg, "price reached stoploss")
                print("price reached stoploss for " + symb)
                break
            else:
                print("target/stoploss not achieved yet")
            time.sleep(5)
        print("thread completed for: "+symb)
    except Exception as e:
        error_msg = "issue in thread for "+symb +" -> " + str(e)
        print(error_msg)
        bot.reply_to(msg, error_msg)

@bot.message_handler(commands=["test"])
def test(message):
    print("testing ..")
    bot.reply_to(message, "bot working fine !")\

@bot.message_handler(commands=["balance"])
def balance(message):
    try:
        for asset in client.futures_account()["assets"]:
            if (asset["asset"] == "USDT"):
                usdt_balance = float(asset["availableBalance"])

        print("usdt_balance: " + str(usdt_balance))
        bot.reply_to(message, "usdt_balance: " + str(usdt_balance))
    except Exception as e:
        print("error in balance -> " + str(e))
        bot.reply_to(message, "error in balance -> " + str(e))

# @bot.message_handler(commands=["start-bot"])
# def start_check(message):
#     global message_chat_id
#     message_chat_id = message.chat.id
#     print(message_chat_id)
#     bot.send_message(message.chat.id, "Bot started")

@bot.message_handler(commands=["get-percentage"])
def get_percentage(message):
    print(PERCENTAGE)
    bot.reply_to(message, str(PERCENTAGE))

@bot.message_handler(commands=["set-percentage"])
def set_percentage(message):
    try:
        print(message.text)
        global PERCENTAGE
        PERCENTAGE = int(message.text.split(" ")[1].strip())
        print("PERCENTAGE:"+str(PERCENTAGE))
        bot.reply_to(message, "PERCENTAGE change to: "+str(PERCENTAGE))

    except Exception as e:
        print("Wrong format -> " + str(e))
        bot.reply_to(message, "Wrong format -> " + str(e))

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
        if(msg_content[0][0].lower() =="coin"):
            msg_coin=msg_content[0][1]
        msg_entry_min = ""
        msg_entry_max = ""
        if (msg_content[1][0].lower() == "buying"):
            msg_entry_min = min(float(msg_content[1][1].split("-")[0].strip()), float(msg_content[1][1].split("-")[1].strip()))
            msg_entry_max = max(float(msg_content[1][1].split("-")[0].strip()), float(msg_content[1][1].split("-")[1].strip()))
        msg_target = ""
        if (msg_content[2][0].lower() == "t1"):
            msg_target = float(msg_content[2][1])
        msg_stoploss = ""
        if (msg_content[3][0].lower() == "stoploss"):
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

    except Exception as e:
        print("This message is not in correct format -> " + str(e))
        bot.reply_to(message, "This message is not in correct format -> " + str(e))
        return

    try:
        SYMBOL = msg_coin.upper()+"USDT"
        print("SYMBOL: "+SYMBOL)
        cheapest_price = float(client.futures_mark_price(symbol=SYMBOL)["markPrice"])
        print("cheapest_price: " + str(cheapest_price))

        usdt_balance = 0
        for asset in client.futures_account()["assets"]:
            if (asset["asset"] == "USDT"):
                usdt_balance = float(asset["availableBalance"])

        print("usdt_balance: " + str(usdt_balance))

        info = client.futures_exchange_info()
        for symbol in info["symbols"]:
            if (symbol["symbol"] == SYMBOL):
                quantity_precision = int(symbol["quantityPrecision"])
                print("quantity_precision: " + str(quantity_precision))
                price_precision = int(symbol["pricePrecision"])
                print("price_precision: " + str(price_precision))
                print(symbol["filters"][0])
                tick_size = float(symbol["filters"][0]["tickSize"])
                tick_size = f"{tick_size:.10f}"
                print("tick_size: " + str(tick_size))
                rounding_val = tick_size.split(".")[1].find("1") + 1
                print("rounding_val: " + str(rounding_val))

        QUANTITY = round((usdt_balance*(PERCENTAGE/100))/cheapest_price,quantity_precision)
        print("buying QUANTITY for this coin: " + str(QUANTITY))


        # changing laverage
        try:
            print(client.futures_change_leverage(symbol=SYMBOL, leverage=LEVERAGE))
        except Exception as e:
            error_msg = "Error changing the leverage"
            print(error_msg)
            bot.reply_to(message, error_msg)
            return

        # creating 8 orders
        reduce_val = (cheapest_price-msg_entry_min)/16

        placed_orders = 0
        for i in range(0,16):
            order_amount = round(cheapest_price - i*reduce_val,rounding_val)
            print(order_amount)
            try:
                print(client.futures_create_order(symbol=SYMBOL, side='BUY', type='LIMIT', price=order_amount, timeInForce="GTC", quantity=QUANTITY))
                placed_orders +=1
            except Exception as e:
                error_msg = "Error placing order. order_amount: "+str(order_amount)+" , quantity: "+str(QUANTITY)+" -> "+str(e)
                print(error_msg)
                bot.reply_to(message, error_msg)

        print(str(placed_orders) + " orders placed successfully")
        bot.reply_to(message, str(placed_orders) + " orders placed successfully")

        # creating take profit order
        try:
            global TAKE_PROFIT
            if(TAKE_PROFIT=="t1"):
                stop_price = msg_target
            else:
                stop_price = round(((float(TAKE_PROFIT[:-1])/100)+1)*cheapest_price,rounding_val)
            print("stop_price: "+str(stop_price))
            print(client.futures_create_order(symbol=SYMBOL, side='SELL', type='TAKE_PROFIT_MARKET', stopPrice=stop_price, closePosition=True))
            bot.reply_to(message, "Created take profit order at: "+str(stop_price))

        except Exception as e:
            error_msg = "issue in creating order for take profit -> " + str(e)
            print(error_msg)
            bot.reply_to(message, error_msg)

        # creating order for stoploss
        try:
            print(client.futures_create_order(symbol=SYMBOL, side='SELL', type='STOP_MARKET', stopPrice=msg_stoploss,closePosition=True))
            bot.reply_to(message, "Created stoploss order at: " + str(msg_stoploss))
        except Exception as e:
            error_msg = "issue in creating order for stoploss -> " + str(e)
            print(error_msg)
            bot.reply_to(message, error_msg)

        # target checking thread
        t = Thread(target=check_for_target, args=([SYMBOL,stop_price,msg_stoploss,message],), )
        t.start()

    except Exception as e:
        print("Issue in order placement -> " + str(e))
        bot.reply_to(message, "Issue in order placement -> " + str(e))
        return


bot.polling()