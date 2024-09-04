#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1  # Exclude the script name itself

    # Print the number of arguments and the correct singular/plural form
    print(f"{argc} argument{'s' if argc != 1 else ''}{':' if argc > 0 else '.'}")

    # Print each argument if there are any
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
