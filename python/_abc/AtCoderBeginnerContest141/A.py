def weather_prediction(s):

    ans = {"Sunny": "Cloudy", "Cloudy": "Rainy", "Rainy": "Sunny"}

    return ans[s]
def main():
    s = str(input())
    print(weather_prediction(s))

if __name__ == '__main__':
    main()
