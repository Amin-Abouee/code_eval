import sys
with open(sys.argv[1]) as sample_tests:
	for test in sample_tests:
		num = int(test)
		if num >= 0 and num <= 2:
			print "Still in Mama's arms"
		elif num >= 3 and num <= 4:
			print "Preschool Maniac"
		elif num >= 5 and num <= 11:
			print "Elementary school"
		elif num >= 12 and num <= 14:
			print "Middle school"
		elif num >= 15 and num <= 18:
			print "High school"
		elif num >= 19 and num <= 22:
			print "College"
		elif num >= 23 and num <= 65:
			print "Working for the man"
		elif num >= 66 and num <= 100:
			print "The Golden Years"
		else:
			print "This program is for humans"