import bisect

def d162(n , sli):

    ans = 0
    Rli = []
    Gli = []
    Bli = []

    for i in range(n):
        if sli[i] == "R":
            Rli.append(i)
        elif sli[i] == "G":
            Gli.append(i)
        else:
            Bli.append(i)

    Rcount = len(Rli)
    Gcount = len(Gli)
    Bcount = len(Bli)
    Rli.sort()
    Gli.sort()
    Bli.sort()

    for i in range(n - 3):
        for w in range(i + 1 , n):
            if sli[i] != sli[w]:
                k = "RGB".replace(sli[i] , "").replace(sli[w] , "")
                if k == "R":
                    ans += Rcount - bisect.bisect_right(Rli , w)
                elif k == "G":
                    ans += Gcount - bisect.bisect_right(Gli , w)
                else:
                    ans += Bcount - bisect.bisect_right(Bli , w)
                if w + w - i < n and sli[w + (w - i)] == k:
                    ans -= 1

    return ans

def main():
    n = int(input())
    sli = list(str(input()))
    print(d162(n , sli))
if __name__ == '__main__':
    main()