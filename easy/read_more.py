import sys
with open('sample.txt','r') as test_cases:
	for test in test_cases:
		test = test.rstrip()
		sz = len(test)
		if sz <= 55:
			print test
		else:
			test = test[0:40:]
			inx = test.rfind(' ')
			test = test[0:inx:]
			test += "... <Read More>"
			print test
