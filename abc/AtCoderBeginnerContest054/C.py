N , M = map(int , input().split())
A = [list(map(int,input().split())) for i in range(M)]
tf = [False]*N

for i in range(M):
    A.append(list(reversed(A[i])))

def saiki(aaa):
    ans = 0
    if all(tf) == True:
        return 1
    stack = []
    for i in range(len(A)):
        if A[i][0] == aaa and tf[A[i][1]-1] == False:
            stack.append(A[i][1])

    for i in range(len(stack)):
        tf[stack[i]-1] = True
        ans += saiki(stack[i])
        tf[stack[i]-1] = False
    return ans

def main():
    tf[0] = True
    ans = saiki(1)
    print(ans)

if __name__ == '__main__':
    main()