import math
def good_distance(n, d, xli):

    ans = 0

    for i in range(n):
        for q in range(i+1, n):
            count = 0
            for w in range(d):
                count += (xli[i][w]-xli[q][w])**2

            if math.sqrt(count).is_integer():
                ans += 1

    return ans

def main():
    n, d = map(int, input().split())
    xli = [list(map(int, input().split()))for i in range(n)]
    print(good_distance(n, d, xli))

if __name__ == '__main__':
    main()
