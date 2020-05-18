def harmony(a, b):

    return "IMPOSSIBLE" if abs(a-b)%2 != 0 else int(abs(a-b)//2)+min(a,b)
def main():
    a, b = map(int, input().split())
    print(harmony(a, b))

if __name__ == '__main__':
    main()
