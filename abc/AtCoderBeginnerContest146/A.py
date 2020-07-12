def cantwaitforholiday(s):

    days = {"SUN": 7, "MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1}
    return days[s]

def main():
    s = str(input())
    print(cantwaitforholiday(s))

if __name__ == '__main__':
    main()