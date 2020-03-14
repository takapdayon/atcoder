def Lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return Lucas(n-1)+Lucas(n-2)

def main():
    n = int(input())
    print(Lucas(n))

if __name__ == '__main__':
    main()
