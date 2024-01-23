def Donuts_max(n , x , ml):

    count = x - sum(ml)
    ans = n + (count // min(ml))

    return ans

def main():
    n , x = map(int, input().split())
    ml = [int(input()) for i in range(n)]
    print(Donuts_max(n , x , ml))

if __name__ == '__main__':
    main()