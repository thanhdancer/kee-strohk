import pandas 
import numpy
raw = pandas.read_csv('hien.txt',index_col = None,header=None)
backSpaceKeyCode =8
shiftKeyCode = 16
count = 0
flag = False
i = 0
list0 = raw[0].values.tolist()
myDict = {}

while i < len(list0):
    if list0[i] == backSpaceKeyCode:
        flag = True
        key = i
        count = count +1
        while flag == True and i < len(list0) -1:
            i = i+1
            if list0[i] == backSpaceKeyCode:
                count = count +1
            else:
                myDict[key] = count
                flag = False
                count = 0
    else:
        count = 0
    i = i+1
misDelWords = [None] * len(myDict)
misReplWords = [None] * len(myDict)
totalMistake = 0
listValue = myDict.values()
listKey = myDict.keys()
totalMistake = sum(listValue)
percentMistake = float(totalMistake)/len(list0)
indexOfMiswordArray = 0;
indexOdReplace = 0
list1 = list0
for hihi in range(len(list1)):
    if list0[hihi] == backSpaceKeyCode:
        list1[hihi] = None

# get all delete record
for iDict in range(len(myDict)):
    mis = "";
    number = 0
    index = 0
    while number < listValue[iDict] and listKey[iDict] - index >0 :
        index +=1
        if list1[listKey[iDict] - index] != None:
            number+=1
            if listKey[iDict] - index -1 >0 and list1[listKey[iDict] - index - 1] == shiftKeyCode:
                mis = mis + "_"
                mis = mis + str(shiftKeyCode)
                list1[listKey[iDict] - index - 1]  = None
            mis = mis + "_"
            mis = mis + str(list1[listKey[iDict] - index])
            list1[listKey[iDict] - index] = None
    misDelWords[indexOfMiswordArray] = mis
    indexOfMiswordArray +=1

# get all replace record
for iDict in range(len(myDict)):
    repl = "";
    number = 0
    index = 0
    while number < listValue[iDict] and listKey[iDict] + index < len(list0) :
        index +=1
        if list1[listKey[iDict] + index] != None:
            number+=1
            repl = repl = "_"
            repl = repl + str(list1[listKey[iDict] + index])
            if listKey[iDict] + index +1 <len(list0) and list1[listKey[iDict] + index] == shiftKeyCode:
                repl = repl + "_"
                repl = repl +str(list1[listKey[iDict] + index +1])
                list1[listKey[iDict] + index +1] = None
            list1[listKey[iDict] + index ] = None
    misReplWords[indexOdReplace] = repl
    indexOdReplace +=1

DataFrame = pandas.DataFrame(misDelWords, index=None)
DataFrame1 = pandas.DataFrame(misReplWords,index = None)
result = pandas.concat([DataFrame, DataFrame1], axis=1)
result.to_csv("featureMistakeWord.txt",index)