def five_antennas(li, k):

    return "Yay!" if max(li)-min(li) <= k else ":("
def main():
    li = [int(input())for i in range(5)]
    k = int(input())
    print(five_antennas(li, k))

if __name__ == '__main__':
    main()