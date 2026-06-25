nums = list(map(int, input().split()))
target = int(input())
A = []
for i, num in enumerate(nums):
    A.append([num, i])

A.sort()
i, j = 0, len(nums) - 1
while i < j:
    cur = A[i][0] + A[j][0]
    if cur == target:
        print [min(A[i][1], A[j][1]),
        max(A[i][1], A[j][1])]
    elif cur < target:
        i += 1
    else:
        j -= 1
#tạo 1 mảng A khác, sort theo giá trị: index
#Giờ lấy i là chuột từ trái, j là chuột từ phải, bắt đầu lấy i+j > target thì lại lấy j - 1 i+1 cứ đẩy lên đẩy xuống đến khi nào bằng nhau
#lấy [min(a,b) max (a,b)] => giống sort