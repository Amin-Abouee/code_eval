import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		temp1 = [n for n in test if (n <= 'j' and n >= 'a') or n.isdigit()]
		res = [str(ord(n) - ord('a')) if n <= 'j' and n >= 'a' else n for n in temp1]
		if len(res):
			print ''.join(res)
		else:
			print "NONE"