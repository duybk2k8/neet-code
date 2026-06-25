from collections import defaultdict
s = input()
t = input()
s_dict = defaultdict(int)
t_dict = defaultdict(int)
for i in s:
    s_dict[i] += 1
for j in t:
    t_dict[j] += 1
if s_dict == t_dict:
    print("True")
else:
    print("False")
#for thì sẽ là O(n+m)
#so sánh dict => bảng chữ cái có 26 th nên rất nhanh ==> O(1)