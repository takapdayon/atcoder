from collections import defaultdict
def c163(n, al):

    count = defaultdict(int)

    for i in range(n-1):
        count[al[i]] += 1

    return count

def main():
    n = int(input())
    al = list(map(int, input().split()))
    dilist = c163(n, al)
    for i in range(1 , n + 1):
        try:
            print(dilist[i])
        except:
            print("0")

if __name__ == '__main__':
    main()