def main():
    due = 50

    while due > 0:
        x = int(input("Insert coin: "))
        if x in [25, 10, 5]:
            due -= x
            if due > 0:
                print(f"Amount Due: {due}")
        else:
            print(f"Amount Due: {due}")


    print(f"Change Owed: {abs(due)}")




if __name__ == "__main__":
    main()








