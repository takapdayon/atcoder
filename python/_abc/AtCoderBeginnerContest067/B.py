def snaketoy(n , k , l):

    ans = 0
    l.sort(reverse=True)
    ans = int(sum(l[:k]))

    return ans

def main():
    n , k = map(int , input().split())
    l = list(map(int , input().split()))
    print(snaketoy(n , k , l))

if __name__ == '__main__':
    main()