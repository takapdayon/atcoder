def remainder_minimization(l, r):

    ans = 10**9

    for i in range(l, r):
        for w in range(i+1, r):
            ans = min(ans, (i*w)%2019)
        if ans == 0:
            break

    return ans

def main():
    l, r = map(int, input().split())
    print(remainder_minimization(l, r))

if __name__ == '__main__':
    main()