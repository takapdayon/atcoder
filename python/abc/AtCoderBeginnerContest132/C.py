def divide_the_problems(n, dli):

    dli.sort()

    n = int(n/2)
    ans = dli[n] - dli[n-1]

    return ans

def main():
    n = int(input())
    dli = list(map(int, input().split()))
    print(divide_the_problems(n, dli))

if __name__ == '__main__':
    main()