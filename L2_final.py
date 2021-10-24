password = 'a123456'
i = 3
while True:
	pwd = input('please input the password:')
	if password == pwd:
		print('login successful')
		break
	else:	
		i = i - 1
		print('you still have', i  ,'times entry')
		if i == 0:
			break
		