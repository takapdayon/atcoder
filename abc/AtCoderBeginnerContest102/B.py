def Maximum(n , al):

    return abs(max(al) - min(al))

def main():
    n = int(input())
    al = list(map(int , input().split()))
    print(Maximum(n , al))

if __name__ == '__main__':
    main()