import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		test = test.rstrip()
		cities = [x for x in test.split(";")]
		cities.remove('')
		distance = []
		for element in cities:
			a = element.split(",")
			distance.append(int(a[1]))
		distance.sort()
		res = []
		res.append(distance[0])
		for i in xrange(1,len(distance)):
			res.append(distance[i] - distance[i-1])
		print ','.join(map(str,res))
