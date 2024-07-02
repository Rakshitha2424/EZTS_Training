import heapq

# Initial list
heap = [30, 25, 27, 18, 22, 14, 21, 7, 5]

# Convert the list into a max-heap by negating the elements
max_heap = [-x for x in heap]
heapq.heapify(max_heap)

def delete_max(max_heap):
    # Remove the largest element (root of the max-heap)
    max_element = -heapq.heappop(max_heap)
    return max_element

# Perform heap deletion
deleted_element = delete_max(max_heap)

# Convert the max-heap back to a list of positive values
resulting_heap = [-x for x in max_heap]

print("Deleted max element:", deleted_element)
print("Heap after deletion:", resulting_heap)