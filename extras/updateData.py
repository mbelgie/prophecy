import sys
import datetime
import os

debug = False
stockDataDir = "/home/michael/prophecy/prophecy/data/stocks/"

tickersFile = stockDataDir + "tickers.txt"


# opens a file, reads all of the lines and then closes it
def openFileRead(filename):
    file = open(filename, 'r')
    fileData = file.readlines()
    file.close()
    return fileData


def buildCommandString(ticker):
    commandString = "python3 /home/michael/prophecy/prophecy/code/srs/getStockPrices.py -t " + str(ticker) + " -s " + str(datetime.datetime.now().strftime("%Y-%m-%d")) + " -e " + \
    str(datetime.date.today() + datetime.timedelta(days=1)) + " -i 5m"
    
    return commandString


def main():
    sys.path.insert(1, '../code/logger')
    lines = openFileRead(tickersFile)

    for ticker in lines:
        commandString = buildCommandString(ticker.strip())
        os.system(str(commandString))


if __name__ == '__main__':
    main()