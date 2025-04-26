import random

print('your password is: ')

chars = 'abcdefghijklmnopqrstuvwxyz/{)(*&^%$#@!1234567890=+_-?><,.:'

password =''
for x in range(10):
  password += random.choice(chars)

print(password)
