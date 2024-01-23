def maxreturn(a, b):

    return max(a+b, a-b, a*b)
def main():
    a, b = map(int, input().split())
    print(maxreturn(a, b))

if __name__ == '__main__':
    main()
