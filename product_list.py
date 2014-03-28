def product_list(list):
	sum = 1
	if len(list) > 0 :
		for e in list :
			sum = sum * e
	return sum

print product_list([9,2])
