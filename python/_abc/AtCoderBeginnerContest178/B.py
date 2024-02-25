def b178(a, b, c, d):

    return max(max(a*c, a*d), max(b*c, b*d))

def main():
    a, b, c, d = map(int, input().split())
    print(b178(a, b, c, d))

if __name__ == '__main__':
    main()
