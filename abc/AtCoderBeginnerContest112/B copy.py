from collections import defaultdict

defadict = defaultdict(int)
nordict = {1:1 , 2:2 , 3:3}
for i in range(3):
    defadict[i] += i

print(defadict)
print(nordict)

print(list(defadict.items()))
print(list(nordict.items()))
