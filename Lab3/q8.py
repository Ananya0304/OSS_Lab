def vending_machine():
    try:
        with open("VendingItems.txt") as f:
            items = {}
            for line in f:
                name, price = line.strip().split('|')
                items[name] = int(price)
    except FileNotFoundError:
        print("VendingItems.txt not found.")
        return

    while True:
        item = input("Enter item name: ")
        if item in items:
            break
        print(f"Available Items are {list(items.keys())}.")
        print("Try Again.")

    while True:
        try:
            money = int(input("Enter money to deposit: "))
            break
        except ValueError as e:
            print(f"Bad Input {e.args[0]}.")
            print("Try Again.")

    price = items[item]
    if money >= price:
        print("Thank you for your purchase. Enjoy")
        if money > price:
            print(f"Do not forget to collect your change, {money - price} Rs.")
    else:
        print(f"Insufficient funds. {item} costs {price} Rs.")
vending_machine()
