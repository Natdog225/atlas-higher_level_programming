#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\language that combines remarkable power with very clear syntax"
word1 = str.split(", ")[2].split()[0] # Extract "object-oriented"
word2 = str.split()[0] # Extract "Python"
print(f"{word1} programming with {word2}")
