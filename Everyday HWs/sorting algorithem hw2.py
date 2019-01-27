from random import *

def which_algor(select, size, lst,start = None, end = None):
  if len(lst) != size:
    return "list size do not match"
  if select == 0:
    return bubble_sort(lst)
  elif select == 1:
    return insertion_sort(lst)
  elif select == 2:
    return selection_sort(lst)
  elif select == 3:
    return merge_sort(lst)
  elif select == 4:
    quicksort_inplace(lst,start,end)
    return lst
  elif select ==5:
    quicksort_extra(lst)
    return lst
  else:
    return "Invalid"

def bubble_sort(lst):
  for i in range(len(lst)-1,0,-1):
    for j in range(i):
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
  return lst
def insertion_sort(lst):
  for i in range(len(lst)):
    for j in range(len(lst)):
      if lst[j] > lst[i]:
        lst[j],lst[i]=lst[i],lst[j]
  return lst
def selection_sort(lst):
  for i in range(len(lst)-1,-1,-1):
    maxi_index = 0
    for j in range(i+1):
      if lst[j] >= lst[maxi_index]:
        maxi_index = j
    lst[maxi_index],lst[i] = lst[i],lst[maxi_index]
  return lst
def merge_sort_list(lst1,lst2):
  i = j = 0
  sorted_lst = []
  while i<len(lst1) and j<len(lst2):
    if lst1[i] > lst2[j]:
      sorted_lst.append(lst2[j])
      j += 1
    else:
      sorted_lst.append(lst1[i])
      i += 1
  if i < len(lst1):
    sorted_lst.extend(lst1[i:])
  
  elif j < len(lst2):
    sorted_lst.extend(lst2[j:])

  return sorted_lst
def merge_sort(lst):
  
  if len(lst) ==0 or len(lst)==1:
    return lst
  else:
    mid_point = len(lst)//2
    lst1 = merge_sort(lst[:mid_point])
    lst2 = merge_sort(lst[mid_point:])
    return merge_sort_list(lst1,lst2)
def partition(lst, start, end , pivot_index):
  lst[pivot_index],lst[end] = lst[end],lst[pivot_index]
  store_index = start
  pivot = lst[end]
  for i in range(start,end):
    if lst[i] < pivot:
        lst[i], lst[store_index] = lst[store_index],lst[i]
        store_index += 1
  lst[store_index], lst[end] = lst[end],lst[store_index]
  return store_index


def quicksort_inplace(lst,start,end):
  if end <= start:
     return None
  pivot_index = randrange(start,end+1)
  new_pivot = partition(lst, start, end, pivot_index)
  quicksort_inplace(lst,start,new_pivot-1)
  quicksort_inplace(lst,new_pivot+1,end)
  
def quicksort_extra(lst):
  if len(lst) <= 1:
      return lst
  k = lst[0]
  array_a, array_b = [], []
  for i in range(1, len(lst)):
      if lst[i] >= k:
          array_b.append(lst[i])
      else:
          array_a.append(lst[i])
  return quicksort_extra(array_a)+ [k] + quicksort_extra(array_b)

test = []
for i in range(120):
  test.append(randint(1,100))
sorts =sorted(test)

for k in range(6):
  key = test
  print(which_algor(k, 100, key,0,len(key)-1))
  print(sorts == key)

