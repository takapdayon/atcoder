from collections import defaultdict
def unification(s):

    ans = 0
    d = defaultdict(int)
    for k in s:
       d[k] += 1

    ans = len(s) - abs(d["0"]-d["1"])

    return ans

def main():
    s = str(input())
    print(unification(s))

if __name__ == '__main__':
    main()