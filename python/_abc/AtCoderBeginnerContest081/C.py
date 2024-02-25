def NotsoDiverse(n , k , al):

    lis = [0]*(n + 1)

    for i in range(n):
        lis[al[i]] += 1

    lis.sort(reverse=True)

    ans = sum(lis[k:])
    return ans

def main():
    n , k = map(int , input().split())
    al = list(map(int , input().split()))
    print(NotsoDiverse(n , k , al))

if __name__ == '__main__':
    main()
