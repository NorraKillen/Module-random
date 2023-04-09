import string
import random
s = [item for item in (string.ascii_letters + string.digits) if item not in 'lI1oO0']
LETTER = {'EN': [x for x in string.ascii_uppercase if x not in 'OI'],
          'en': [x for x in string.ascii_lowercase if x not in 'ol'],
          'dig': [x for x in string.digits if x not in '01']}
def generate_password(length):
    l = []
    l.append(random.choice(LETTER['EN']))
    l.append(random.choice(LETTER['en']))
    l.append(random.choice(LETTER['dig']))
    l.extend(random.sample(s, length-3))
    random.shuffle(l)
    return l
def generate_passwords(count, length):
    for i in range(count):
         print(*generate_password(length), sep='')

n, m = int(input()), int(input())

generate_passwords(n, m)