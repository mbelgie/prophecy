import sys
import logger
import argParser
import saveStockPrices
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


def main():
    validArgList = ["-t", "-s", "-e", "-p", "-i"]

    args = getArgs()
    # get the arguments frome the command line and organize them
    options = argParser.parseArgs(args, validArgList)

    if options == -1:
        logger.error("Exiting", debug)
        return -1

    if options[1] == options[2]:
        logger.log("Stock data for " + str(options[0]) + " is already up to date", debug)

    try:
        data = getData(options)
    except:
        return -1

    # options[0] is the stock ticker symbol
    saveStockPrices.save(data, options[0])

if __name__ == '__main__':
    main()
    