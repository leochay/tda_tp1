import sys

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
    # print(a[:j])
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
  return

def selection(filerandom):
  print("selection")
  b=[]
  with open(filerandom, 'r') as f:
    for line in f:
      b.append(int(line))
  #print(b)
  from timeit import default_timer as timer
  #slice create a copy of the array
  results={}
  mean=0
  for x in xrange(0,20):
    print(x)
    a=b[:]
    start = timer()
    selectionsort(a)
    end = timer()
    results[x]=end-start
    print (results[x])
    mean+=end-start
  print(x)
  mean=mean/(x+1)
  print (mean)
  return


def insertion(filerandom):
  print("selection")
  b=[]
  with open(filerandom, 'r') as f:
    for line in f:
      b.append(int(line))
  #print(b)
  from timeit import default_timer as timer
  #slice create a copy of the array
  results={}
  mean=0
  for x in xrange(0,5):
    print(x)
    a=b[:]
    start = timer()
    insertionsort(a)
    end = timer()
    results[x]=end-start
    print (results[x])
    mean+=end-start
  print(x)
  mean=mean/(x+1)
  print (mean)
  return

def insertion(filerandom):
  print("selection")
  b=[]
  with open(filerandom, 'r') as f:
    for line in f:
      b.append(int(line))
  #print(b)
  from timeit import default_timer as timer
  #slice create a copy of the array
  results={}
  mean=0
  for x in xrange(0,5):
    print(x)
    a=b[:]
    start = timer()
    quicksort(a)
    end = timer()
    results[x]=end-start
    print (results[x])
    mean+=end-start
  print(x)
  mean=mean/(x+1)
  print (mean)
  return

def sort(type,number,worstcase):

  sorts = {'selection': selectionsort,
  'insertion': insertionsort,
  'quick': quicksort,
  'merge': mergesort,
  'heap': heapsort}

  method_name = myargs['-i']
     # set by the command line options
    #if myargs[]
  if type not in sorts:
    raise Exception("Sort Algorithm %s not implemented" % type)
    exit()

  if worstcase:
    file='worstcase'
  else:
    file=number+'.random'
  b=[]
  with open(file, 'r') as f:
    for line in f:
      b.append(int(line))
  #print(b)
  from timeit import default_timer as timer
  #slice create a copy of the array
  results={}
  mean=0
  for x in xrange(0,10):
    print(x)
    a=b[:]
    start = timer()
    sorts[type](a)
    end = timer()
    results[x]=end-start
    print (results[x])
    mean+=end-start
  print(x)
  mean=mean/(x+1)
  print (mean)
  return

def runAll():
  print ("run all")
  return

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)
    if myargs.has_key('-i'):
      sort(myargs['-i'],myargs['-n'],myargs.has_key('-w'))
    else:
      runAll()
    exit()
#main
#print("selection sort")
##unsortedList=[20,10,50,70,100,3,2,9]
##f = open('50.random', 'r')
##list(f)
##two forms of running a file load
##first form simple code but not memory efficient
#with open('50.random', 'r') as f:
# a=list(f)
#print(a)
##doble array conversion from string to int
#a = [int(i) for i in a]
##print(a)
##second form
#b=[]
#with open('50.random', 'r') as f:
# for line in f:
#   b.append(int(line))
##print(b)

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
