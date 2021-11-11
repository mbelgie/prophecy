import logger
import os
from datetime import datetime

debug = False
stockDataDir = "/home/michael/prophecy/prophecy/data/stocks/"
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


def openFileAppend(filename):
    file = open(filename, 'a')
    return file


def openFileRead(filename):
    file = open(filename, 'r')
    return file.readlines()


def formatStockPrice(price):
    return round(price, 4)


def checkDateTimeExists(fileData, dateTime):
    for line in fileData:
        if dateTime in line:
            return True

def writeData(file, data, fileData):
    dataList = data.values.tolist()
    numValues = len(dataList)
    for i in range(numValues):
        price = formatStockPrice(dataList[i][0])

        if checkDateTimeExists(fileData, str(data.axes[0][i])[0:19]):
            continue
        
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
    file = openFileAppend(filename)
    logger.log("Writing data to " + str(ticker) + " (" + str(datetime.now()) + ")", debug)
    fileData = openFileRead(filename)
    writeData(file, data, fileData)
    file.close()
    logger.log("Finished writing data to " + str(ticker) + " (" + str(datetime.now()) + ")", debug)
