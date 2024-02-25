def b190(n, s, d, xy):

    for xyi in xy:
        if xyi[0] < s and xyi[1] > d:
            return 'Yes'

    return 'No'

n, s, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
print(b190(n, s, d, xy))