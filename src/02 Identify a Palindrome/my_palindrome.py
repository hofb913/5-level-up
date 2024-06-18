import re

def is_palindrome(s):
    s1 = re.sub(r'[^A-Z]', '', s.upper()) 
    s2 = s1[::-1]
    return (s1 == s2)

str = "Go hang a salami, I'm a lasagna hog."
print(f'{is_palindrome(str)}')