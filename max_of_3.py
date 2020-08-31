#!/user/bin/python3

def max(uno, dos, tres):
    if uno > dos and uno > tres:
        print("{} is biggest".format(uno))
    elif dos > uno and dos > tres:
        print("{} is biggest".format(dos))
    elif tres > uno and tres > dos:
        print("{} is biggest".format(tres))

def main():
    one = input("Enter 1st number= ")
    two = input("Enter 2nd number= ")
    three = input("Enter 3rd number= ")
    max(one, two, three)

if __name__ == "__main__":
    main()
