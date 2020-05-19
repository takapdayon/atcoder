def transfer(a, b, c):

    return 0 if a > b+c else c+b-a
def main():
    a, b, c = map(int, input().split())
    print(transfer(a, b, c))

if __name__ == '__main__':
    main()
