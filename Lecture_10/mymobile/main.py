from mobile_phone import MyMobile


def menu():
    """Menu."""
    print("\nMenu:")
    print("1 - Turn on mobile")
    print("2 - Turn off mobile")
    print("3 - Call")
    print("-1 - Exit")


def main():
    my_phone = MyMobile("8-800-555-35-35")
    while True:
        menu()
        choice = input("Make your choise: ")
        if choice == "1":
            print(my_phone.turn_on())
        elif choice == "2":
            print(my_phone.turn_off())
        elif choice == "3":
            print(my_phone.call("8-800-555-35-35"))
        elif choice == "-1":
            print("Exiting the app")
            break
        else:
            print("Incorrect input")


if __name__ == "__main__":
    main()
