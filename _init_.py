file = open("TranslateTestFile.txt", 'r')
finalTrans = ""

for line in file:
    row = line
    rowList = list(row.split(" "))
    
    for x in rowList:
        for y in x:
            if y == "፠" or y =="፡" or y =="።" or y =="፣" or y =="፤" or y =="፥" or y =="፦" or y =="፧" or y =="፨":
                if y == "፠": # ፠ section mark
                    finalTrans += "§"
                elif y == "፡": # ፡ word separator
                    finalTrans += "|"
                elif y == "።": # ። full stop (period)
                    finalTrans += "."
                elif y == "፣": # ፣ comma
                    finalTrans += ","
                elif y == "፤": # ፤ semicolon
                    finalTrans += ";"
                elif y == "፥": # ፥ colon
                    finalTrans += ":"
                elif y == "፦": # ፦ Preface colon (introduces speech from a descriptive prefix)
                    finalTrans += ":" #Not really sure about this one...
                elif y == "፧": # ፧ question mark
                    finalTrans += "?"
                elif y == "፨": # ፨ paragraph separator 
                    finalTrans += "" #Also not sure about this one
            
            #the ha family
            elif y == "ሀ":
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
            
            #the le family   ለ ሉ ሊ ላ ሌ ል ሎ
            elif y == "ለ":
                finalTrans += "le"
            elif y == "ሉ":
                finalTrans += "lu"
            elif y == "ሊ":
                finalTrans += "li"
            elif y == "ላ":
                finalTrans += "la"
            elif y == "ሌ":
                finalTrans += "lē"
            elif y == "ል":
                finalTrans += "lə"
            elif y == "ሎ":
                finalTrans += "lo"

        finalTrans += " "

print("Here is the final translation:")
print(finalTrans)