def d165(n):

    ans = 0
    for i in range(1, 200000):
        count = 2019*i
        if n.count(str(count)) != 0:
            ans += n.count(str(count))
    return ans

def main():
    n = str(input())
    print(d165(n))
if __name__ == '__main__':
    main()