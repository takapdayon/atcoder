def b162(n):

    ans = 0

    for i in range(1 , n + 1):
        if i % 3 != 0 and i % 5 != 0:
            ans += i

    return ans

def main():
    n = int(input())
    print(b162(n))

if __name__ == '__main__':
    main()