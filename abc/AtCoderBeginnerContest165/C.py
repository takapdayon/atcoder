import itertools

def c165(n, m, q, adli):

    ans = 0
    li = list(itertools.combinations_with_replacement(range(1,m+1), n))
    for i in li:
        count = 0
        for a, b, c, d in adli:
            if i[b-1] - i[a-1] == c:
                count += d
        ans = max(ans, count)

    return ans

def main():
    n, m, q = map(int, input().split())
    adli = [list(map(int, input().split()))for i in range(q)]
    print(c165(n, m, q, adli))

if __name__ == '__main__':
    main()