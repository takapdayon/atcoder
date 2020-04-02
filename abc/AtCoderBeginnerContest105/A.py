def Atcoder_Crackers(n , k):

    return 0 if n % k == 0 else 1

def main():
    n , k = map(int , input().split())
    print(Atcoder_Crackers(n , k))

if __name__ == '__main__':
    main()