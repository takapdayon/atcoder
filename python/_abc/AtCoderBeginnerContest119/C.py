from fractions import gcd
from functools import reduce

def gcdli(xl):
    #xlはlist
    return reduce(gcd , xl)

def monsters_battle_royale(n, al):

    ans = gcdli(al)

    return ans

def main():
    n = int(input())
    al = list(map(int, input().split()))
    print(monsters_battle_royale(n, al))

if __name__ == '__main__':
    main()