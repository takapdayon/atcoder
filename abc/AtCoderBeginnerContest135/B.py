import copy
def or01swap(n, pli):

    plis = copy.copy(pli)
    plis.sort()
    count = 0

    for i in range(n):
        if pli[i] != plis[i]:
            count += 1

    return "YES" if count <= 2 else "NO"

def main():
    n = int(input())
    pli = list(map(int, input().split()))
    print(or01swap(n, pli))

if __name__ == '__main__':
    main()
