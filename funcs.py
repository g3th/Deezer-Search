
#longest string in a list ('max()' returns incorrect values)

def longest(value):
	maxs = '';a=0
	while a < len(value):
		if len(value[a]) > len(maxs):
			maxs = value[a]
		a +=1
	return maxs
	
#calculate TUI spaces
	
def spaces(value, index):
	nspace = 0
	if len(value[index]) < len(longest(value)):
		nspace = len(longest(value))-len(value[index])+2
	else:
		nspace = 2
	return nspace

#string characters are not English (i.e. Japanese, Arabic, Cyrillic...)

def takinOurJobs(string):
	try:
		string.encode(encoding='utf-8').decode('ascii')
	except UnicodeError:
		string = string.replace(string[10:],'..')
	return string
