import sys
with open(sys.argv[1]) as test_cases:
    for test in test_cases:
        a,b = [int(x) for x in test.split(',')]
        while a >= b:
            a -= b
        print a