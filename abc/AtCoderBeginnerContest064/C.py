def ratecount(n , a):

    ansmin = 0
    ansmax = 0
    highrater = 0
    leftnumeral = [1 , 400 , 800 , 1200 , 1600 , 2000 , 2400 , 2800]
    rightnumeral = [399 , 799 , 1199 , 1599 , 1999 , 2399 , 2799 , 3199]
    count = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]

    for i in range(len(leftnumeral)):
        for w in range(n):
            if int(a[w]) >= int(leftnumeral[i]) and int(a[w]) <= int(rightnumeral[i]):
                count[i] = 1

    for i in range(n):
        if int(a[i]) >= 3200:
            highrater += 1

    if sum(count) == 0:
        ansmin = 1
        ansmax = highrater if highrater <= len(leftnumeral) else 8
    else:
        ansmin = sum(count)
        ansmax = (sum(count) + highrater) if sum(count) + highrater <= len(leftnumeral) else 8

    return str(ansmin) + " " + str(ansmax)

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(ratecount(n , a))

if __name__ == '__main__':
    main()