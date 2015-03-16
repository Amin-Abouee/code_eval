import sys
with open(sys.argv[1]) as test_cases:
	morse = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G',
	'....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O',
	'.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W',
	'-..-':'X','-.--':'Y','--..':'Z','-----':'0','.----':'1','..---':'2','...--':'3',
	'....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'}
	for test in test_cases:
		test = test.rstrip()
		test = test.replace("  ", " * ")
		word = [morse[x] if x in morse else x for x in test.split()]
		word = [' ' if x == '*' else x for x in word]
		print ''.join(word)

