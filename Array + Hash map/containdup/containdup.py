from collections import defaultdict
nums = input().split()
dup_map = defaultdict(int)
result = 0
for n in nums:
    dup_map[n] += 1

for value in dup_map.values():
    if value > 1:
        result += 1

if result != 0:
    print("true")
else:
    print("false")
#O(n)