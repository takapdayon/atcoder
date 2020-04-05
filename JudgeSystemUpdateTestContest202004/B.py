def bjsut(n , xc):

    blue = []
    red = []

    for i in range(n):
        if xc[i][1] == "B":
            blue.append(int(xc[i][0]))
        else:
            red.append(int(xc[i][0]))

    red.sort()
    blue.sort()

    ans = red + blue

    return ans

def main():
    n = int(input())
    xc = [list(map(str , input().split())) for i in range(n)]
    ans = bjsut(n , xc)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()