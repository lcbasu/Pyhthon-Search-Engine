def how_many_days(month):
	days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
	return days_in_month[month-1]
print how_many_days(12)