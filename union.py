def union(list1, list2):
	for e in list2:
		if e not in list1:
			list1.append(e)

list1 = [1,2,3,4]
list2 = [21,22,23,24]
union(list1,list2)

print 'list1 : ', list1
print 'list2 : ', list2