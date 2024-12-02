# Program that fixed the 'broken_mod' module
# Name: Natasha Mazibuko
# Date: 31 August 2024

import string

def palindrome (s):
   if len(s) == 1:
      return s.isalpha()
   elif len(s) == 0:  # added!!!!!
      return True
   elif s[0] in string.punctuation or s[0] in string.whitespace:
      return palindrome(s[1:])   # fixed!!!
   elif s[-1] in string.punctuation or s[-1] in string.whitespace:
      return palindrome(s[:-1])
   elif s[0].lower() == s[-1].lower():
      return palindrome (s[1:-1])
   else:
      return False