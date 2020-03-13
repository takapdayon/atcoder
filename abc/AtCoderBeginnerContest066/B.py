def ss(s):

    ans = 0
    ss = s
    flag = True

    while flag:
        ss = ss[:int(len(ss)-2)]
        if ss[:int(len(ss)/2)] == ss[(int(len(ss)/2)):]:
            ans += len(ss)
            flag = False

    return ans

def main():
    s = str(input())
    print(ss(s))

if __name__ == '__main__':
    main()