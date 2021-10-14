age = input ('please enter your age:')
age = int(age)
if age >= 30:
	print('you can vote')
if age <= 30:
	print('no voting')

c = input ('please input degree celsius:')
c = int(c)
f = c * 9/5 + 32
print('fahrenheit is:', f)