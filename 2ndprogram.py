# Write a Python program to reverse a string.
# ﻿Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse(str):
    revstr=""
    for i in str:
        revstr=i+revstr
    return revstr
str=input("enter a string:")
print(reverse(str))