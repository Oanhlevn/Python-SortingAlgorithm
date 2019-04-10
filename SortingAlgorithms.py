import random 
import time
def random_array(len):
  array = []
  for x in range(0, len):
    randnum= random.randrange(0,len)
    array.append(randnum)
  return array 
print(random_array(5))
pass

def is_sorted(arr):
  # Returns true if arr is sorted properly, smallest to largest.
  print(arr)
  for i in range(0,len(arr)-1): 
    if arr[i]> arr[i+1]:
       return False
  return True 
print (is_sorted(random_array(5)))
pass

def bogosort(arr):
  #print(arr)
  while is_sorted(arr) == False: 
    random.shuffle(arr)
  return arr 
a=random_array(4)
start = time.time()
bogosort(a)
end = time.time()
print(end-start)
print(a)
#%time bogosort(a)
assert is_sorted(a)
#pass



def selection_sort(arr): 
  print(arr)
  for i in range(0,len(arr)):
    unsorted_arr=[]
    for j in range(i+1, len(arr)): 
      unsorted_arr.append(arr[j])
      print(unsorted_arr)
      smallest= min(unsorted_arr)
      print (smallest)
      smallestindex = arr.index(smallest)
      print(smallestindex)
    if arr[i] > smallest:
      temp= arr[i]
      arr[i]=smallest
      arr[smallestindex]= temp
  return arr 
print(selection_sort([6,8,9,10,4,17,34,2,1,0])) 
assert is_sorted(selection_sort([6,8,9,10,4,17,34,2,1,0]))
start = time.time()
selection_sort([6,8,9,10,4,17,34,2,1,0])
end = time.time()
print("Selection_Sort_Time:",end-start)

def Bubble_Sort(arr): 
  print(arr)
  for i in range (0,len(arr)-1):
    if arr[i] > arr[i+1]: 
      temp = arr[i]
      arr[i] = arr[i+1]
      arr[i+1] = temp 
      print(arr)
    for j in range (0,len(arr)-1-i ): 
      if arr[j]>arr[j+1]:
       temp= arr[j]
       arr[j] = arr[j+1]
       arr[j+1]= temp
       print(arr)  
  return arr
print(Bubble_Sort([10,4,8,23,17,45,11,22,89,0]))
assert is_sorted(Bubble_Sort([6,8,9,10,4,17,34,2,1,0]))
start = time.time()
Bubble_Sort([6,8,9,10,4,17,34,2,1,0])
end = time.time()
print("BubbleSortTime:",end-start)

def Quick_Sort(arr): 
  print(arr)
  if len(arr) <=1: 
    return arr
  else:
    pivot = arr[len(arr)-1]
    print("pivot",pivot)
    pivotarr= []
    smallerarr = []
    higherarr = []
    for i in range(0,len(arr)):   
      if arr[i]> pivot: 
        higherarr.append(arr[i])
        print("higerarr",higherarr)
      elif arr[i]< pivot:
       smallerarr.append(arr[i])
       print("smallerarr",smallerarr)
      else:
       pivotarr.append(arr[i])
       print("pivotarr",pivotarr)   
  return  Quick_Sort(smallerarr) + pivotarr + Quick_Sort(higherarr)
print(Quick_Sort([10,4,8,23,17,45,11,22,89,23]))
assert is_sorted(Quick_Sort([6,8,9,10,4,17,34,2,1,0]))
start = time.time()
Quick_Sort([6,8,9,10,4,17,34,2,1,0])
end = time.time()
print("Quick_Sort_Time:",end-start)

def Merge(arr1,arr2):
  c=[]
  while len(arr1)>0 and len(arr2)>0:
   if arr1[0]< arr2[0]:
     c.append(arr1[0])
     arr1.remove(arr1[0])
   else: 
     c.append(arr2[0])
     arr2.remove(arr2[0])
  while len(arr1)>0 and len(arr2)==0:
    c.append(arr1[0])
    arr1.remove(arr1[0])
  while len(arr1)==0 and len(arr2)>0:
    c.append(arr2[0])
    arr2.remove(arr2[0])
  return c 
  print ("arrayc:", c)

def Merge_Sort(arr): 
  #split the arr
  print(arr)
  if len(arr) <=1: 
    return arr
  else:
    arr1=[]
    arr2=[]
    for i in range(0,len(arr)/2):
      arr1.append(arr[i])
      print("array1:",arr1)
    for i in range(len(arr)/2,len(arr)):
      arr2.append(arr[i])
      print("array2:",arr2)
    arr1= Merge_Sort(arr1) 
    arr2= Merge_Sort(arr2)
  return Merge(arr1,arr2)
print(Merge_Sort([6,8,9,10,4,17,34,2,1,0]))
assert is_sorted(Quick_Sort([6,8,9,10,4,17,34,2,1,0]))
start = time.time()
Quick_Sort([6,8,9,10,4,17,34,2,1,0])
end = time.time()
print("Quick_Sort_Time:",end-start)



     








