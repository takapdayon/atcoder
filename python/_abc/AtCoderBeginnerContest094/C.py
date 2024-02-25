import copy

def Many_Medians(n , xl):

    ans = []
    left = n // 2
    right = n // 2 - 1
    sort_xl = sorted(xl)

    for x in xl:
        if x < sort_xl[left]:
            ans.append(sort_xl[left])
        else:
            ans.append(sort_xl[right])

    return ans

def main():
    n = int(input())
    xl = list(map(int , input().split()))
    ans = Many_Medians(n, xl)
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()