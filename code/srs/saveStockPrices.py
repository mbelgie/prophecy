import logger
import os
from datetime import datetime

debug = False
stockDataDir = "../../data/stocks/"
tickersFile = stockDataDir + "tickers.txt"


def createFile(filename, ticker):
    logger.log("Creating stock data file for " + str(ticker), debug)
    file = open(filename, 'w')
    file.write("Stock data file created: " + str(datetime.now()) + "\n")
    file.close()
    logger.log("Created file successfully for " + str(ticker), debug)


def checkFileExists(filename, ticker):
    if not os.path.exists(filename):
        createFile(filename, ticker)


# checks if the ticker has already been used
def checkTickerExists(ticker):
    file = open(tickersFile, 'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        if line.strip() == ticker.strip():
            return True
    return False


def openFile(filename):
    file = open(filename, 'a')
    return file


def formatStockPrice(price):
    return round(price, 4)


def writeData(file, data):
    dataList = data.values.tolist()
    numValues = len(dataList)
    for i in range(numValues):
        price = formatStockPrice(dataList[i][0])
        file.write(str(data.axes[0][i])[0:19] + " " + str(price) + "\n")

def writeTicker(tickerExist, ticker):
    if tickerExist:
        return
    else:
        file = open(tickersFile, 'a')
        file.write(ticker + "\n")
        file.close()




def save(data, ticker):
    filename = stockDataDir + ticker + ".txt"
    tickerExist = checkTickerExists(ticker)
    writeTicker(tickerExist, ticker)
    checkFileExists(filename, ticker)
    file = openFile(filename)
    logger.log("Writing data to " + str(ticker) + " (" + str(datetime.now()) + ")", debug)
    writeData(file, data)
    file.close()
    logger.log("Finished writing data to " + str(ticker) + " (" + str(datetime.now()) + ")", debug)
