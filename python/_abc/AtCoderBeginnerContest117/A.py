def Entrance_Examination(t, x):

    return t/x
def main():
    t, x = map(int, input().split())
    print(Entrance_Examination(t, x))

if __name__ == '__main__':
    main()