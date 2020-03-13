import bisect

def snukefestival(n , a , b , c):

    ans = 0
    a.sort()
    b.sort()
    c.sort()

    for i in b:
        ab = bisect.bisect_left(a , i)
        cb = bisect.bisect_right(c , i)
        ans += ab * (len(b) - cb)

    return ans

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int , input().split()))
    print(snukefestival(n , a , b , c))

if __name__ == '__main__':
    main()