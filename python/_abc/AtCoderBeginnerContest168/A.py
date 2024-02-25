def a168(n):

    ans = ""
    aaa = n[-1]
    hon = [2,4,5,7,9]
    pon = [0,1,6,8]
    bon = [3]

    if int(aaa) in hon:
        ans = "hon"
    elif int(aaa) in pon:
        ans = "pon"
    else:
        ans = "bon"

    return ans

def main():
    n = list(str(input()))
    print(a168(n))

if __name__ == '__main__':
    main()