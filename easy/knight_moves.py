import sys
with open (sys.argv[1],'r') as test_cases:
	for test in test_cases:
		test = test.rstrip()
		h , v = [x for x in test]
		all_pose = []
		# print h, v
		if ord(h) - ord('a') >= 2:
			if ord(v) - ord('1') >= 1:
				all_pose.append('%s%s' % (chr(ord(h) - 2), chr(ord(v) - 1)))
			if ord('8') - ord(v) >= 1:
				all_pose.append('%s%s' % (chr(ord(h) - 2), chr(ord(v) + 1)))
		if ord('h') - ord(h) >= 2:
			if ord(v) - ord('1') >= 1:
				all_pose.append('%s%s' % (chr(ord(h) + 2), chr(ord(v) - 1)))
			if ord('8') - ord(v) >= 1:
				all_pose.append('%s%s' % (chr(ord(h) + 2), chr(ord(v) + 1)))
		if ord(v) - ord('1') >= 2:
			if ord(h) - ord('a') >= 1:
				all_pose.append('%s%s' % (chr(ord(h) - 1), chr(ord(v) - 2)))
			if ord('h') - ord(h) >= 1:
				all_pose.append('%s%s' % (chr(ord(h) + 1), chr(ord(v) - 2)))
		if ord ('8') - ord(v) >= 2:
			if ord(h) - ord('a') >= 1:
				all_pose.append('%s%s' % (chr(ord(h) - 1), chr(ord(v) + 2)))
			if ord('h') - ord(h) >= 1:
				all_pose.append('%s%s' % (chr(ord(h) + 1), chr(ord(v) + 2)))
		print ' '.join(sorted(all_pose))

# e1 e3 f4 h4
# b3 c2
# b5 b7 c4 c8 e4 e8 f5 f7
# c4 c6 d3 d7 f3 f7 g4 g6
# a3 c3 d2
