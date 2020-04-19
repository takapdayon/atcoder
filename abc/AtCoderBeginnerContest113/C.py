
from collections import defaultdict

def id(n , m , pyli):

    ans = 0
    count = defaultdict(list)
    for i, w in pyli:
        count[i].append(w)

    for key, value in count:
        count[key].sort()


    return ans

def main():
    n , m = map(int , input().split())
    pyli = [list(map(int , input())) for i in range(m)]
    print(id(n , m , pyli))

if __name__ == '__main__':
    main()