def c160(k , n , al):

    count = 0

    for i in range(n):
        if i == n - 1:
            count = max(count , (k - al[i]) + al[0])
        else:
            count = max(count , al[i + 1] - al[i])

    return k - count

def main():
    k , n = map(int , input().split())
    al = list(map(int , input().split()))
    print(c160(k , n , al))
if __name__ == '__main__':
    main()