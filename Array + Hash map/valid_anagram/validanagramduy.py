s = input()
t = input()
if sorted(s) == sorted(t):
        print("True")
else:
        print("False")
#(Sort là O(nlogn + mlogm)) sort cần qua nhiều tầng (chia đôi là log n xong nhiều tầng n => n.logn)