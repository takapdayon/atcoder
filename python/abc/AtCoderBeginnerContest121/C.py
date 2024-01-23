def energy_drink_collector(n, m, abli):

    ans = 0
    count = m
    abli.sort(key=lambda x: x[0])

    for i in abli:
        if i[1] <= count:
            ans += i[0]*i[1]
            count -= i[1]
        else:
            ans += count*i[0]
            count = 0
        if not count:
            break
    return ans

def main():
    n, m = map(int, input().split())
    abli = [list(map(int, input().split()))for i in range(n)]
    print(energy_drink_collector(n, m, abli))

if __name__ == '__main__':
    main()