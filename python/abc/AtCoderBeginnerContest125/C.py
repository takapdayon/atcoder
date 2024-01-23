import copy

from fractions import gcd
from functools import reduce

def gcdli(xl):
    #xlはlist
    return reduce(gcd , xl)

def gcd_on_blackboard(n, ali):

    ans = 0

    for i in range(n):
        count = copy.copy(ali)
        count.pop(i)
        ans = max(ans, gcdli(count))

    return ans

def main():
    n = int(input())
    ali = list(map(int, input().split()))
    print(gcd_on_blackboard(n, ali))

if __name__ == '__main__':
    main()