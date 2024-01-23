def showertime(n , t , tl):
    ans = 0
    for i in range(n):
        ans += t
        if i != 0 and tl[i] - tl[i-1] < t:
            ans -= t - (tl[i] - tl[i-1])

    return ans

def main():
    n , t = map(int , input().split())
    tl = list(map(int , input().split()))
    print(showertime(n , t , tl))

if __name__ == '__main__':
    main()
