def find_second(search_string,target_string):
	first_occur = search_string.find(target_string)
	second_occur = search_string.find(target_string,first_occur+1)
	return second_occur

search_string = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><title>iFest 2012</title><link rel="stylesheet" type="text/css" href="css/style_makeover.css" /><p class="copyright"><span>&copy; IEEE IIT Roorkee | <a href="http://ifest1.ieeeiitr.com/ifest_2011.php">iFest 2011</a></span></div></body></html><span>&copy; IEEE IIT Roorkee | <a href="http://ifest2.ieeeiitr.com/ifest_2011.php">iFest 2011</a></span></div></body></html><span>&copy; IEEE IIT Roorkee | <a href="http://ifest3.ieeeiitr.com/ifest_2011.php">iFest 2011</a></span></div></body></html><span>&copy; IEEE IIT Roorkee | <a href="http://ifest4.ieeeiitr.com/ifest_2011.php">iFest 2011</a></span></div></body></html>'

target_string = 'ifest'

print find_second(search_string,target_string)