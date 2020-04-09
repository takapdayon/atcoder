def Atcoder111(n):

    ans = ""

    if int(n[0]) > int(n[1]) or int(n[0]) == int(n[1]) >= int(n[2]):
        ans = n[0]*3
    else:
        ans = int(n[0]*3)
        ans += 111

    return ans

def main():
    n = str(input())
    print(Atcoder111(n))

if __name__ == '__main__':
    main()