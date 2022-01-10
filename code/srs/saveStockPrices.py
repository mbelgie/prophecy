import logger
import os
from datetime import datetime

debug = False
stockDataDir = "/home/michael/prophecy/prophecy/data/stocks/"
tickersFile = stockDataDir + "tickers.txt"


# creates a file for a ticker
def createFile(filename, ticker):
    logger.log("Creating stock data file for " + str(ticker), debug)
    file = open(filename, 'w')
    # file.write("Stock data file created: " + str(datetime.now()) + "\n")
    file.close()
    logger.log("Created file successfully for " + str(ticker), debug)


# checks id a file exists, if it doesn't, create it
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


# opens a file to append to
def openFileAppend(filename):
    file = open(filename, 'a')
    return file


# opens a file, reads all of the lines and then closes it
def openFileRead(filename):
    file = open(filename, 'r')
    fileData = file.readlines()
    file.close()
    return fileData


# formats the stock price by rounding it to the nearest hundredth of a cent (4 decimal places)
def formatStockPrice(price):
    return round(price, 4)


# checks if a particular point of data is already been collected
def checkDateTimeExists(fileData, dateTime):
    for line in fileData:
        if dateTime in line:
            return True


# writes data to a file if it hasn't been collected already
def writeData(file, data, fileData):
    dataList = data.values.tolist()
    numValues = len(dataList)
    for i in range(numValues):
        price = formatStockPrice(dataList[i][0])

        if checkDateTimeExists(fileData, str(data.axes[0][i])[0:19]):
            continue
        
        file.write(str(data.axes[0][i])[0:19] + " " + str(price) + "\n")


# writes new ticker to the ticker file if it doesn't exist in there already
def writeTicker(tickerExist, ticker):
    if tickerExist:
        return
    else:
        file = open(tickersFile, 'a')
        file.write(ticker + "\n")
        file.close()


# saves the ticker data
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
