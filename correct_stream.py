#!/usr/bin/python3
def correct_stream(user, correct):
    list = []
    for i in range(0,len(user)):
        if user[i] == correct[i]:
            list.append(1)
        else:
            list.append(-1)
    return list
def main():
    print(correct_stream(
        ["it", "is", "find"],
        ["it", "is", "fine"]
    )) #➞ [1, 1, -1]

    print(correct_stream(
        ["april", "showrs", "bring", "may", "flowers"],
        ["april", "showers", "bring", "may", "flowers"]
    )) #➞ [1, -1, 1, 1, 1]
if __name__ == "__main__":
    main()
