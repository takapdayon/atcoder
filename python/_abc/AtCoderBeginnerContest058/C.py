def mozi(n , s):
    ans = ""
    for code in range(ord('a'), ord('z') + 1):
        azmin = 50
        for i in range(n):
            azmin = min(azmin , str(s[i]).count(chr(code)))

        if azmin != 0:
            for i in range(azmin):
                ans += chr(code)

    return ans

def main():
    n = int(input())
    #s = [list(map(str , input())) for i in range(n)]
    s = [list(map(str , input().split())) for i in range(n)]
    print(mozi(n , s))

if __name__ == '__main__':
    main()
