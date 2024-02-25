
def Same_Integers(abc):

    ans = 0
    abc.sort()
    count = abc[2]*3 - abc[0] - abc[1] - abc[2]

    if count % 2 == 0:
        ans = int(count / 2)
    else:
        ans = int((count + 3) // 2)

    return ans

def main():
    abc = list(map(int , input().split()))
    print(Same_Integers(abc))

if __name__ == '__main__':
    main()