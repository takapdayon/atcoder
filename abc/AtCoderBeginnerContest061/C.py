def smallk(n , k , ab):
    count = 0
    for i in range(n):
        if count + int(ab[i][1]) >= k:
            return int(ab[i][0])
        else:
            count += int(ab[i][1])

def main():
    n , k = map(int , input().split())
    ab = [list(map(int,input().split())) for i in range(n)]
    ab.sort()
    print(smallk(n , k , ab))

if __name__ == '__main__':
    main()
