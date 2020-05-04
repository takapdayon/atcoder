def b166(n, k):

    count = []
    for i in range(k):
        d = int(input())
        al = []
        a = 0
        if d == 1:
            a = int(input())
            count.append(a)
        else:
            al = list(map(int, input().split()))
            for w in al:
                count.append(w)

    return n - len(set(count))

def main():
    n, k = map(int, input().split())
    print(b166(n, k))

if __name__ == '__main__':
    main()