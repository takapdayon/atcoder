def nextPrime(x):

    for i in range(x, x*2):
        a = 0
        for w in range(2, i):
            if i%w ==0:
                break
            else:
                a = w
        if i == a + 1:
            return i

def main():
    x = int(input())
    print(nextPrime(x))

if __name__ == '__main__':
    main()