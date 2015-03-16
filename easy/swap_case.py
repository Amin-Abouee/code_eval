import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		res = ''
		for s in test:
			if s.islower():
				res += str(s.upper())
			elif s.isupper():
				res += str(s.lower())
			else:
				res += str(s)
		print res,