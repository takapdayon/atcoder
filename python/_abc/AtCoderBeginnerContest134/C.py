import copy
def exception_handling(n, ali):

    sortali = copy.copy(ali)
    sortali.sort(reverse=True)

    alimax = sortali[0]
    alimax2 = sortali[1]

    ans = []

    for i in ali:
        if i != alimax:
            ans.append(alimax)
        else:
            ans.append(alimax2)

    return ans

def main():
    n = int(input())
    ali = [int(input())for i in range(n)]
    ans = exception_handling(n, ali)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()