def interpreter():
    i = input("expression")
    x,y,z = i.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        results= x + z
    elif y == "-":
        results = x-z
    elif y == "*":
        results=x*z
    elif y == "/":
            results=(x)/(z)

    print(results)





interpreter()

