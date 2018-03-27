#unsorted list uList
#sorted list sList
#do 
#take smallest from unsorted List
#insert in the sorted list
#while there is element in the unsorted list

def selectionsort(array):
	for j in xrange(len(array)):
		iMin=j
		for i in xrange(j+1,len(array)):
			if array[i] <array[iMin]:
				iMin=i

		if iMin!=j:
			aux = array[j]
			aarray[j]=array[iMin]
			array[iMin]=aux
		#	print(a[:j])
def insertionsort(array):
    for i in xrange(1, len(array)):
        j = i-1 
        key = array[i]
        while (array[j] > key) and (j >= 0):
           array[j+1] = array[j]
           j -= 1
        [j+1] = key

def quicksort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quicksort(less)
        more = quicksort(more)
        return less + pivotList + more

def heapsort(array):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(array)-2)/2, -1, -1):
    siftdown(array, start, len(array)-1)
 
  for end in range(len(array)-1, 0, -1):
    array[end], array[0] = array[0], array[end]
    siftdown(array, 0, end - 1)
  return array
 
def siftdown(array, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and array[child] > array[child + 1]:
      child += 1
    if array[root] > array[child]:
      array[root], array[child] = array[child], array[root]
      root = child
    else:
      break

def mergesort(array):
	if len(array) < 2:
		return array

	middle = int(len(array)/2)
	left = mergesort(array[:middle])
	right = mergesort(array[middle:])

	return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result            

def runSorts(filerandom):
	b=[]
	with open(filerandom, 'r') as f:
		for line in f:
			b.append(int(line))
	#print(b)
	from timeit import default_timer as timer
	a=b[:]#slice create a copy of the array
	start = timer()
	selectionsort(a)
	end = timer()
	print(end - start)
	a=b[:]
	start = timer()
	insertionsort(a)
	end = timer()
	print(end - start)
	a=b[:]
	start = timer()
	quicksort(a)
	end = timer()
	print(end - start)
	a=b[:]
	start = timer()
	heapsort(a)
	end = timer()
	print(end - start)
	a=b[:]
	start = timer()
	mergesort(a)
	end = timer()
	print(end - start)

	print(b)


#main
print("selection sort")
#unsortedList=[20,10,50,70,100,3,2,9]
#f = open('50.random', 'r')
#list(f)
#two forms of running a file load
#first form simple code but not memory efficient
with open('50.random', 'r') as f:
	a=list(f)
print(a)
#doble array conversion from string to int
a = [int(i) for i in a]
#print(a)
#second form
b=[]
with open('50.random', 'r') as f:
	for line in f:
		b.append(int(line))
#print(b)

runSorts('50.random')
runSorts('100.random')
runSorts('500.random')
runSorts('1000.random')
runSorts('2000.random')
runSorts('3000.random')
runSorts('4000.random')
runSorts('5000.random')
runSorts('7500.random')
runSorts('10000 .random')

#MIT IMPLEMENTATION
#def selSort(L):
#    for i in range(len(L) - 1):
#        minIndx = i
#        minVal = L[i]
#        j = i+1
#        while j < len(L):
#            if minVal > L[j]:
#                minIndx = j
#                minVal = L[j]
#            j += 1
#        if minIndx != i:
#            temp = L[i]
#            L[i] = L[minIndx]
#            L[minIndx] = temp	
