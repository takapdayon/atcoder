def a169(a, b):

    return a*b

def main():
    a, b = map(int, input().split())
    print(a169(a, b))

if __name__ == '__main__':
    main()