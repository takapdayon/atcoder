def Streamline(n, m, xl):

    xl.sort()
    count = []
    for i in range(m-1):
        count.append(xl[i+1]-xl[i])

    count.sort(reverse=True)
    ans = xl[-1]-xl[0] - sum(count[:n-1])

    return ans

def main():
    n, m = map(int, input().split())
    xl = list(map(int, input().split()))
    print(Streamline(n, m, xl))

if __name__ == '__main__':
    main()