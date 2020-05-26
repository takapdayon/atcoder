def kuku(a, b):

    return a*b if max(a, b) < 10 else -1
def main():
    a, b = map(int, input().split())
    print(kuku(a, b))

if __name__ == '__main__':
    main()
