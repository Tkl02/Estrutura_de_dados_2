import random
#-------------------------------------------------bogo sort
def bogoSort(a):
	n = len(a)
	while (is_sorted(a)== False):
		shuffle(a)

def is_sorted(a):
	n = len(a)
	for i in range(0, n-1):
		if (a[i] > a[i+1] ):
			return False
	return True

def shuffle(a):
	n = len(a)
	for i in range (0,n):
		r = random.randint(0,n-1)
		a[i], a[r] = a[r], a[i]

a = [3, 2, 4, 1, 0, 5]
bogoSort(a)
print("Sorted array :")
for i in range(len(a)):
	print ("%d" %a[i]),
#--------------------------------------------------------------
#---------------------------------------------------bubble sort
def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		if not swapped:
			return

arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")

#---------------------------------------------------------------
#----------------------------------------------------bucket sort
def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up	
	return b	
			
def bucketSort(x):
	arr = []
	slot_num = 10 
				
	for i in range(slot_num):
		arr.append([])

	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)

	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])

	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x

x = [0.897, 0.565, 0.656,
	0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))
#------------------------------------------------------
#-----------------------------------------cocktail sort
def cocktailSort(a):
	n = len(a)
	swapped = True
	start = 0
	end = n-1
	while (swapped == True):

		swapped = False

		for i in range(start, end):
			if (a[i] > a[i + 1]):
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True

		if (swapped == False):
			break

		swapped = False

		end = end-1

		for i in range(end-1, start-1, -1):
			if (a[i] > a[i + 1]):
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True

		start = start + 1

a = [5, 1, 4, 2, 8, 0, 2]
cocktailSort(a)
print("Sorted array is:")
for i in range(len(a)):
	print("% d" % a[i])

#--------------------------------------------------
#----------------------------------------gnome sort

def gnomeSort( arr, n):
	index = 0
	while index < n:
		if index == 0:
			index = index + 1
		if arr[index] >= arr[index - 1]:
			index = index + 1
		else:
			arr[index], arr[index-1] = arr[index-1], arr[index]
			index = index - 1

	return arr

arr = [ 34, 2, 10, -9]
n = len(arr)

arr = gnomeSort(arr, n)
print( "Sorted sequence after applying Gnome Sort :")
for i in arr:
    print (i)

#------------------------------------------------
#---------------------------------------heap sort

def heapify(arr, N, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	if l < N and arr[largest] < arr[l]:
		largest = l

	if r < N and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		heapify(arr, N, largest)

def heapSort(arr):
	N = len(arr)

	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i)

	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]

	heapSort(arr)
	N = len(arr)

	print("Sorted array is")
	for i in range(N):
		print("%d" % arr[i], end=" ")

#-----------------------------------------------------------
#---------------------------------------------insertion sort

def insertionSort(arr):

	for i in range(1, len(arr)):
		key = arr[i]

		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])

#----------------------------------------------------------
#------------------------------------------------merge sort
def mergeSort(arr):
	if len(arr) > 1:

		mid = len(arr)//2

		L = arr[:mid]

		R = arr[mid:]

		mergeSort(L)

		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)

#-------------------------------------------------------
#---------------------------------------------quick sort
def partition(array, low, high):

	pivot = array[high]

	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1

			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1])

	return i + 1

def quick_sort(array, low, high):
	if low < high:

		pi = partition(array, low, high)

		quick_sort(array, low, pi - 1)

		quick_sort(array, pi + 1, high)

array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')

#-------------------------------------------------------------
#---------------------------------------------------radix sort
def countingSort(arr, exp1):

	n = len(arr)

	output = [0] * (n)

	count = [0] * (10)

	for i in range(0, n):
		index = arr[i] // exp1
		count[index % 10] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = n - 1
	while i >= 0:
		index = arr[i] // exp1
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	i = 0
	for i in range(0, len(arr)):
		arr[i] = output[i]

def radixSort(arr):

	max1 = max(arr)

	exp = 1
	while max1 / exp >= 1:
		countingSort(arr, exp)
		exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]

radixSort(arr)

for i in range(len(arr)):
	print(arr[i],end=" ")
#--------------------------------------------------------
#------------------------------------------selection sort
def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):

			if array[j] < array[min_index]:
				min_index = j

		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)

#--------------------------------------------------------
#------------------------------------------------tim sort
MIN_MERGE = 32
def calcMinRun(n):
	"""Returns the minimum length of a
	run from 23 - 64 so that
	the len(array)/minrun is less than or
	equal to a power of 2.

	e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
	..., 127=>64, 128=>32, ...
	"""
	r = 0
	while n >= MIN_MERGE:
		r |= n & 1
		n >>= 1
	return n + r

def insertionSort(arr, left, right):
	for i in range(left + 1, right + 1):
		j = i
		while j > left and arr[j] < arr[j - 1]:
			arr[j], arr[j - 1] = arr[j - 1], arr[j]
			j -= 1

def merge(arr, l, m, r):

	len1, len2 = m - l + 1, r - m
	left, right = [], []
	for i in range(0, len1):
		left.append(arr[l + i])
	for i in range(0, len2):
		right.append(arr[m + 1 + i])

	i, j, k = 0, 0, l

	while i < len1 and j < len2:
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1

		else:
			arr[k] = right[j]
			j += 1

		k += 1

	while i < len1:
		arr[k] = left[i]
		k += 1
		i += 1

	while j < len2:
		arr[k] = right[j]
		k += 1
		j += 1

def timSort(arr):
	n = len(arr)
	minRun = calcMinRun(n)

	for start in range(0, n, minRun):
		end = min(start + minRun - 1, n - 1)
		insertionSort(arr, start, end)

	size = minRun
	while size < n:

		for left in range(0, n, 2 * size):

			mid = min(n - 1, left + size - 1)
			right = min((left + 2 * size - 1), (n - 1))

			if mid < right:
				merge(arr, left, mid, right)

		size = 2 * size

if __name__ == "__main__":

	arr = [-2, 7, 15, -14, 0, 15, 0,
		7, -7, -4, -13, 5, 8, -14, 12]

	print("Given Array is")
	print(arr)

	timSort(arr)

	print("After Sorting Array is")
	print(arr)
	
