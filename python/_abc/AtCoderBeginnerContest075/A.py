def differenceone(a , b , c):

    ans = 0
    if a == b:
        ans = c
    elif b == c:
        ans = a
    else:
        ans = b

    return ans

def main():
    a , b , c = map(int , input().split())
    print(differenceone(a , b , c))

if __name__ == '__main__':
    main()