import re
def to_camel_case(text):
    if '-'or'_' in text:
        text=re.split('-|_',text)
        if text[0].islower():
            for i in range(1,len(text)):
                text[i]=text[i].capitalize()
        else:
            for i in range(0,len(text)):
                text[i]=text[i].capitalize()
    text=''.join(text)
    return text
