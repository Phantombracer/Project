import requests

def load_wishlist():
    wishlist = []
    with open("wishlist.txt", "r") as file:
        for line in file:
            game_id, desired_price = line.strip().split(",")
            wishlist.append((int(game_id), float(desired_price)))
    return wishlist

wishlist = load_wishlist()

def check_game_discount(game_id, desired_price):

    url = f"https://store.steampowered.com/api/appdetails?appids={game_id}&cc=ua"

    response = requests.get(url)

    data = response.json()

    game_info = data.get(str(game_id))

    if not game_info or not game_info.get("success"):
        print("Помилка отримання даних")
        return

    game_data = game_info["data"]

    name = game_data["name"]

    print(f"Гра: {name}")

    if "price_overview" in game_data:

        price = game_data["price_overview"]["final"] / 100
        initial_price = game_data["price_overview"]["initial"] / 100
        currency = game_data["price_overview"]["currency"]
        discount = game_data["price_overview"]["discount_percent"]

        if price <= desired_price:
            print("Ціна нижче бажаної!")

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


for app_id, desired_price in wishlist:
    check_game_discount(app_id, desired_price)