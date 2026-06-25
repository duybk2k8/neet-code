nums = list(map(int, input().split()))
#input().split() là nhập 1 dãy số vào, sau đó nó sẽ split tạo thành 1 list các string
#map int là chuyển thành 1 dãy int
#list ở ngoài là biến nó thành list
target = int(input())
solution = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target and i!=j and i not in solution and j not in solution:
            solution.append(i)
            solution.append(j)
        
#cách này oke nhưng mà là O(n^2)
print(solution)