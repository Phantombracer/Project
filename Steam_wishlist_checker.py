import requests

def load_wishlist():
    with open("wishlist.txt", "r") as file:
        return [int(line.strip()) for line in file]

wishlist = load_wishlist()

def check_game_discount(game_id):

    url = f"https://store.steampowered.com/api/appdetails?appids={game_id}&cc=ua"

    response = requests.get(url)

    data = response.json()

    game_data = data[str(game_id)]["data"]

    name = game_data["name"]

    print(f"Гра: {name}")

    if "price_overview" in game_data:

        price = game_data["price_overview"]["final"] / 100
        initial_price = game_data["price_overview"]["initial"] / 100
        currency = game_data["price_overview"]["currency"]
        discount = game_data["price_overview"]["discount_percent"]

        
        if discount > 0:
            print(f"Стара ціна: {initial_price} {currency}")
            print(f"Нова ціна: {price} {currency}")
            print(f"Знижка: {discount}%")
        else:
            print(f"Ціна: {price} {currency}")
            print("Знижки немає")

    else:
        print("Гра безкоштовна або ціна недоступна")

    print("====================")


for game in wishlist:
    check_game_discount(game)