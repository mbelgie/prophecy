import os
from datetime import datetime

logsDirectory = "../../data/logs/"

def createLog(debug):
    fileName = "log_file_"
    if debug == True:
        fileName += "debug_"
    logNumber = getCurrentLogNumber(debug) + 1
    fileName += str(logNumber)
    file = open(str(logsDirectory) + fileName, 'w')
    file.write("Log file created: " + str(datetime.now()) + "\n")
    file.close()

# Gets the most recent log number so that we can either open that log, or create a new one with a greater number
def getCurrentLogNumber(debug):
    logList = os.listdir(str(logsDirectory))
    logNumber = 0
    for log in logList:
        if debug == True and log.split("_")[2] == "debug":
            tempNumber = int(log.split("_")[-1])
            if tempNumber > logNumber:
                logNumber = tempNumber
        elif debug == False and (not log.split("_")[2] == "debug"):
            tempNumber = int(log.split("_")[-1])
            if tempNumber > logNumber:
                logNumber = tempNumber
    return logNumber

def openLog(debug):
    logNumber = getCurrentLogNumber(debug)
    fileName = "log_file_"
    if debug == True:
        fileName += "debug_"
    fileName += str(logNumber)
    file = open(str(logsDirectory) + str(fileName), 'a')
    return file

def log(message, debug):
    file = openLog(debug)
    file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ": " + message + '\n')
    file.close()

def error(message, debug):
    file = openLog(debug)
    file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ": ERROR - " + message + '\n')
    file.close()
