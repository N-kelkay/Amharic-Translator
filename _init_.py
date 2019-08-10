import re

file = open("TranslateTestFile.txt", 'r')
finalTrans = ""

for line in file:
    row = line
    rowList = list(row.split(" "))
    
    for x in rowList:
        for y in x:
            if y == "አ":
                finalTrans += "ah"
            if y == "በ":
                finalTrans += "be"
            if y == "ሶ":
                finalTrans += "so"
            if y == "ላ":
                finalTrans += "la"
        finalTrans += " "

print("Here is the final translation:")
print(finalTrans)