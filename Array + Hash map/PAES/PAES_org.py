nums0 = input()
nums = list(map(int, nums0.split()))
res = []
for i in range(len(nums)):
    nums_alt = nums.copy() #nums_alt = nums thì đều chỉ cùng 1 số => phải tạo bản sao
    value = 1
    nums_alt.pop(i) #dùng remove thì nó kbt xóa theo vị trí, nó xóa theo giá trị => trùng thì xóa k đúng chỗ
    #===> sử dụng pop: pop là xóa phần tử ở đúng vị trí đó, nếu string.pop() ==> nó auto xóa con cuối
    for j in nums_alt:
        value *= j
    res.append(value)
print(res)
