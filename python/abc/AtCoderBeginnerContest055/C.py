def scc(N , M):
    ans = 0
    if N * 2 >= M:
        ans += M // 2
        return ans
    else:
        ans += N
        M -= N*2
        ans += M//4
        return ans

def main():
    N , M = map(int , input().split())
    print(scc(N , M))

if __name__ == '__main__':
    main()
