#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a, 10):
        if a == b:
            continue
        print(f"{a}{b}", end="")
        if a == 8 and b == 9:
            print()
        else:
            print(", ", end="")
