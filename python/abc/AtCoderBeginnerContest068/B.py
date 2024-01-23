def breaknumbeer(n):

    ans = 1

    while ans <= n:
        ans *= 2

    return int(ans / 2)

def main():
    n = int(input())
    print(breaknumbeer(n))

if __name__ == '__main__':
    main()