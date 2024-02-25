def Grand_Garden(n, hl):

    ans = 0
    maxlen = max(hl)
    for i in range(maxlen):
        for w in range(n):
            if hl[w] == 0:
                continue
            elif w+1 == n:
                ans += 1
                hl[w] -= 1
                continue
            elif hl[w+1] == 0:
                ans += 1
            hl[w] -= 1

    return ans

def main():
    n = int(input())
    hl = list(map(int, input().split()))
    print(Grand_Garden(n, hl))

if __name__ == '__main__':
    main()