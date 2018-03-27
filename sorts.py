#unsorted list uList
#sorted list sList
#do 
#take smallest from unsorted List
#insert in the sorted list
#while there is element in the unsorted list

def selectionsort(a):
	for j in xrange(len(a)):
		iMin=j
		for i in xrange(j+1,len(a)):
			if a[i] < a[iMin]:
				iMin=i

		if iMin!=j:
			aux = a[j]
			a[j]=a[iMin]
			a[iMin]=aux
		#	print(a[:j])
def insertionsort(a):
    for i in xrange(1, len(a)):
        j = i-1 
        key = a[i]
        while (a[j] > key) and (j >= 0):
           a[j+1] = a[j]
           j -= 1
        a[j+1] = key

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

def heapsort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break

def mergesort(left, right):
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
