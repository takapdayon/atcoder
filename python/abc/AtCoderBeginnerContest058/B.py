def pw(o , e):
    ans = ""
    olist = list(o)
    elist = list(e)

    for i in range(len(e)):
        ans += olist[i]
        ans += elist[i]

    if len(o) != len(e):
        ans += olist[-1]

    return ans


def main():
    o = str(input())
    e = str(input())
    print(pw(o , e))

if __name__ == '__main__':
    main()
