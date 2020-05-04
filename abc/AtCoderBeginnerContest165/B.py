def b165(x):

    ans = 0
    manycount = 100
    for i in range(10000000):
        if manycount >= x:
            break
        else:
            ans += 1
            manycount += manycount//100

    return ans

def main():
    x = int(input())
    print(b165(x))

if __name__ == '__main__':
    main()