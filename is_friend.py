def is_friend(name):
	name_initial = name[0]
	if((name_initial == 'D') or (name_initial == 'N')):
		return True
	else:
		return False

print is_friend('Nalin')