# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
import heapq
heapq.heapify(A)
#k hoàn toàn sort => chỉ tạo ra heap map th

#Heap Push (Insert element)
#Time: O(logn (bỏ 1 nửa đi ===> tổng logn))
heapq.heappush(A, 4)
print(A)

#Heap Pop (Extract min)
#Time: O(logn)
minn = heapq.heappop(A)

print(A, minn) #take min = -4

#Heap Sort
#Time: O(n logn), Space: O(n)
#Note: O(1) space is possible via swapping, but this is complex

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list
#sort dc hết chứ k chỉ sort ra heap

#Heap Push Pop: Time: O(log n)
heapq.heappushpop(A, 99)
#push 99 vào và pop out root 0

#Peak at the min: Time: O(1)
A[0]

#Max Heap
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)
for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)
#chuyển về hết âm => sort min
largest = -heapq.heappop(B)
#force về max

heapq.heappush(B, -7) #Insert 7 into max heap ==> phải push ngược lại

#Build heap from scratch: Time: O(n log n)
C = [-5, 4, 2, 1, 7,  0, 3]
heap = []
for x in C:
    heapq.heappush(heap, x)
    print(heap, len(heap)) #check size of heap

#Putting tuples of items on the heap
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter
counter = Counter(D) # tạo dictionary count tần suất
#key là giá trị, value là frequency
for k, v in counter.items():
    print(k, v)