
def Flip_and_Flip(n , m):

    ans = 0

    if n == 1:
        if m == 1:
            ans = 1
        else:
            ans = m - 2
    else:
        ans = (n - 2)*(m - 2)

    return ans

def main():
    n , m = map(int , input().split())
    print(Flip_and_Flip(n , m))

if __name__ == '__main__':
    main()