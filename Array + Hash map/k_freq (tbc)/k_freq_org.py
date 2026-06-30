from collections import defaultdict
nums=input().split()
k=int(input())
freq = defaultdict(int)
ans = []
for i in nums:
    freq[i] += 1 #đếm là O(n)

    #sort là O(mlogn) ==> cộng lại là O(nlogn)   
        
print([num for num, count in sorted(
        freq.items(), 
        key=lambda x: x[1], 
        reverse=True)[:(k)]]) 
#cắt list là O(k)
#for num,count in (đúng theo trình tự của dict)
#freq.items() trả về từng tuple (1,3) (2,2)
#lambda x:x[1] là lấy giá trị x[1] = 3 => sort theo cái đấy
#:(k) là cắt list, slicing thì lấy đến trước vị trí k => k cần -1
#chỉ return num => lấy key th
