#!/usr/bin/python3

# Print all possible combinations of two digits
# First 8 rows (00 to 79)
for i in range(8):
    print(", ".join("{:d}{:d}".format(i, j) for j in range(i + 1, 10)), end=", ")

# Last row (89)
print(", ".join("{:d}{:d}".format(8, j) for j in range(9, 10)))
