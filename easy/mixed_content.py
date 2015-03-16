import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		test = test.rstrip()
		s = [x for x in test.split(',')]
		num = [x for x in s if x.isdigit()]
		word = [x for x in s if x.isalpha()]
		if len(word) > 0 and len(num) == 0: 
			print ','.join(word)
		elif len(num) > 0 and len(word) > 0:
			print ','.join(word) + '|' +  ','.join(num)
		elif len(word) == 0  and len(num) > 0:
			print ','.join(num)