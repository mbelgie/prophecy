from datetime import datetime
import matplotlib.pyplot as plt
import sys


stockDataDir = "/home/michael/prophecy/prophecy/data/stocks/"


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
    for line in lines:
        data = line.split()
        date = datetime.strptime(data[0], '%Y-%m-%d').date()
        time = data[1]
        price = data[2]

        dateList.append(date)
        timeList.append(time)
        priceList.append(price)
    
    return dateList, timeList, priceList
        

def plotData(dateList, timeList, priceList):
    ax = plt.gca()
    ax.set_yticks(ax.get_yticks()[::10])
    
    plt.plot(dateList, priceList)
    plt.show()
    

def main():
    ticker = sys.argv[1]
    lines = getData(ticker)
    dateList, timeList, priceList = populateData(lines)
    plotData(dateList, timeList, priceList)


if __name__ == '__main__':
    main()
    