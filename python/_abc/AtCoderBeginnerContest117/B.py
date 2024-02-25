def Polygon(n, ll):

    return "Yes" if max(ll) < sum(ll)-max(ll) else "No"

def main():
    n = int(input())
    ll = list(map(int, input().split()))
    print(Polygon(n, ll))

if __name__ == '__main__':
    main()
