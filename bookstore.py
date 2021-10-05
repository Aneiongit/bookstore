def exiting():
    print("Exiting... Bye!")
    exit()


def add_item(item):
    global items
    items.append(item)
    return items


def get_items():
    print(f"{'Name': <31} {'Quantity': <10} {'Unit': <8} {'Unit price (PLN)': <8}")
    for item in items:
        print(f"{(item[0]):<30}  {item[1]:<10} {item[2]:<8} {item[3]:<8}")


if __name__ == "__main__":
    print("Bookstore Management System")
    print("Exit - exit the program.")
    print("Show - display stock.")
    print("Add - add an item.")

    while True:
        choice = input("Choose one from the options: ")
        choice = choice.lower()

        items = [["The Tower", 50, "pcs", 44.99],
                 ["The Witcher", 20, "pcs", 32.99],
                 ["Animal Farm", 10, "pcs", 15.99]]

        if choice == "exit":
            print("Exiting... bye!")
            break
        elif choice == "show":
            print(get_items())
            continue
        elif choice == "add":
            name = str(input("To add an item please provide name: "))
            quantity = int(input("Please provide quantity: "))
            unit = str(input("Please provide unit (i.e: kg, l, pcs): "))
            unit_price = float(input("Please provide price per unit in PLN: "))
            new_item = [name, quantity, unit, unit_price]
            global item
            add_item(new_item)
            print(items)
            print(f"{'Name': <31} {'Quantity': <10} {'Unit': <8} {'Unit price (PLN)': <8}")
            for item in items:
                print(f"{(item[0]):<30}  {item[1]:<10} {item[2]:<8} {item[3]:<8}")
            continue
        else:
            print("Wrong option!")
            continue

# "Dragon Age", 25, "pcs", 54.99
