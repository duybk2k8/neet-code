#hashmap là cấu trúc lưu dữ liệu theo dạng key==> value
#==> hashmap chính là dict
#store information => value
#pair with keys (unique)

#dễ làm việc hơn với SE
#Hashmaps cho phép O(1) trong khi arrays, linked lists là O(n) => faster 

#array thì key nó là index (kiểu từ 0=>n a[0])
#hashmap dùng hashfunction => accustomed muốn assign thành key => map thành index ở list

#ví dụ
ages = {
    "An": 18,
    "Binh": 20,
    "Chi": 22
}

print(ages["Chi"])
#python sẽ hash(chi) => ra 1 số cụ thể của hash ở trong list 
#tính vị trí cụ thể trong bảng => tới vị trí đó lấy 22 => O(1)

#ví dụ: Có bảng 5 ô từ 0=>4, hash function index = key%5
#thêm key 7 => 7%5=2 => cho vào ô 2
#thêm key 12 => 12%5=2 => ô 2 đã có => collision xảy ra => đưa vào ô gần đó => 3
#thêm key 17 => 17%5=2 => ô 2 đã có => collision => đưa vào ô 2 => k dc => vào ô 3 => k dc => ô gần đó => 4
#thì khi tìm 17, hashmap sẽ tư duy như sau:
#17%5=2 => thấy ô 2 => k thấy 17 => sang ô 3 => k thấy 17 => sang ô 4 => nó thêm vài bước nhưng trung bình vẫn là O(1)

#lưu ý: khi hash function đã map key thì nó k thể modify dc=>immutable
#list có thể chỉnh khi tạo => k thể assign thành ke

#INITIALIZING HASHMAPS
#C1: city_map = {} #hoặc có thể là city_map = dict()
#C2: 
from collections import defaultdict
city_map = defaultdict(list)

cities = ["Calgary", "Vancouver", "Toronto"]
#C1: city_map["Canada"] = [] #ban đầu phải assign canada initialize với 1 info rỗng, sau đấy mới dc append vào
city_map["Canada"] += cities
print(city_map["Canada"])
#để tránh phải khai báo tập rỗng từ ban đầu => có thể dùng DefaultDict => nó đã initialized empty ray trước

#RETRIEVING DATA
#hashmap.keys() => return all keys
#hashmap.values()=> return all values
#hashmap.items() => return hết cặp key-value ở dạng tuples
city_map1 = {
    'Canada': ["Calgary", "Vancouver", "Toronto"],
    'USA' : ["New York City", "Austin", "Seattle"],
    'England' : ["London", "Manchester"]
}
print(city_map.values())

#file:///C:/Users/Admin/OneDrive/Documents/freecodecamp%202/output/pdf/giao-trinh-hashing-python.pdf

#SET
#set là tập hợp giá trị k trùng nhau => kiểm tra 1 phần tử xuất hiện hay chưa (k dc retrieve kiểu s[0] giống list, chỉ check là "4" in s? thôi)

set_sample = set()
num = input().split()
for n in num:
    set_sample.add(n) #add các phần tử k trùng nhau, nếu trùng thì k add nữa
    set_sample.remove(n) #remove, nếu phần tử k có thì error => nếu k muốn lỗi dùng discard 
len(set_sample) #số phần tử có trong


count = [0] * 26 # a ... z
#tạo mảng gồm 26 kí tự
