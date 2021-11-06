# ---------------------------------------------------------------------------------
### RANDOM PASSWORD GENERATOR ###
# ---------------------------------------------------------------------------------
# Prints out a random password based on the number of characters that a user wants.
# ---------------------------------------------------------------------------------


import string
import random

def passgen(n):

# Simply generating random strngs of different lengths and concatenating them together.

    ran = ''.join(random.choices(string.ascii_letters, k = n*2//3))    
    pas = ''.join(random.choices(string.digits, k = n*2//9))
    dom = ''.join(random.choices(string.punctuation, k = n//9))

    return (ran +  str(pas) + str(dom))