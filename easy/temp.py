import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    num = [int(x) for x in test.split()]
    temp = map(str, range(1,num[2]+1))
    temp = ['FB' if (x.isdigit() and int(x) % num[0] == 0 and int(x) % num[1] == 0) else x for x in temp]
    temp = ['F' if (x.isdigit() and int(x) % num[0] == 0) else x for x in temp]
    temp = ['B' if (x.isdigit() and int(x) % num[1] == 0) else x for x in temp]
    print ' '.join(map(str, temp))
test_cases.close()