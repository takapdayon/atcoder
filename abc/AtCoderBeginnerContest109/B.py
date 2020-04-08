
def Shiritori(n , wli):

    ans = "Yes"

    if len(set(wli)) != len(wli):
        ans = "No"
    else:
        last = (wli[0])[0]
        for i in wli:
            if last != i[0]:
                ans = "No"
                break
            last = i[-1]

    return ans

def main():
    n = int(input())
    wli = [str(input()) for i in range(n)]
    print(Shiritori(n , wli))

if __name__ == '__main__':
    main()