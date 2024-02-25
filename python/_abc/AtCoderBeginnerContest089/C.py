from itertools import combinations

def March(n , sl):

    ans = 0
    count = {m: 0 for m in list("MARCH")}

    for i in sl:
        if i[0] in count:
            count[i[0]] += 1

    c = combinations(list("MARCH"), 3)
    for q, w, i in c:
        ans += count[q] * count[w] * count[i]

    return ans

def main():
    n = int(input())
    sl = [str(input()) for i in range(n)]
    print(March(n , sl))

if __name__ == '__main__':
    main()