def curtain(a, b):

    return a-b*2 if a > b*2 else 0
def main():
    a, b = map(int, input().split())
    print(curtain(a, b))

if __name__ == '__main__':
    main()
