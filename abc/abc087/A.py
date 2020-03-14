
def Buying_Sweeets(x , a , b):

    return (x - a) % b

def main():
    x = int(input())
    a = int(input())
    b = int(input())
    print(Buying_Sweeets(x , a , b))

if __name__ == '__main__':
    main()
