import sys
test_cases = open('sample.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    num = [int(x) for x in test.split(',')]
    binary = bin(num[0])
    # print len(binary)
    if binary[len(binary)-num[1]] == binary[len(binary)-num[2]]:
    	print 'true'
    else:
    	print 'false'
test_cases.close()