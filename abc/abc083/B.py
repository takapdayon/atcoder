
def Some_Sums(n , a , b):

    ans = 0

    for i in range(1 , n + 1):
        s = str(i)
        array = list(map(int , s))
        if a <= sum(array) and sum(array) <= b:
            ans += i

    return ans

def main():
    n , a , b = map(int , input().split())
    print(Some_Sums(n , a , b))

if __name__ == '__main__':
    main()
