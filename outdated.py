import sys

def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        x = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ")
        x = x.strip()
        try:
            if any(month in x for month in months):
                d, y = x.split(",")
                mon, d = d.split(" ")
                mon = str(mon)
                m = months.index(mon) + 1
                y = int(y)
                if 1 <= m <= 12 and 1 <= int(d) <= 31:
                    sys.stdout.write(f"{y:04}-{m:02}-{int(d):02}\n")
                else:
                    print("Invalid input format. Please try again.")
            elif "/" in x:
                m, d, y = x.split("/")
                m = int(m)
                d = int(d)
                y = int(y)
                if 1 <= m <= 12 and 1 <= d <= 31:
                   sys.stdout.write(f"{y:04}-{m:02}-{d:02}\n")
                else:
                    print("Invalid input format. Please try again.")
            else:
                print("Invalid input format. Please try again.")
        except ValueError:
            print("Invalid input format. Please try again.")

if __name__ == "__main__":
    main()
