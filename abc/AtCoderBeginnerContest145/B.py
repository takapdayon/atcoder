def echo(n, s):

    sharf = s[:int(n//2)]

    return "Yes" if s == sharf+sharf else "No"

def main():
    n = int(input())
    s = str(input())
    print(echo(n, s))

if __name__ == '__main__':
    main()