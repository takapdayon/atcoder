def kansu(i):

    s = list(str(i))

    smozi = ""
    if abs(int(s[-1]) - int(s[-2])) < 2:
        return 0
    else:
        s[-2] = str(int(s[-2]) + 1)
        flag = True
        while flag:
            a = -2
            if abs(a) == len(s) or abs(int(s[a - 1]) - int(s[a])) < 2:
                if abs(a) == len(s):
                    a += 1
                s[a - 1] = str(int(s[a - 1]) + 1)
                flag == False
                w = 1
                for i in range(a + 1 , -2):
                    s[i] = str(int(s[a - 1]) - w)
                    w += 1
            else:
                a -= 1

        for i in range(len(s)):
            smozi += str(s[i])

        return int(smozi)

def d161(k):

    ans = 10
    count = 10

    if k < 10:
        return k

    while count < k:
        ans += 1
        reans = kansu(ans)

        if reans == 0:
            count += 1
        else:
            ans = reans

    return ans

def main():
    k = int(input())
    print(d161(k))
if __name__ == '__main__':
    main()