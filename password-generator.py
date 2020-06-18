#! python3
import string
import random

charQty = 12

while True:

  try:
    charQty=int(input("How many characters you want in the password?: "))
  except:
    print('Invalid number, please try again...')
    continue
  else:
    break

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(list(map(lambda x: random.choice(characters), range(charQty))))

print(f'Password: {password}')