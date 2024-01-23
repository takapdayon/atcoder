def algae(r, d, x):

    ans = []
    count = x
    for _ in range(1, 11):
        count = r*count - d
        ans.append(count)
    return ans

def main():
    r, d, x = map(int, input().split())
    ans = algae(r, d, x)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()