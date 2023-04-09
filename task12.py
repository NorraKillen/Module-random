import string
import random
def generate_password(length):
    s = [item for item in (string.ascii_letters + string.digits) if item not in 'lI1oO0']
    return random.sample(s, length)
def generate_passwords(count, length):
    for i in range(count):
         print(*generate_password(length), sep='')

n, m = int(input()), int(input())

generate_passwords(n, m)