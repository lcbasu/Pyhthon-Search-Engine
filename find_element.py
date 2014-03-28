def find_element(list,search_element):
	index = 0
	for e in list:
		if e == search_element:			
			return index
		index = index + 1
	return -1

list = [1,2,3,4,5,6,7,8,9,0]
print find_element(list,5)