def Kagami_Mochi(n , dl):

    ans = len(set(dl))

    return ans

def main():
    n = int(input())
    dl = [str(input()) for i in range(n)]
    print(Kagami_Mochi(n , dl))

if __name__ == '__main__':
    main()
