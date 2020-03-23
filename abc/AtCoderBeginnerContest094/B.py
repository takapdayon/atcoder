import bisect

def Toll_Gates(n , m , x , al):

    al.sort()
    ans = 0

    left = bisect.bisect_left(al, x)
    right = m - left

    ans = min(left , right)

    return ans

def main():
    n , m , x = map(int , input().split())
    al = list(map(int, input().split()))
    print(Toll_Gates(n , m , x , al))

if __name__ == '__main__':
    main()