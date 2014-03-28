def hash_string(keyword, buckets):
	word_value = 0
	for e in keyword:
		word_value = (word_value + ord(e))%buckets
	return word_value

def make_hashtable(nbuckets):
	i = 0
	table = []
	while i < nbuckets:
		table.append([])
		i = i + 1
	return table

def hashtable_get_bucket(hashtable,key):
	return hashtable[hash_string(key,len(hashtable))]

def hashtable_add(htable,key,value):
	bucket = hashtable_get_bucket(htable,key)
	bucket.append([key,value])

def hashtable_lookup(htable,key):
	bucket = hashtable_get_bucket(htable,key)
	for e in bucket:
		if e[0] == key:
			return e[1]
	return None

def hashtable_update(htable,key,value):
	bucket = hashtable_get_bucket(htable,key)
	for e in bucket:
		if e[0] == key:
			e[1] = value
			return
	return hashtable_add(htable,key,value)
	


table = make_hashtable(3)
hashtable_add(table,'udacity',23)

print table

print hashtable_lookup(table,'udacity')

hashtable_update(table,'udacity',27)

print hashtable_lookup(table,'udacity')

hashtable_update(table,'udacityNEW',31)

print table