word = input()
import random
print(*random.sample(word, len(word)), sep='')
