def Task(al):

    return max(al) - min(al)

def main():
    al = list(map(int , input().split()))
    print(Task(al))

if __name__ == '__main__':
    main()