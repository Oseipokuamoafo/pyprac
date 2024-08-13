import sys

def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total_cost = 0

    while True:
        try:
            item = input("Item: ").title()
            if item in menu.keys():
                x = menu.get(item)
                total_cost += x
                print(f"Total: ${total_cost:.2f}")
            else:
                print("Sorry, we don't have that item.")
        except EOFError:
            print()
            sys.exit(0)

if __name__ == "__main__":
    main()
