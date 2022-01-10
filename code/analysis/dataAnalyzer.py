import sys
import pandas as pd
import matplotlib
from datetime import datetime


stockDataDir = "/home/michael/prophecy/prophecy/data/stocks/"


def analyze(ticker, dateTimeList, priceList):
    matplotlib.rcParams['figure.figsize'] = [12.0, 8.0]
    data = [[0]*2]*len(priceList)
    for i in range(len(priceList)):
        data[i][0] = dateTimeList[i]
        data[i][1] = priceList[i]

    dataSet = pd.DataFrame.from_records(data)
    dataSet.head(10)
    dataSet.plot(grid=True)


def getData(ticker):
    tickerFile = stockDataDir + str(ticker) + ".txt"
    file = open(tickerFile, 'r')
    lines = file.readlines()
    file.close()
    return lines


def populateData(lines):
    dateList = []
    timeList = []
    priceList = []
    dateTimeList = []
    for line in lines:
        data = line.split()
        date = datetime.strptime(data[0], '%Y-%m-%d').date()
        dateAndTime = datetime.strptime(data[0] + " " + data[1], "%Y-%m-%d %H:%M:%S")
        time = data[1]
        price = data[2]

        dateList.append(date)
        timeList.append(time)
        priceList.append(price)
        dateTimeList.append(dateAndTime)

    return dateList, timeList, priceList, dateTimeList


def main():
    ticker = sys.argv[1]
    lines = getData(ticker)
    dateList, timeList, priceList, dateTimeList = populateData(lines)
    analyze(ticker, dateTimeList, priceList)


if __name__ == '__main__':
    main()
    