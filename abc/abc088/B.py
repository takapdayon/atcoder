
def Card_Game(n , al):

    al.sort(reverse=True)

    Alice = al[0::2]
    Bob = al[1::2]

    ans = sum(Alice) - sum(Bob)

    return ans

def main():
    n = int(input())
    al = list(map(int , input().split()))
    print(Card_Game(n , al))

if __name__ == '__main__':
    main()
