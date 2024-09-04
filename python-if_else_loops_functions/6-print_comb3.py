#!/usr/bin/python3

# Print all possible combinations of two digits
for i in range(10):
    for j in range(i + 1, 10):  # Start from i+1 to avoid dups
        print(f"{i:d}{j:d}", end=", " if i < 8 or j < 9 else "\n")
