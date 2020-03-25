def Exponential(x):

    ans = 0
    if x == 1:
        ans = 1
    else:
        for i in range(1, x + 1):
            for w in range(2, x + 1):
                if i ** w > x:
                    break
                else:
                    ans = max(ans, i ** w)

    return ans

def main():
    x = int(input())
    print(Exponential(x))

if __name__ == '__main__':
    main()