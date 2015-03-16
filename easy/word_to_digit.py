import sys
with open(sys.argv[1],'r') as test_cases:
	convertor = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
	for test in test_cases:
		test = test.rstrip()
		words = [x for x in test.split(';')]
		print ''.join([convertor[word] for word in words])

