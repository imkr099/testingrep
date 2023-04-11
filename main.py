import random

# a = ''.join([random.choice(list('123456789')) for x in range(6)])
#
# print(a)
confirmation_code = random.randint(100000, 999999)
print(confirmation_code)