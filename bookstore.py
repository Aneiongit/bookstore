import csv


def exiting():
    print("Exiting... Bye!")
    exit()


def add_item(new_item):
    global items
    items.append(new_item)
    return items


def sell_item(item):
    global items
    for item in items:
        if name == item[0]:
            item[1] = item[1] - quantity
        elif name != item[0]:
            continue
        else:
            print("We do not have this stock, please try again.")


def get_income():
    income = sum(item[1]*item[3] for item in sold_items)
    return income


def get_cost():
    cost = sum(item[1]*item[3] for item in items)
    return cost


def get_items():
    print(f"{'Name': <31} {'Quantity': <10} {'Unit': <8} {'Unit price (PLN)': <8}")
    for item in items:
        print(f"{(item[0]):<30}  {item[1]:<10} {item[2]:<8} {item[3]:<8}")


def get_sold_items():
    print(f"{'Name': <31} {'Quantity': <10} {'Unit': <8} {'Unit price (PLN)': <8}")
    for item in sold_items:
        print(f"{(item[0]):<30}  {item[1]:<10} {item[2]:<8} {item[3]:<8}")


def get_revenue():
    cos = get_cost()
    inc = get_income()
    revenue = float(inc) - float(cos)
    return revenue


def export_items_to_csv():
    with open("books.csv", "w", newline="") as warehouse:
        writer = csv.writer(warehouse)
        writer.writerows(items)


def export_sales_to_csv():
    with open("sales.csv", "w", newline="") as warehouse:
        writer = csv.writer(warehouse)
        writer.writerows(sold_items)


items = []

sold_items = []

if __name__ == "__main__":
    with open('books.csv', newline='') as f:
        reader = csv.reader(f)
        items = list(reader)
        for item in items:
            item[0] = str(item[0])
            item[1] = int(item[1])
            item[2] = str(item[2])
            item[3] = float(item[3])

    with open('sales.csv', newline='') as f:
        reader = csv.reader(f)
        sold_items = list(reader)
        for item in items:
            item[0] = str(item[0])
            item[1] = int(item[1])
            item[2] = str(item[2])
            item[3] = float(item[3])

    print("Bookstore Management System")
    print("Exit - exit the program.")
    print("Save - saving progress.")
    print("Show - display stock.")
    print("Add - add an item.")
    print("Sell - deduct an item.")
    print("Revenue - show profit.")

    while True:
        choice = input("Choose one from the options: ")
        choice = choice.lower()

        if choice == "exit":
            print("Exiting... bye!")
            break
        elif choice == "save":
            export_items_to_csv()
            export_sales_to_csv()
            continue
        elif choice == "show":
            print(get_items())
            continue
        elif choice == "add":
            name = str(input("To add an item please provide name: "))
            quantity = int(input("Please provide quantity: "))
            unit = str(input("Please provide unit (i.e: kg, l, pcs): "))
            unit_price = float(input("Please provide price per unit in PLN: "))
            new_item = [name, quantity, unit, unit_price]
            add_item(new_item)
            continue
        elif choice == "sell":
            name = str(input("To sell an item please provide name: "))
            quantity = int(input("Please provide quantity: "))
            for item in items:
                if name == item[0]:
                    unit = item[2]
                    unit_price = item[3]
                    sold_item = [name, int(quantity), unit, float(unit_price)]
                elif name != item[0]:
                    continue
            sell_item(sold_item)
            sold_items.append(sold_item)
            print(f"You have sold: {sold_item}.")
            continue
        elif choice == "revenue":
            print(f"Income: {get_income():.2f}")
            print(f"Cost: {get_cost():.2f}")
            print(f"Revenue: {get_revenue():.2f}")
        else:
            print("Wrong option!")
            continue


