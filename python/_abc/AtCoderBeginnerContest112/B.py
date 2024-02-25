def Time_Limit_Exceeded(n , t , ctl):

    count = []

    for i in ctl:
        if i[1] <= t:
            count.append(i[0])

    return min(count) if len(count) != 0 else "TLE"

def main():
    n , t = map(int , input().split())
    ctl = [list(map(int , input().split())) for i in range(n)]
    print(Time_Limit_Exceeded(n , t , ctl))

if __name__ == '__main__':
    main()