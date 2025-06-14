import heapq


def sort_through_heap(iterable):
    heap = []
    sorted_list = []
    
    for value in iterable:
        heapq.heappush(heap, -value)
        
    while heap:
        sorted_list.append(-heapq.heappop(heap))
        
    return sorted_list


nums = [5, 3, 8, 1, 2, 7, 30, 20 , 11, 100]
desc_sorted = sort_through_heap(nums)
print('Descending sorted: ', desc_sorted)
    