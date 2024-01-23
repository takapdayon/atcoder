def ringo(d , n):

    return n * 100**d if n != 100 else 101 * 100**d

def main():
    d , n = map(int , input().split())
    print(ringo(d , n))

if __name__ == '__main__':
    main()