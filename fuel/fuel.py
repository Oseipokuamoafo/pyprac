def fractoper(n):
    percentage = round(n*100)
    if percentage <= 1:
        print("E")
    elif percentage  >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def main():
    while True:
        fraction = input("fraction")
        try:
            x,y = fraction.split("/")
            x=int(x)
            y=int(y)

            if y == 0:
                print(f"Error: Division by zero is not allowed.")
            elif x > y:
                print(f" x cant be greater than y")
            else:
                f = x/y
                fractoper(f)
                break
        except (ValueError, ZeroDivisionError):
            print("Error: Invalid input. Please enter a fraction in the format 'x/y' and y shouldnt be 0")

if __name__ == "__main__":
    main()

