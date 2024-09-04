#!/usr/bin/python3

# Print all possible combinations of two digits
for i in range(8):
    print(", ".join(f"{i:d}{j:d}" for j in range(i + 1, 10)), end=", ")

# Last row (89)
print(", ".join(f"{8:d}{j:d}" for j in range(9, 10)))
