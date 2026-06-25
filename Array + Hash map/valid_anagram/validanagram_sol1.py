s = input()
t = input()

#counter(s) ==> hashmap count think automatically
#counter(t) => return (counter(s) == counter(t))
#y hệt cái dưới mà ít dòng hơn th
if len(s) != len(t):
    print("False")

countS, countT = {}, {}
for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    #get là giống countS[s[i]] => lấy value int nhưng mà nếu k có thì sẽ auto là 0
    countT[t[i]] = 1 + countT.get(t[i], 0)
for c in countS:
    if countS[c] != countT.get(c,0): 
        print("False")
    else:
        print("True") 

#nếu c k có trong countT để k bị collision => get