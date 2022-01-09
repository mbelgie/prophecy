import sys
import logger
import argParser
import saveStockPrices
from datetime import datetime, timedelta
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


# used to get the arrays for the start and end dates 
# we need an array of dates to use API calls consecutively since there is a maximum amount of data that can be transferred
# if we want data ~30 minutes apart, we can only get a months worth of data
def getDateArrays(startDate, endDate):
    pass


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

    try:
        data = getData(options)
    except:
        return -1

    # options[0] is the stock ticker symbol
    saveStockPrices.save(data, options[0])

if __name__ == '__main__':
    main()
    