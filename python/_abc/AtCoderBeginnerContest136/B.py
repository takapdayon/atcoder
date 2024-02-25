def uneven_numbers(n):

    ans = 0

    for i in range(1, n+1):
        if len(str(i)) % 2 != 0:
            ans += 1

    return ans

def main():
    n = int(input())
    print(uneven_numbers(n))

if __name__ == '__main__':
    main()
