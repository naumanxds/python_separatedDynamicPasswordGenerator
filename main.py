import random

file = open('testfile.txt', 'r')
username = []
passwords = []

for l in file:
	combo = l.split(':')
	username.append(combo[0])
	passwords.append(combo[1].rstrip('\n'))

file.close()
print(random.choice(passwords))

