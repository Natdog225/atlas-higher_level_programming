#!/usr/bin/python3

# Print numbers from 0 to 99 with formatting
print(", ".join("{:02d}".format(i) for i in range(99)), end=", ")
print("{:02d}".format(99))
