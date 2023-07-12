#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a, 10):
        if a == b:
            continue
        if a == 8 and b == 9:
            print(f"{a}{b}")
        else:
            print(f"{a}{b}", end=", ")
