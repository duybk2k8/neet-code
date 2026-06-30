strs = input().split()
s = ""
#ENCODE
for word in strs:
    s += str(len(word))
    s += "#" #thêm vào chuỗi string
    s += word
print(s)

#DECODE
i = 0
num = ""
res = []
#ý tưởng, duyệt từng cái, nếu nó là số => cho vào i, nếu đến # thì dừng
#===> sử dụng isdigit
#dừng sau đó cắt ===> dùng slicing
#SLICING
#Cú pháp: string[start : stop : step] (stop là dừng trước đó 1 cái, ví dụ stop = 7 thì nó chỉ nhận đến 6)

#k ghi ==True vì nó trả ra bool, True (boolean) /= "True"
while i < len(s):
    while s[i].isdigit():
        num += s[i]
        i += 1
    length = int(num)
    res.append(s[i + 1 : i + 1 + length])
    i += (length + 1) 
    num = ""
print(res)