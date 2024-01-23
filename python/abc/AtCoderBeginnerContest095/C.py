def HalfPizza(a , b , c , x , y):

    ans = 0

    if a + b < c * 2:
        ans += a * x + b * y
    else:
        ans += c * 2 * min(x, y)
        ans += min(abs(x - y) * a if x > y else abs(x - y) * b , c * 2 * abs(x - y))

    return ans

def main():
    a , b , c , x , y = map(int, input().split())
    print(HalfPizza(a , b , c , x , y))

if __name__ == '__main__':
    main()