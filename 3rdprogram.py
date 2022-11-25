# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# ﻿Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def characters(string):
    lowercase=0
    uppercase=0
    for i in string:
        if i.islower():
            lowercase +=1
        elif i.isupper():
            uppercase +=1
        else:
            pass
    print("no.of upper case characters:",uppercase)
    print("no.of lower case characters",lowercase)
string=input("enter the string:")
characters(string)
