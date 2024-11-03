import requests
from time import sleep

def solscan():
    BASE_URL = "https://api.geckoterminal.com/api/v2/networks/solana/new_pools"
    response = requests.get(BASE_URL)
    data = response.json()
    address = data['data'][0]['attributes']['address']
    name, _ = data['data'][0]['attributes']['name'].split(' / ')

    return address, name


last_address = None

while True:
    address, name = solscan()
    if address != last_address:
        print(f"Новый адрес: {address}, Имя: {name}")
        last_address = address
    else:
        pass
    sleep(2)




