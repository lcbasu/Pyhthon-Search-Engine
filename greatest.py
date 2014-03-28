def greatest(list):
	max = 0
	if len(list) > 0 :
		for e in list :
			if e > max :
				max = e
	return max

print greatest([1,2,3,4,5,1,5])