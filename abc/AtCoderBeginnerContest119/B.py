def digital_gifts(n, xuli):

    ans = 0

    for i in xuli:
        if i[1] == "JPY":
            ans += float(i[0])
        else:
            ans += float(i[0])*380000

    return ans

def main():
    n = int(input())
    xuli = [list(map(str, input().split())) for i in range(n)]
    print(digital_gifts(n, xuli))

if __name__ == '__main__':
    main()
