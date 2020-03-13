def xy(A):
    ans = 1
    mod = 10**9+7
    for i in range(1,A+1):
        ans = (ans * i) % mod

    return ans

def main():
    A = int(input())
    print(xy(A))

if __name__ == '__main__':
    main()
