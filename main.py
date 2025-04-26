import random

print('your password is: ')

pch = "abcdefghijklmnopqrstuvwxyz/\}{)(*&^%$#@!1234567890=+_-?><,.:'

password = ''
for x in range(10):
  password += random.choice(pch)
