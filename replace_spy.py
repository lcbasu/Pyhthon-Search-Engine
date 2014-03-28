def replace_spy(list):
	list[2] = list[2] + 1
	#we don't need return here, because we just need to modify the value

list = [0,3,4]
replace_spy(list)
print list