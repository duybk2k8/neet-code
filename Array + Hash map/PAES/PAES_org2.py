#ý tưởng gợi ý, việc cứ duyệt đi duyệt lại ==> tốn tgian
#thay vì đó, tạo 1 mảng trái (tích các số bên trái số i) , 1 mảng phải ===> nhân với nhau là xong
#cthuc mảng left: left[i] = left[i-1] * nums[i-1]
nums0 = input()
nums = list(map(int, nums0.split()))
res = []
left = [1]
right = [1]
for i in range(1, len(nums)):
    left.append(left[i - 1] * nums[i - 1])
    right.append(right[i - 1] * nums[-i])

for j in range(len(nums)):
    value = left[j] * right[-j - 1]
    res.append(value)
print(res)