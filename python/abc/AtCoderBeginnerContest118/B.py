def Foods_Loved(n, m, kal):

    ans = 0

    for i in range(1, m+1):
        flag = True
        for ka in kal:
            if i not in ka[1:]:
                flag = False
        if flag:
            ans += 1

    return ans

def main():
    n, m = map(int, input().split())
    kal = [list(map(int, input().split())) for i in range(n)]
    print(Foods_Loved(n, m, kal))

if __name__ == '__main__':
    main()
