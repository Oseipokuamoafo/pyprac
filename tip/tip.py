def main():
    dollars = input("How much was the meal? ")
    percent = input("What percentage would you like to tip? ")
    tip = dollars_to_float(dollars) * percent_to_float(percent)
    print(f"Leave ${tip:.2f}\n")


def dollars_to_float(d):
   d= d.replace("$" , "")
   d= float(d)
   return d



def percent_to_float(p):
    p=p.replace("%" , "")
    p= float(p) / 100
    return float(p)


main()
