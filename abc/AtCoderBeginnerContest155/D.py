def kakeru(a , alist):
    ans = []
    for i in alist:
        ans.append(a * i)
    return ans

def pairs(n , k , a):

    kakelist = []
    for i in range(n - 1):
        kakelist += kakeru(a[i] , a[i + 1:])

    kakelist.sort()

    return kakelist[k - 1]

def main():
    n , k = map(int , input().split())
    a = list(map(int,input().split()))
    print(pairs(n , k , a))

if __name__ == '__main__':
    main()