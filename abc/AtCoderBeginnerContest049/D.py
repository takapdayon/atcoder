def saiki():

    ans = 0

    return ans

def renketu(n , k , l , pqli , rsli):

    #再起関数を呼ぶ
    ans = []

    return ans

def main():
    n, k, l = map(int, input().split())
    pqli = [list(int(input())) for i in range(k)]
    rsli = [list(int(input())) for i in range(l)]
    print(renketu(n , k , l , pqli , rsli))

if __name__ == '__main__':
    main()