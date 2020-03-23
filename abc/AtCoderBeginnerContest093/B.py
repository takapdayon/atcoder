def Small_and_Large(a , b , k):

    ans = []

    for i in range(k):
        if a + i <= b:
            ans.append(a + i)
        if b - i >= a:
            ans.append(b - i)

    return sorted(set(ans))

def main():
    a , b , k = map(int , input().split())
    ans = Small_and_Large(a, b, k)
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()