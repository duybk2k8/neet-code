nums = input().split()
hashset=set()
for n in nums:
    if n in hashset:
        print("True")
    hashset.add(n)
print("False")

#print thành return, khi đã return true là dừng luôn, k tiếp tục đi nữa
#ý tưởng: k cần quá cầu kì như dict
#ném từng con 1 vào, check xem con đó đã trong set chưa, rồi thì true, k thì false