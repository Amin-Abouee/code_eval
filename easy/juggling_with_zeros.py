import sys
with open(sys.argv[1]) as test_sample:
	for test in test_sample:
		test = test.rstrip()
		s = test.split()
		flags = s[0::2]
		seqs = s[1::2]
		bin = ''
		for i in xrange(len(flags)):
			if flags[i] == '0':
				bin += seqs[i]
			else:
				bin += '1' * len(seqs[i])

		print int(bin,2)
