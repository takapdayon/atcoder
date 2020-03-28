n , x , y = map(int , input().split())

flag = [False] * n
checksu = 0
lili = [list([i , i + 1]) for i in range(1 , n)]
lili += [list([lili[i][1] , lili[i][0]]) for i in range(len(lili))]
lili.append([x , y])
lili.append([y , x])

def saiki(i , w):

    hairetu = []
    ans = 0

    if i == 0:
        if w < checksu:
            return 0
        else:
            return 1

    for q in lili:
        if q[0] == w and flag[q[1] - 1] == False:
            hairetu.append(q[1])

    for q in hairetu:
        flag[q - 1] == True
        ans += saiki(i - 1 , q)

    return ans

ans = []

for i in range(1 , n):
    count = 0
    for w in range(1 , n):
        checksu = w
        flag = [False] * n
        count += saiki(i , w)
    ans.append(count)

for i in range(len(ans)):
    print(ans[i])
