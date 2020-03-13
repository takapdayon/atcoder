def bmon(n , a , b):

    ans = 0
    count = n // (a + b)
    ans = count * a

    ans += min(n % (a + b), a)

    return ans

def main():
    n , a , b = map(int , input().split())
    print(bmon(n , a , b))

if __name__ == '__main__':
    main()