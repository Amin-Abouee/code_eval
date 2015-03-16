import sys
with open(sys.argv[1]) as test_cases:
    table = [[0 for x in xrange(256)] for x in xrange(256)]
    for test in test_cases:
        s = [x for x in test.split()]
        if s[0] == 'SetRow':
        	table[int(s[1])] = [int(s[2])] * 256
        elif s[0] == 'SetCol':
            for x in xrange(len(table)):
                table[x][int(s[1])] = int(s[2])
        elif s[0] == 'QueryRow':
            print sum(table[int(s[1])])
        elif s[0] == 'QueryCol':
            total = 0
            for x in xrange(len(table)):
                total += table[x][int(s[1])]
            print total
        else:
        	pass