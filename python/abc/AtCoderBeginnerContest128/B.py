def guidebook(n, spli):

    ans = []
    for i in range(n):
        temp = [i+1, spli[i][0], (-1)*int(spli[i][1])]
        ans.append(temp)
    ans.sort(key=lambda x: (x[1], x[2]))
    return ans
def main():
    n = int(input())
    spli = [list(map(str, input().split()))for i in range(n)]
    ans = guidebook(n, spli)
    for i in ans:
        print(i[0])

if __name__ == '__main__':
    main()