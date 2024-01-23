def c164(n, sl):

    ans = len(set(sl))

    return ans

def main():
    n = int(input())
    sl = [str(input()) for i in range(n)]
    print(c164(n, sl))

if __name__ == '__main__':
    main()