def Colorful(a, b, c, d):

    return "Yes" if (abs(a - b) <= d and abs(b - c) <= d) or abs(a - c) <= d else "No"

def main():
    a , b , c , d = map(int , input().split())
    print(Colorful(a , b , c , d))

if __name__ == '__main__':
    main()