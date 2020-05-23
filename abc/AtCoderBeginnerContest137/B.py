def one_clue(k, x):

    ans = []

    for i in range(x-k+1, x+k):
        ans.append(i)

    return ans

def main():
    k, x = map(int, input().split())
    print(*one_clue(k, x))

if __name__ == '__main__':
    main()
