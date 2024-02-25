def ddd(s , q , ql):

    ans = ""
    leftans = "" #1
    rightans = "" #2
    count = 0

    for i in range(q):
        if int(ql[i][0]) == 2:
            #ans = ans[::-1]
            if count % 2 == 0:
                if int(ql[i][1]) == 1:
                    leftans = ql[i][2] + leftans
                else:
                    rightans = rightans + ql[i][2]
            else:
                if int(ql[i][1]) == 1:
                    rightans = rightans + ql[i][2]
                else:
                    leftans = ql[i][2] + leftans
        else:
            count += 1

    if count % 2 == 1:
        ans = rightans[::-1] + s[::-1] + leftans[::-1]
    else:
        ans = leftans + s + rightans

    return ans

def main():
    s = str(input())
    q = int(input())
    ql = [list(map(str , input().split())) for i in range(q)]
    print(ddd(s , q , ql))
if __name__ == '__main__':
    main()