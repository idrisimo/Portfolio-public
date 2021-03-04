import random
import string

def make_miniurl(length):
    letters_numbers = string.ascii_lowercase + string.digits
    mini_string = ''.join((random.choice(letters_numbers) for item in range(length)))

    return mini_string
