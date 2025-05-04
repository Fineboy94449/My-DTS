import requests

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = data.get(coin, {}).get("usd")
        if price:
            print(f"Current {coin.upper()} price: ${price}")
        else:
            print(f"Could not find price for '{coin}'.")
    else:
        print("Failed to fetch data from CoinGecko.")

coin = input("Enter a cryptocurrency (e.g. bitcoin, ethereum): ").lower()
get_price(coin)

