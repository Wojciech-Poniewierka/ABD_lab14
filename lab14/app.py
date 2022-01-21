#bubblesort algorithm

def bubblesort(unsorted):
	l = len(unsorted)
	while l > 1:
		for i in range(0, l-1):
			if unsorted[i] > unsorted[i+1]:
				unsorted[i+1], unsorted[i] = unsorted[i], unsorted[i+1]
		l -= 1
	return unsorted

