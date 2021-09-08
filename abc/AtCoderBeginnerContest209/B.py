def b209(n, x, alist):

    alla = sum(alist) - (len(alist) // 2)

    if alla <= x:
        return "Yes"
    return "No"

n, x = map(int, input().split())
alist = list(map(int, input().split()))
print(b209(n, x, alist))
