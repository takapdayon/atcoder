def five_dishes(li):

    ans = 0
    count = 10
    for i in li:
        ans += -(-i//10)*10
        if i%10 != 0:
            count = min(count, i%10)
    return ans-(10-count) if count != 10 else ans

def main():
    li = [int(input())for i in range(5)]
    print(five_dishes(li))

if __name__ == '__main__':
    main()