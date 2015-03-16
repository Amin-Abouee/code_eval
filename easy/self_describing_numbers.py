import sys
with open(sys.argv[1],'r') as test_case:
	for test in test_case:
		test = test.rstrip()
		check = True
		for n in xrange(len(test)):
			if int(test[n]) != test.count(str(n)):
				print 0
				check = False
				break
		if check == True:
			print 1
