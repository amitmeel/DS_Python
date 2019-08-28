# binary search example in Python
# here Arr is an of integer type, n is size of array 
#	and target is element to be found
def binarySearch(Arr, n, target) :
	#set stating and ending index
	start, end = 0, n-1

	while start <= end :
		mid = (start + end) // 2
		# we found a match
		if Arr[mid] == target :
			return mid
		# go on right side
		elif Arr[mid] < target :
			start = mid + 1
		# go on left side
		else :
			end = mid - 1;
	# element is not present in list
	return "Not Found"


print(binarySearch([1,2,3,4], 4, 9))