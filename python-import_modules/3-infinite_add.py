#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Calculate the sum of all arguments (excluding the script name)
    total = sum(int(arg) for arg in sys.argv[1:])

    print("{}".format(total))
