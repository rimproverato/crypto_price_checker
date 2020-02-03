# imports
import tkinter

# calculate market cap

# calculate price 

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
bitcoin_marketcap = tkinter.Button(text = " Marketcap", font = ("times", 15))
bitcoin_marketcap.grid(row = 1, column = 1)

# bitcoin price
bitcoin_price = tkinter.Button(text = " Price", font = ("times", 15))
bitcoin_price.grid(row = 1, column = 2)

# ethereum
bitcoin = tkinter.Label(text = "  Ethereum", font = ("times", 15))
bitcoin.grid(row = 2, column = 0)

# ethereum marketcap
bitcoin_marketcap = tkinter.Button(text = " Marketcap", font = ("times", 15))
bitcoin_marketcap.grid(row = 2, column = 1)

# ethereum price
ethereum_price = tkinter.Button(text = " Price", font = ("times", 15))
ethereum_price.grid(row = 2, column = 2)

# monero
bitcoin = tkinter.Label(text = "Monero", font = ("times", 15))
bitcoin.grid(row = 3, column = 0)

# ethereum marketcap
monero_marketcap = tkinter.Button(text = " Marketcap", font = ("times", 15))
monero_marketcap.grid(row = 3, column = 1)

# ethereum price
monero_price = tkinter.Button(text = " Price", font = ("times", 15))
monero_price.grid(row = 3, column = 2)

# main window event loop
main_window.mainloop()