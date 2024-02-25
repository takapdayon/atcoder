def P_Number(a , b):

    ans = 0

    for i in range(a, b + 1):
        rev = str(i)
        if str(i) == rev[::-1]:
            ans += 1

    return ans

def main():
    a , b = map(int , input().split())
    print(P_Number(a , b))


if __name__ == '__main__':
    main()