#!/usr/bin/python3

# Print numbers from 0 to 99 with formatting
print(", ".join(f"{i:02d}" for i in range(99)), end=", ")
print(f"{99:02d}")
