
nums = input().split()
found = False
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            found = True
print(found)