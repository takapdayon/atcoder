def areadifference(h , w):
    ans = 0
    count1 = 10000000000
    count2 = 10000000000
    if h % 3 == 0 or w % 3 == 0:
        return ans

    for i in range(1 , h + 1):
        hcount = max( i * w , (((h - i)//2) * w) , ((-(-(h - i)//2)) * w)) - min( i * w , (((h - i)//2) * w) , ((-(-(h - i)//2)) * w))
        wcount = max( i * w , ((h - i) * (w//2)) , ((h - i) * (-(-w//2)))) - min( i * w , ((h - i) * (w//2)) , ((h - i) * (-(-w//2))))
        count1 = min(count1 , hcount , wcount)

    for i in range(1 , w + 1):
        hcount = max( i * h , (((w - i)//2) * h) , ((-(-(w - i)//2)) * h)) - min( i * h , (((w - i)//2) * h) , ((-(-(w - i)//2)) * h))
        wcount = max( i * h , ((w - i) * (h//2)) , ((w - i) * (-(-h//2)))) - min( i * h , ((w - i) * (h//2)) , ((w - i) * (-(-h//2))))
        count2 = min(count2 , hcount , wcount)

    ans = min(count1 , count2)

    return ans

def main():
    h , w = map(int , input().split())
    print(areadifference(h , w))

if __name__ == '__main__':
    main()

