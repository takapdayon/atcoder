def b160(x):

    ans = 0

    ans += (x // 500) * 500 * 2
    nokori = x % 500
    ans += (nokori // 5) * 5

    return ans

def main():
    x = int(input())
    print(b160(x))

if __name__ == '__main__':
    main()