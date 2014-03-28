def hash_string(keyword, buckets):
	word_value = 0
	for e in keyword:
		word_value = (word_value + ord(e))%buckets
	return word_value

print hash_string('udacity',12)