import statistics

def temp(x, y, k, alist):
    pond = []
    for tk in range(k):
        for uk in range(k):
            pond.append(alist[y+tk][x+uk])

    return statistics.median_low(pond)

def d203(n, k, alist):

    mostmin = 10**9

    for y in range(n-k+1):
        for x in range(n-k+1):
            mostmin = min(mostmin, temp(x, y, k, alist))

    return mostmin

n, k = map(int, input().split())
alist = [list(map(int, input().split())) for _ in range(n)]
print(d203(n, k, alist))