N , M = map(int , input().split())
A = [str(input()) for i in range(N)]
B = [str(input()) for i in range(M)]

def bina(A , B):
    for i in range((N-M)+1):
        for w in range(N):
            c = []
            for q in range(M):
                c += [A[i+q][w:w+M]]
            if c == B:
                return "Yes"
    return "No"

if __name__ == '__main__':
    ans = bina(A , B)
    print(ans)
