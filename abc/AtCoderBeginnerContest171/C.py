def c171(n):

    ans = ""
    while n > 0:
        n -= 1
        ans += chr(ord('a') + n % 26)
        n //= 26

    return ans[::-1]

def main():
    n = int(input())
    print(c171(n))

if __name__ == '__main__':
    main()