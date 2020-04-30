def double_helix(b):

    acgt = {"A":"T", "T":"A", "C":"G", "G":"C"}

    return acgt[b]
def main():
    b = str(input())
    print(double_helix(b))

if __name__ == '__main__':
    main()