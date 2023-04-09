import random

def generate_ip():
    u = []
    for i in range(4):
        u.append(str(random.randint(0, 255)))

    return '.'.join(u)
