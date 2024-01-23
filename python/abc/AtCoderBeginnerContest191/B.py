def b191(n, x, al):

    al = [i for i in al if i != x]
    return al

n, x = map(int, input().split())
al = list(map(int, input().split()))
print(*(b191(n, x, al)))