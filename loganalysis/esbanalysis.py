print ("hello esb logs")



def readSimCodes() :
    print("readSimCodes")
    simCodes = {}
    simfile = "2"
    f = open(simfile, "rb")
    lineiter = iter(f)
    for line in lineiter:
        strline = str(line)
        pos = strline.find("VehicleName")
        if  pos>= 0:
            # print(strline)

            substr = strline[pos+15:]
            pos2 = substr.find("\"")
            ss = substr[:pos2]
            simCodes[ss] = ss

            # print(substr)
            # print(ss)
            # print(pos2)
    return simCodes



def readLog(logfile):
    logCodes = {}
    f = open(logfile, "rb")
    lineiter = iter(f)
    for line in lineiter:
        strline = str(line)
        # print(strline)
        pos = strline.find("simCode")
        if pos >= 0:
            # print(strline)
            substr = strline[pos + 10:]
            pos2 = substr.find("\"")
            ss = substr[:pos2]
            logCodes[ss] = ss

            # print(substr)
            # print(ss)
            # print(pos2)

    return logCodes


def parsingLog(logfile, simCodes):
    print(logfile)
    logCodes = readLog(logfile)
    for k in logCodes:
        # print(k)
        haskey = k in simCodes
        if not haskey:
            print(k)

simCodes = readSimCodes()
# print(ss)
logfile = "esbClient-2022-09-22.27"

# logCodes = readLog(logfile)
# print(logCodes)

parsingLog(logfile,simCodes)

# for k in logCodes:
#     haskey = k in simCodes
#     if not haskey:
#         print(k)


dirpath = "C:/work/temp/esbLogs"
#
import os
#
g = os.walk(dirpath)
for path,dir_list,file_list in g:
    print(path)
    print(dir_list)
    print(file_list)
    for file_name in file_list:
        logpathname = os.path.join(path, file_name)
        # print(os.path.join(path, file_name) )
        parsingLog(logpathname, simCodes)


