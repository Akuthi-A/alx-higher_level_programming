#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv)

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print(f"{length}: {sys.argv[length]}")
    else:
        print(f"{length} arguments:")
        for i in range(1, length):
            print(f"{i}: {sys.argv[i]}")
