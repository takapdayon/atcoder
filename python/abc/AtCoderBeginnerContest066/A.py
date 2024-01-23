def miner(a):
    
    a.sort()
    ans = int(a[0]) + int(a[1])
    return ans

def main():
    a = list(map(int , input().split()))
    print(miner(a))

if __name__ == '__main__':
    main()