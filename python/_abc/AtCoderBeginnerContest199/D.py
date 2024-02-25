def saiki(aaa, color):
    ans = 0
    if all(tf) == True:
        return 1
    stack = []
    for i in range(len(m)):
        if A[i][0] == aaa and tf[A[i][1]-1] == False:
            stack.append(A[i][1])

    for i in range(len(stack)):
        tf[stack[i]-1] = True
        ans += saiki(stack[i])
        tf[stack[i]-1] = False
    return ans

def d199(n, m, abl):
    # 深さ優先探索や...
    # あと組み合わせやな, 行けるかこれ
    # おもいだしいやぁ
    if m == 0:
        return 3 ** n
    if m == 1:
        return (3 ** n + n) // 2
    ans = saiki(1, 1)
    return ans

n, m = map(int, input().split())
abl = [list(map(int, input().split())) for i in range(m)]
tf = [False]*n
color = [0]*n
print(d199(n, m, abl))




N , M = map(int , input().split())
A = [list(map(int,input().split())) for i in range(M)]


for i in range(M):
    A.append(list(reversed(A[i])))


def main():
    tf[0] = True
    ans = saiki(1)
    print(ans)

if __name__ == '__main__':
    main()