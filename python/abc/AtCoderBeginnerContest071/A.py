def mealdelivery(x , a , b):

    return "A" if abs(x - a) < abs(x - b) else "B"

def main():
    x , a , b = map(int , input().split())
    print(mealdelivery(x , a , b))

if __name__ == '__main__':
    main()
