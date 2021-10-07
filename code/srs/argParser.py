import logger

# variables for debugging and verbose statements
debug = False
verbose = False


# parses the users arguments
def parseArgs(args, validArgList):

    options = [None]*len(validArgList)
    for x in range(0, len(args), 2):
        options = checkValidArg(args[x], args[x+1], options, validArgList)
    
    if options[0] == None:
        logger.error("No ticker symbol was given", debug)
        return -1

    return options


# checks if a pair of arguments is valid
def checkValidArg(arg1, arg2, options, validArgList):

    if arg1 not in validArgList:
        print(str(arg1) + " is not a valid option")
        logger.error("Invalid argument (" + str(arg1) + ")", debug)
        printHelp()
        return -1
    
    # assigns the proper argument to its right place in the options list
    options[validArgList.index(arg1)] = arg2
    return options
    



def printHelp():
    print("\nProper usage:")
    print("-t       ticker name (e.g. MSFT)")
    print("-s       start date - YYYY-MM-DD (e.g. 2021-01-01)")
    print("-e       end date - YYYY-MM-DD (e.g. 2021-02-01)")
    print("-p       period - use instead of start/end (e.g. 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max)")
    print("-i       interval - intraday if period < 60 days (e.g. 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo)")
    print("\n")