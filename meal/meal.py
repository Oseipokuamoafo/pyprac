def main():
    x=input("What time is it?")
    time=convert(x)
    if 7 <= time<= 8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")
    else:
        return None







    


def convert(time):
    h,m = time.split(":")
    h=float(h)
    m=float(m)
    time = h + (m/60)
    return time



    ...


if __name__ == "__main__":
    main()
