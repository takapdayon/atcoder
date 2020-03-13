def answercount(n , s):

    not10min = 101
    for i in range(n):
        if int(s[i]) % 10 != 0:
            not10min = min(not10min , s[i])

    if not10min == 101:
        return 0

    if int(sum(s)) % 10 == 0:
        return (int(sum(s)) - not10min)

    return int(sum(s))

def main():
    n = int(input())
    s = [int(input()) for i in range(n)]
    print(answercount(n , s))

if __name__ == '__main__':
    main()
