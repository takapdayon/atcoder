def digits(n , r):

    ans = 0
    if r == 2:
        ans = len(bin(n)) - 2
    elif r == 8:
        ans = len(oct(n)) - 2
    elif r == 10:
        ans = len(str(n))
    else:
        ans = len(hex(n)) - 2

    return ans

def main():
    n , r = map(int , input().split())
    print(digits(n , r))

if __name__ == '__main__':
    main()
