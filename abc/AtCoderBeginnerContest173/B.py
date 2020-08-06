from collections import defaultdict

def b173(n, slist):

    countdict = defaultdict(int)

    for s in slist:
        countdict[s] += 1

    return countdict

def main():
    tlist = ["AC", "WA", "TLE", "RE"]
    n = int(input())
    slist = [str(input())for i in range(n)]
    countdict = b173(n, slist)

    for t in tlist:
        print(t + " x " + str(countdict.get(t, 0)))

if __name__ == '__main__':
    main()