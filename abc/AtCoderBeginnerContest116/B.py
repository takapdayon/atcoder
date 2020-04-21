def Collatz_Problem(n):

    ans = 1
    count = []
    while True:
        if n in count:
            break
        else:
            count.append(n)
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
        ans += 1


    return ans

def main():
    n = int(input())
    print(Collatz_Problem(n))

if __name__ == '__main__':
    main()
