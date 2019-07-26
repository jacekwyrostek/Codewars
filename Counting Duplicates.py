'''
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
that occur more than once in the input string. The input string can be assumed to contain only alphabets 
(both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
'''
import string
def duplicate_count(text):
    text=text.lower()
    x=0
    for i in string.printable:
        if text.count(i) >= 2:
            x+=1
        else:
            continue
    return x
