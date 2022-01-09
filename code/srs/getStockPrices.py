import sys
import logger
import argParser
import saveStockPrices
from datetime import datetime, timedelta, date
import yfinance as yf


debug = False


# returns the command line arguments (not including the script name)
def getArgs():
    return sys.argv[1:]


def getData(options):
    logger.log("Getting data for " + str(options[0]) + " with options " + str(options[1:]), debug)

    if options[3] == None and options[4] == None:
        data = yf.download(options[0], start=options[1], end=options[2])
    elif options[3] != None and options[4] == None:
        data = yf.download(options[0], start=options[1], end=options[2], period=options[3])
    elif options[3] == None and options[4] != None:
        data = yf.download(options[0], start=options[1], end=options[2], interval=options[4])
    elif options[3] != None and options[4] != None:
        data = yf.download(options[0], start=options[1], end=options[2], period=options[3], interval=options[4])
    else: 
        pass

    return data


def getYear(date):
    return int(str(date)[0:4])


def getMonth(date):
    return int(str(date)[5:7])


def getDay(date):
    return int(str(date)[8:10])


def getDaysBetweenDates(startDate, endDate):
    d0 = date(getYear(startDate), getMonth(startDate), getDay(startDate))
    d1 = date(getYear(endDate), getMonth(endDate), getDay(endDate))
    delta = d1 - d0
    return int(delta.days)

# used to get the arrays for the start and end dates 
# we need an array of dates to use API calls consecutively since there is a maximum amount of data that can be transferred
# if we want data ~30 minutes apart, we can only get a months worth of data
def getDateArrays(startDate, endDate):
    dateArray = [startDate]
    tempStartDate = startDate
    tempEndDate = endDate
    
    while True:
        numDaysBetweenDates = getDaysBetweenDates(tempStartDate, endDate)
        if numDaysBetweenDates <= 30:
            break
        
        # logger.log("Too many days between dates (" + str(numDaysBetweenDates) + ") need multiple API calls", debug)
        date1 = datetime.strptime(tempStartDate, "%Y-%m-%d")
        date2 = date1 + timedelta(days=30)
        tempEndDate = str(date2.date())
        dateArray.append(tempEndDate)
        tempStartDate = tempEndDate
    
    dateArray.append(endDate)
    return dateArray


def main():
    validArgList = ["-t", "-s", "-e", "-p", "-i"]

    args = getArgs()
    # get the arguments frome the command line and organize them
    options = argParser.parseArgs(args, validArgList)
    
    if options == -1:
        logger.error("Exiting", debug)
        return -1

    # checks if stock data is up to date
    # if str((datetime.strptime(options[1], '%Y-%m-%d') + timedelta(days=1)).date()) == options[2]:
    #     logger.log("Stock data for " + str(options[0]) + " is already up to date", debug)
    #     return 0
    if options[4] == '60m':
        try:
            data = getData(options)
        except:
            return -1
        
        # options[0] is the stock ticker symbol
        saveStockPrices.save(data, options[0])

        
    else:
        dateArray = getDateArrays(options[1], options[2])
        for i in range(len(dateArray) - 1):
            options[1] = dateArray[i]
            options[2] = dateArray[i + 1]
            try:
                data = getData(options)
            except:
                return -1

            # options[0] is the stock ticker symbol
            saveStockPrices.save(data, options[0])


if __name__ == '__main__':
    main()
    