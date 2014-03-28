def find_element_new(list, search_string):	
	if search_string in list:
		return list.index(search_string)
	else:
		return -1

list = [1,2,3,4,5,6,7,8,9,0]
print find_element_new(list,1)