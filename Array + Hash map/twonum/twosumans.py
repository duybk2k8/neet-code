nums = list(map(int, input().split()))
target = int(input())
from collections import defaultdict
sum_set = defaultdict(int)
solution=[]


for i, num in enumerate(nums): #enumerate là lấy cái i cả giá trị
    diff = target - num
    if diff in sum_set:
        solution = [sum_set[diff], i]
    sum_set[num] = i #3:0
print(solution)
#tư duy: ví dụ lấy luôn chuỗi [3,4,5,6] target = 7
#mục tiêu: O(n)
#Tư duy 1: dùng set => ép các số vào trong => kiểu tra for i trong nums thì target - nums[i] có trong set k 
#có thì ===> print i và index(target - nums[i])
#===> NHƯỢC ĐIỂM: for duyệt n phần tử, index lại phải dò thêm n => O(n^2)

#Tư duy 2: dùng dic => for lấy luôn index và giá trị
#bắt đầu từ 0 thì num = 3, check xem target - num = 4 có trong dict k (ban đầu dict rỗng) => k có
#===> lưu số 3 vào: {3:0}
# i = 1 => num = 4 => check xem target - num = 3 có trong dict k => có => thêm i =1 và value của 3 là 0 vào solution => ok
#===> tổng quát, duyệt từng phần tử, check xem target - num có trong đó k => lưu phần tử vào dict (phần tử là key, index sẽ là value)
#sau đó nếu có thì chỉ việc lấy index là value của dict thôi => O(1)
#===> tổng sẽ là O(n)