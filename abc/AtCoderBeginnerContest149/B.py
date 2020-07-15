def greedyTakahashi(a, b, k):

    a -= k

    if a < 0:
        return (0, b+a) if b+a > 0 else (0, 0)
    else :
        return (a, b)

def main():
    a, b, k = map(int, input().split())
    print(*greedyTakahashi(a, b, k))

if __name__ == '__main__':
    main()