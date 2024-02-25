def apple_pie(a, p):

    return (a*3+p)//2
def main():
    a, p = map(int, input().split())
    print(apple_pie(a, p))

if __name__ == '__main__':
    main()
