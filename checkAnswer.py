import random


def check_answer():
    return True if random.randint(0, 1) % 2 == 0 else False
