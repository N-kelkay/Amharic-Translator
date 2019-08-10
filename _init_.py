file = open("TranslateTestFile.txt", 'r')
finalTrans = ""

for line in file:
    row = line
    rowList = list(row.split(" "))
    
    for x in rowList:
        for y in x:
            if y == "ሀ":
                finalTrans += "hä"
            elif y == "ሁ":
                finalTrans += "hu"
            elif y == "ሂ":
                finalTrans += "hi"
            elif y == "ሃ":
                finalTrans += "ha"
            elif y == "ሄ":
                finalTrans += "hē"
            elif y == "ህ":
                finalTrans += "hə"
            elif y == "ሆ":
                finalTrans += "ho"
        finalTrans += " "

print("Here is the final translation:")
print(finalTrans)