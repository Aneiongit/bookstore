def exiting():
    print("Exiting... Bye!")
    exit()


def get_items():
    print(f"{'Name': <31} {'Quantity': <10} {'Unit': <8} {'Unit price (PLN)': <8}")
    for item in items:
        print(f"{(item[0]):<30}  {item[1]:<10} {item[2]:<8} {item[3]:<8}")


if __name__ == "__main__":
    print("Bookstore Management System")
    print("Exit - exit the program.")
    print("Show - display stock.")

    choice = input("Choose one from the options: ")
    choice = choice.lower()

    items = [["The tower", 50, "pcs", 44.99],
             ["Ania z zielonego wzgorza", 20, "pcs", 32.99],
             ["Animal Farm", 10, "pcs", 15.99]]

    if choice == "exit":
        print("Exiting... bye!")
    elif choice == "show":
        print(get_items())
    else:
        print("Wrong option, exiting... bye!")
