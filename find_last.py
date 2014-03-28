def find_last(search_string, target_string):
	end_pos = -1
	while True:
		p = search_string.find(target_string,end_pos+1)
		if p == -1:
			return end_pos
		end_pos = p

search_string = 'ifest hello ifest'

target_string = 'lokesh'

print find_last(search_string,target_string)