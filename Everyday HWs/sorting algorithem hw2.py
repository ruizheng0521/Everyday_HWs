from random import randrange

def which_algor(select, size, lst,start = None, end = None):
  if len(lst) != size:
    return "list size do not match"
  elif select == 0:
    return bubble_sort(lst)
  elif select == 1:
    return insertion_sort(lst)
  elif select == 2:
    return selection_sort(lst)
  elif select == 3:
    return merge_sort(lst)
  elif select == 4:
    quicksort_extra(lst,start,end)
    return lst
  elif select ==5:
    quicksort_in_place(lst,start,end)
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
  quicksort_extra(lst,start,new_pivot-1)
  quicksort_extra(lst,new_pivot+1,end)
  
def extra_partition(lst,start,end):
    pivot = lst[(start + end) //2]
    clone = []
    pivot, lst[start] = lst[start], pivot
    front = 0 
    back = end - start
    for i in range(start+1, end+1):
      if lst[i] < pivot:
        clone.append(lst[i])
        front +=1 
      else:
        clone.append(lst[i])
        back -=1
    clone[front] = pivot
    for i in range(start, end +1):
      lst[i] = clone[i-start]
    return start + front

def quicksort_in_place(lst,start,end):

  if end <= start:
     return None
  pivot = extra_partition(lst, start, end)
  quicksort_in_place(lst,start,pivot-1)
  quicksort_in_place(lst,pivot+1,end)

