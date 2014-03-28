def biggest(num1,num2,num3):
	max = num1
	if(num2 > max):
		max = num2
		if(num3 > max):
			max = num3
	else:
		if(num3 > max):
			max = num3
	return max

print biggest(99,88,3)

#biggest using bigger procedure defined earlier

def bigger(num1,num2):
	max = num1
	if(num2>max):
		max = num2
	return max

def biggest_new(num1,num2,num3):
	return bigger(bigger(num1,num2),num3)

print 'biggest with bigger'
print biggest_new(1,2,3)