def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    if not sw2l(s):
        return False
    if not maxnminlength(s):
        return False
    if not validnum(s):
        return False
    if not has_no_punctuation(s):
        return False
    return True




def sw2l(plate):
    return len(plate) >= 2 and plate[0].isalpha() and plate[1].isalpha()
def maxnminlength(plate):
    return 6 >= len(plate) >= 2
def validnum(plate):
    firstdig = True
    for i,char in enumerate(plate):
        if char.isdigit():
            if firstdig and char =="0":
                return False
            firstdig = False
            if i < len(plate)-1 and not plate[i +1].isdigit():
                return False
    return True
def has_no_punctuation(plate):
    return plate.isalnum()


if __name__ == "__main__":
    main()







