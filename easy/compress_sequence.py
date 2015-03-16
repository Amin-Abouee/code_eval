import sys
import collections
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		test = test.rstrip()
		num = [x for x in test.split()]
		# preserve_order = list(collections.OrderedDict.fromkeys(num))
		# c = collections.Counter(num)
		# for element in preserve_order:
			# print "%s %s" %(c[element], str(element)),
		# print
		cnt = 0
		indicator = num[0]
		for x in num:
			if x == indicator:
				cnt += 1
			else:
				print "%d %s" %(cnt,indicator),
				indicator = x
				cnt = 1
		print "%d %s" %(cnt,indicator)