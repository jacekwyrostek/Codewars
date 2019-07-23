import string

def is_pangram(s):
    verification=True
    for letter in list(string.ascii_lowercase):
        letterCheck=s.lower().count(letter)
        if letterCheck==0:
            verification=False
            break
    return verification
