# imports
import tkinter
import requests

coin_marketcap_api = "https://api.coinmarketcap.com/v1/ticker/"
# calculate market cap
def check_marketcap(coin_name):
    web_response  = requests.get(coin_marketcap_api + coin_name) 
    web_response_json = web_response.json()
    return(web_response_json[0]["market_cap_usd"])

# calculate price 
def check_price(coin_name):
    web_response  = requests.get(coin_marketcap_api + coin_name) 
    web_response_json = web_response.json()
    return(web_response_json[0]["price_usd"])

# initialize tkinter
main_window = tkinter.Tk()

# main window title
main_window.title("Favorite Crypto Price Checker")

# make the screen size
main_window.geometry("500x800")


# coin name
coin_name  = tkinter.Label(main_window, text = "Coin name", font  = ("time", 16), pady = 20, padx = 40)
coin_name.grid(row = 0, column = 0)
# coin market cap
coin_name  = tkinter.Label(main_window, text = "Marketcap", font  = ("time", 16), pady = 20, padx = 40)
coin_name.grid(row = 0, column = 1)
# coin price 
coin_name  = tkinter.Label(main_window, text = "Price", font  = ("time", 16), pady = 20, padx  = 40)
coin_name.grid(row = 0, column = 2)

# number one
number_one  = tkinter.Label(text = "1. ", font = ("times", 15), pady  = 20)
number_one.grid(row = 1, column = 0, sticky = tkinter.W)
# number two
number_two  = tkinter.Label(text = "2. ", font = ("times", 15), pady = 20)
number_two.grid(row = 2, column = 0, sticky = tkinter.W)
# number three 
number_three  = tkinter.Label(text = "3. ", font = ("times", 15), pady = 20)
number_three.grid(row = 3, column = 0, sticky = tkinter.W)

# bitcoin
bitcoin = tkinter.Label(text = " Bitcoin", font = ("times", 15))
bitcoin.grid(row = 1, column = 0)

# bitcoin marketcap
bitcoin_marketcap = tkinter.Button(text = check_marketcap("bitcoin"), font = ("times", 15))
bitcoin_marketcap.grid(row = 1, column = 1)

# bitcoin price
bitcoin_price = tkinter.Button(text = f"USD {check_price('bitcoin')}", font = ("times", 15))
bitcoin_price.grid(row = 1, column = 2)

# ethereum
bitcoin = tkinter.Label(text = "  Ethereum", font = ("times", 15))
bitcoin.grid(row = 2, column = 0)

# ethereum marketcap
ethereum_marketcap = tkinter.Button(text = check_marketcap("ethereum"), font = ("times", 15))
ethereum_marketcap.grid(row = 2, column = 1)

# ethereum price
ethereum_price = tkinter.Button(text = f"USD {check_price('ethereum')}", font = ("times", 15))
ethereum_price.grid(row = 2, column = 2)

# monero
bitcoin = tkinter.Label(text = "Monero", font = ("times", 15))
bitcoin.grid(row = 3, column = 0)

# monero marketcap
monero_marketcap = tkinter.Button(text = f"USD {check_marketcap('monero')}", font = ("times", 15))
monero_marketcap.grid(row = 3, column = 1)

# monero price
monero_price = tkinter.Button(text = check_price("monero"), font = ("times", 15))
monero_price.grid(row = 3, column = 2)

# main window event loop
main_window.mainloop()