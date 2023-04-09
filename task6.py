import random
def generate_index():
    b = ''
    for i in range(2):
        b += (chr(random.randint(97, 122))).upper()
    b += str(random.randint(0, 99))
    b += '_'
    b += str(random.randint(0, 99))
    for i in range(2):
        b += (chr(random.randint(97, 122))).upper()
    return b