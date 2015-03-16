import sys
with open(sys.argv[1],'r') as test_cases:
	for test in test_cases:
		a , b = test.split()
		words = ['-','+']
		index = [i for i, x in enumerate(list(b)) if x in words]
		num_1 = a[:int(index[0]):]
		num_2 = a[int(index[0])::]
		if '+' in list(b):
			print int(num_1) + int(num_2)
		else:
			print int(num_1) - int(num_2)