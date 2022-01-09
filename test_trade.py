from binance.client import Client


#bot 0
# api_key = 'wFqCyHdnaygcjy4W4refvi6Jo4qdlLb0OUOIeWjcCUZ5F53s7DM05ShS7Kzv9YM7'
# api_secret = '4gmQwHlieQwQGHuHdsN7KILZWCxQdLXutTaOCjy7wwOi7QddRVebNueaEpeSETIj'

#bot 1
api_key = 'Mm7ai1Sri20YjysrLm5DpzP3AHFIt80edsxzMvtZjrsfstlqqTtzADIlH1Qynmmm'
api_secret = 'Qp6pJKzPmq2LtTpk5rE3xE0y3xQX4UuIA6ira6hMhsyRmslV7eI9GgDscEQ3Hohn'

#bot 2
# api_key = 'zXx32EFAKAIwoVl45DopUqF6TYsTAqN7rzEq78gbc75pWO9mT9Kl4K7L7YVHAzUR'
# api_secret = 'gbwJG2E8zz01eui9orYw3ntTlv1dKf8fSMCGYfqSCiL3gPyuh6hwEi3cVASSFimf'

client = Client(api_key, api_secret)

usdt_balance = 0
for asset in client.futures_account()["assets"]:
    if(asset["asset"]=="USDT"):
        usdt_balance = asset["availableBalance"]
print("usdt_balance: "+usdt_balance)




# LEVERAGE = 10
# SYMBOL = "OCEANUSDT"
# PERCENTAGE = 1

# #testnet
# api_key = "KZexYHU1F0a0tfcw9lpDWqSLnz1T3O9Idr4xUmw20oWG7u8HW9yBszL5ELFf0Z2h"
# api_secret = "HqeRs5Qs4YLFJSW8DXX7i9hPJnDGIcg0DWS0JdCJApalIw9Raz45ToaQGCPh1YY9"


# print(client.futures_coin_create_order("BTCUSDT"))


# ## working fine
# print(client.futures_change_leverage(symbol="BTCUSDT", leverage=5))
# print(client.futures_change_leverage(symbol="BTCUSDT", leverage=20))
# print(client.futures_create_order(symbol="BTCUSDT", side='BUY', type='MARKET', quantity=0.001))

# SYMBOL = "BNBUSDT"
# order_amount=511.2561231
# QUANTITY=0.1
# print(client.futures_create_order(symbol=SYMBOL, side='BUY', type='LIMIT', price=order_amount, timeInForce="GTC", quantity=QUANTITY))

# info = client.futures_exchange_info()
# print(info)

# SYMBOL = "BNBUSDT"
# SYMBOL = "OCEANUSDT"
# SYMBOL = "RUNEUSDT"
# SYMBOL = "FTMUSDT"
# SYMBOL = "MKRUSDT"
# SYMBOL = "BTCUSDT"
# for sym in info["symbols"]:
#     if(sym["symbol"]==SYMBOL):
#         val = sym["filters"][0]
#         print(val)
#         price_precision = int(sym["pricePrecision"])
#         print(price_precision)


# info = client.futures_exchange_info()
# for symbol in info["symbols"]:
#     if (symbol["symbol"] == SYMBOL):
#         quantity_precision = int(symbol["quantityPrecision"])
#         print("quantity_precision: " + str(quantity_precision))
#         price_precision = int(symbol["pricePrecision"])
#         print("price_precision: "+str(price_precision))
#
#         print(symbol["filters"][0])
#
#         tick_size = float(symbol["filters"][0]["tickSize"])
#
#         tick_size = f"{tick_size:.10f}"
#         print("tick_size: "+str(tick_size))
#
#         # rounding_val = str(int(1/tick_size)).count("0")
#
#         rounding_val =tick_size.split(".")[1].find("1")+1
#
#         print("rounding_val: " + str(rounding_val))






# print(client.futures_mark_price(symbol=SYMBOL))
#
# cheapest_price = float(client.futures_mark_price(symbol=SYMBOL)["markPrice"])
# print("cheapest_price: "+str(cheapest_price))

#
# print(client.futures_account_balance())

# print(client.futures_ticker(symbol=SYMBOL))
# print(client.get_ticker(symbol=SYMBOL))

# info = client.futures_exchange_info()
# # print(info)
# for symbol in info["symbols"]:
#     if(symbol["symbol"]==SYMBOL):
#         print(symbol)


# print(client.get_exchange_info(symbol=SYMBOL))





# print(client.futures_create_order(symbol=SYMBOL, side='BUY', type='LIMIT',price=0.82877, timeInForce="GTC", quantity=28.1))



# timeInForce -> immediate-or-cancel (IOC), fill-or-kill (FOK), or good-'til-canceled (GTC).
# print(client.futures_create_order(symbol=SYMBOL, side='BUY', type='LIMIT',price=round(cheapest_price, 5), timeInForce="GTC", quantity=30))

# print(client.futures_create_order(symbol=SYMBOL, side='BUY', type='MARKET', quantity=30))

#to cancel after reach target 1
# print(client.futures_cancel_all_open_orders(symbol=SYMBOL))

# print(client.futures_get_open_orders())

# print(client.futures_get_all_orders(symbol=SYMBOL))


# take profit market
# print(client.futures_create_order(symbol=SYMBOL, side='SELL', type='TAKE_PROFIT_MARKET',stopPrice=1.0, closePosition=True))
# stop market
# print(client.futures_create_order(symbol=SYMBOL, side='SELL', type='STOP_MARKET',stopPrice=0.5, closePosition=True))


# print(client.futures_position_information(symbol="MATICUSDT"))


# print(client.futures_get_order(symbol='BTCUSDT'))
# print(client.futures_get_all_orders())
# print(client.futures_account())
# print(client.futures_cancel_orders(symbol="OCEANUSDT"))
# print(client.futures_coin_account_balance())
# print(client.futures_coin_get_all_orders())
# print(client.futures_account_balance())



# print(client.futures_coin_get_open_orders())

# print(client.futures_coin_get_all_orders(symbol="BTCUSDT"))

# print(client.futures_cancel_orders(symbol="BTCUSDT"))



# client.API_URL = 'https://testnet.binance.vision/api'

# # get balances for all assets & some account information
# print(client.get_account())

# # get balance for a specific asset only (BTC)
# print(client.get_asset_balance(asset='USDT'))

# # get balances for futures account
# print(client.get_margin_account())

# get balances for futures account
# print("-----")


# print(client.futures_get_open_orders())
# print(client.futures_account_balance())


# print(client.futures_get_all_orders())
# print(client.futures_coin_create_order())