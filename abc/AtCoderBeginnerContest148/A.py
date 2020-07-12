def blackjack(a, a2, a3):

    return "bust" if a+a2+a3 >= 22 else "win"

def main():
    a, a2, a3 = map(int, input().split())
    print(blackjack(a, a2, a3))

if __name__ == '__main__':
    main()