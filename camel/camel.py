def main():
    x = input("Input a camel case string")
    x = camel_to_snake(x)
    print(x)

def camel_to_snake(camel):
    snake = []
    for char in camel:
        if char.isupper():
            snake.append("_")
            snake.append(char.lower())
        else:
            snake.append(char)
    return "".join(snake).lstrip("_")

if __name__ == "__main__":
    main()


