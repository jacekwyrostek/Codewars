'''
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.

#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
'''

def get_middle(s):
    s1=list(str(s))
    x=len(s1)
    if x%2 == 0:
        return s1[x/2-1]+s1[x/2]
    else:
        return s1[int(round(x/2))]
