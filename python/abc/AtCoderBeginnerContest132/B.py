def ordinary_number(n, pli):

    ans = 0

    for i in range(1, n-1):
        if pli[i-1] != pli[i] != pli[i+1]:
            if pli[i-1] + pli[i] + pli[i+1] - max(pli[i-1], pli[i], pli[i+1]) - min(pli[i-1], pli[i], pli[i+1]) == pli[i]:
                ans += 1

    return ans

def main():
    n = int(input())
    pli = list(map(int, input().split()))
    print(ordinary_number(n, pli))

if __name__ == '__main__':
    main()
