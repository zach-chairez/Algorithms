'''
TC = time complexity
AS = auxillary space

Sorting Algorithms:
    - Bubble Sort - O(n^2) TC / O(1) AS
    - Insertion Sort - O(n^2) but can be O(n) TC / O(1) AS
    - Merge Sort - O(nlogn) TC / O(n) AS
'''

# Functions:  
#    bubble_sort, insertion_sort, and merge_sort
# Input:      
#    unsorted_array - list of unsorted integers
# Purpose:  
#   The functions listed above will 
#   sort the list "unsorted_array" and output its sorted version.

import random, time

a = 0; b = 50000; len_of_array = 20000
unsorted_array = random.sample(range(a,b+1),len_of_array)


''' Bubble Sort Algorithm '''
def bubble_sort(input_array):
           
    for i in range(len(input_array)):
        swap = False
        
        for j in range(0,len_of_array-i-1):
            
            if input_array[j] > input_array[j+1]:
                input_array[j],input_array[j+1] = input_array[j+1],input_array[j] 
                swap = True
                
        if swap == False:
            break 
     
    return input_array

''' Insertion Sort Algorithm ''' 
def insertion_sort(input_array):
    
    for i in range(1,len(input_array)):
        value = input_array[i]
        j = i - 1
        
        while j >= 0 and value < input_array[j]:
            input_array[j+1] = input_array[j]
            j -= 1
        input_array[j+1] = value
    
    return input_array


''' Merge Sort Algorithm '''
def merge_sort(input_array):
    
    if len(input_array) <= 1:
        return input_array
    
    mid_loc = len(input_array) // 2
    left_array = merge_sort(input_array[:mid_loc])
    right_array = merge_sort(input_array[mid_loc:])
    
    return merge(left_array,right_array)

def merge(left_array,right_array):
    merged_array = []
    i = j = 0
    
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            j += 1
    merged_array.extend(left_array[i:])
    merged_array.extend(right_array[j:])
    
    return merged_array
    
    
# Checking function results and computational time
bubble_time = time.time()
sorted_list_bubble = bubble_sort(unsorted_array)
bubble_time = time.time() - bubble_time

insert_time = time.time()
sorted_list_insertion = insertion_sort(unsorted_array)
insert_time = time.time() - insert_time

merge_time = time.time()
sorted_list_merge = merge_sort(unsorted_array)
merge_time = time.time() - merge_time

print(f"Bubble sort took {bubble_time} seconds to complete")
print(f"Insertion sort took {insert_time} seconds to complete")
print(f"Merge sort took {merge_time} seconds to complete")
        

        