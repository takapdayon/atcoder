def Hina_Arare(n , sl):

    ans = ""

    count = len(set(sl))

    if count == 3:
        ans = "Three"
    else:
        ans = "Four"

    return ans

def main():
    n = int(input())
    sl = list(map(str , input().split()))
    print(Hina_Arare(n , sl))


if __name__ == '__main__':
    main()