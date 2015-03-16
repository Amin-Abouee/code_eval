import sys
import re
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		num = re.findall("Label [+-]?\d+", test)
		total = 0
		for n in num:
			a,b = n.split()
			total += int(b)
		print total