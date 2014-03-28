def make_hashtable(nbuckets):
	i = 0
	table = []
	while i < nbuckets:
		table.append([])
		i = i + 1
	return table

print make_hashtable(5)