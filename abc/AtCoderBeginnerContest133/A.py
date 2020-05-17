def tort(n, a, b):

    return min(n*a, b)
def main():
    n, a, b = map(int, input().split())
    print(tort(n, a, b))

if __name__ == '__main__':
    main()
