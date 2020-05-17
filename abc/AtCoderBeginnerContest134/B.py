def golden_apple(n, d):

    ans = -(-n//((d*2)+1))

    return ans

def main():
    n, d = map(int, input().split())
    print(golden_apple(n, d))

if __name__ == '__main__':
    main()
