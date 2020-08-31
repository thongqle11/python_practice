#!/usr/bin/python3

def checkprime(number):
    if number < 2:
        print("Not Prime")
        exit()
    for x in range(2,number):
        if number%x == 0:
            print(number, "is Not Prime")
            print(x, "times", number//x, "is equal to", number)
            break
    else:
        print(number, "is Prime")
def main():
    num=int(input("Enter number to check prime: "))
    checkprime(num)

if __name__ == "__main__":
    main()
