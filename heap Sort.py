#heap Sort 
# Heap sort can be understood as the improved version of the binary search tree. 
# It does not create a node as in case of binary search tree instead it builds
#  the heap by adjusting the position of elements
#  within the array itself. In which method a tree structure called heap 
# is used where a heap is a type of binary tree.

#Implementations
#importtant  Module from heap Module
from heapq import heappush,heappop

#create function for heap
def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)
    
    ordered = []

    # element left in the top heap
    while heap:
        ordered.append(heappop(heap))

    return ordered



# array 
array = [14,22,15,3,27,9,16,35,18,22,1]
print('the result of the heap sort:')
print(heap_sort(array))
