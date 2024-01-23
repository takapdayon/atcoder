def b163(n, m, al):


    return n - sum(al) if n - sum(al) >= 0 else "-1"

def main():
    n , m = map(int, input().split())
    al = list(map(int, input().split()))
    print(b163(n, m, al))

if __name__ == '__main__':
    main()