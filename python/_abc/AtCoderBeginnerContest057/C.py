def fab(x):
    if x == 1:
        return x

    ans = 0
    for i in range(1 , x + 1):
        if -(-x // i) < i:
            return ans
        if x % i == 0:
            ans = len(str(int(x / i)))

def main():
    n = int(input())
    print(fab(n))

if __name__ == '__main__':
    main()