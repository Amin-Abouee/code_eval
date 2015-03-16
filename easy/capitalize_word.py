import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		lst = [word[0].upper() + word[1:] if word[0].isalpha() else word for word in test.split() ]
		print ' '.join(lst)