from binance.client import Client


#keys for oraginal account
# api_key = 'yZhdQLPZCcr13m8zBadCv6tK9EsAJiLF9u9hzOMhAnEBDYasKDYxXzxbFHFtStjp'
# api_secret = 'Pdbl4mwl7xZhZr95QEzihNevg1J5USRlWuHVnwb6To2h1soEgNXrJ8TFteM45KEP'

api_key = 'wFqCyHdnaygcjy4W4refvi6Jo4qdlLb0OUOIeWjcCUZ5F53s7DM05ShS7Kzv9YM7'
api_secret = '4gmQwHlieQwQGHuHdsN7KILZWCxQdLXutTaOCjy7wwOi7QddRVebNueaEpeSETIj'


# #testnet
# api_key = "KZexYHU1F0a0tfcw9lpDWqSLnz1T3O9Idr4xUmw20oWG7u8HW9yBszL5ELFf0Z2h"
# api_secret = "HqeRs5Qs4YLFJSW8DXX7i9hPJnDGIcg0DWS0JdCJApalIw9Raz45ToaQGCPh1YY9"



client = Client(api_key, api_secret)

# print(client.futures_coin_create_order("BTCUSDT"))

print(client.futures_change_leverage(symbol="BTCUSDT", leverage=5))
print(client.futures_change_leverage(symbol="BTCUSDT", leverage=2))
print(client.futures_create_order(symbol="BTCUSDT", side='BUY', type='MARKET', quantity=15))


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