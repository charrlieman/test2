import random


ans = random. randint(1, 100)


while True:
	guess = input ('Guess the number:')
	guess = int(guess)
	if ans == guess:
		print('Correct!')
		break

	elif ans > guess: 
		print('It is larger')

	elif ans < guess:
		print('It is smaller')
