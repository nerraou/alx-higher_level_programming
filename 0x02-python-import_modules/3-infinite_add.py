#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    sum = 0
    if length == 1:
        print("0")
    elif length == 2:
        print("{}".format(sys.argv[1]))
    else:
        for i in range(1, length):
            sum += int(sys.argv[i])
        print(sum)
