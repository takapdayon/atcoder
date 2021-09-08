def b205(n, alist):

    if len(set(alist)) != len(alist):
        return "No"

    return "Yes"

n = int(input())
alist = list(map(int, input().split()))
print(b205(n, alist))
