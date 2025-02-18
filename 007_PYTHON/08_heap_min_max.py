    
    
    
import heapq

def nsmallest(arr,n):
    heap = []

    heapq.heapify(heap)
    for i in arr:
        heapq.heappush(heap,i)
    
    for i in range(0,n-1):
        heapq.heappop(heap)

    return heapq.heappop(heap)

def nlargest(arr,n):
    heap = []

    heapq.heapify(heap)
    for i in arr:
        heapq.heappush(heap,-i)
    
    for i in range(0,n-1):
        heapq.heappop(heap)

    return -heapq.heappop(heap)
num=[2,1,5,3,1,8]
print(nlargest(num,1))
print(nsmallest(num,1))