import numpy
def Resistors(n , al):

    count = 0

    for i in range(n):
        count += 1/al[i]

    return numpy.reciprocal(count)

def main():
    n = int(input())
    al = list(map(int , input().split()))
    print(Resistors(n , al))

if __name__ == '__main__':
    main()