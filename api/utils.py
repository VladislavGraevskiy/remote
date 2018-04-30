import string

import random


def get_random_string(size=10):
    """
    Returns a random string.
    If you need securely generated random string use django.utils.crypto.get_random_string
    The default length of 10 with the a-z, 0-9 character
    """
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(size))
