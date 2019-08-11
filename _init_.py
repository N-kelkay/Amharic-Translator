#Author Natnael Kelkay

# "r" Opens a file for reading only.
# "r+" Opens a file for both reading and writing.
# "rb" Opens a file for reading only in binary format.
# "rb+" Opens a file for both reading and writing in binary format.
# "w" Opens a file for writing only.
file = open("TranslateTestFile.txt", 'r+')

finalTrans = ""
lineToAddCounter = 0

file.write("\n\nHere is the final translation:\n")

for line in file:
    lineTrans = ""
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
            
            #the ha family ሀ ሁ ሂ ሃ ሄ ህ ሆ
            elif y == "ሀ":
                finalTrans += "hä"
                lineTrans += "hä"
            elif y == "ሁ":
                finalTrans += "hu"
                lineTrans += "hu"
            elif y == "ሂ":
                finalTrans += "hi"
                lineTrans += "hi"
            elif y == "ሃ":
                finalTrans += "ha"
                lineTrans += "ha"
            elif y == "ሄ":
                finalTrans += "hē"
                lineTrans += "hē"
            elif y == "ህ":
                finalTrans += "hə"
                lineTrans += "hə"
            elif y == "ሆ":
                finalTrans += "ho"
                lineTrans += "ho"
            
            #the le family   ለ ሉ ሊ ላ ሌ ል ሎ
            elif y == "ለ":
                finalTrans += "le"
                lineTrans += "le"
            elif y == "ሉ":
                finalTrans += "lu"
                lineTrans += "lu"
            elif y == "ሊ":
                finalTrans += "li"
                lineTrans += "li"
            elif y == "ላ":
                finalTrans += "la"
                lineTrans += "la"
            elif y == "ሌ":
                finalTrans += "lē"
                lineTrans += "lē"
            elif y == "ል":
                finalTrans += "lə"
                lineTrans += "lə"
            elif y == "ሎ":
                finalTrans += "lo"
                lineTrans += "lo"

            #the second ha family ሐ ሑ ሒ ሓ ሔ ሕ ሖ
            elif y == "ሐ":
                finalTrans += "hhä"
                lineTrans += "hhä"
            elif y == "ሑ":
                finalTrans += "hhu"
                lineTrans += "hhu"
            elif y == "ሒ":
                finalTrans += "hhi"
                lineTrans += "hhi"
            elif y == "ሓ":
                finalTrans += "hha"
                lineTrans += "hha"
            elif y == "ሔ":
                finalTrans += "hhē"
                lineTrans += "hhē"
            elif y == "ሕ":
                finalTrans += "hhə"
                lineTrans += "hhə"
            elif y == "ሖ":
                finalTrans += "hho"
                lineTrans += "hho"

            # the me family መ ሙ ሚ ማ ሜ ም ሞ
            elif y == "መ":
                finalTrans += "me"
                lineTrans += "me"
            elif y == "ሙ":
                finalTrans += "mu"
                lineTrans += "mu"
            elif y == "ሚ":
                finalTrans += "mi"
                lineTrans += "mi"
            elif y == "ማ":
                finalTrans += "ma"
                lineTrans += "ma"
            elif y == "ሜ":
                finalTrans += "mē"
                lineTrans += "mē"
            elif y == "ም":
                finalTrans += "mə"
                lineTrans += "mə"
            elif y == "ሞ":
                finalTrans += "mo"
                lineTrans += "mo"
            

            #the sze family ሠ ሡ ሢ ሣ ሤ ሥ ሦ
            elif y == "ሠ":
                finalTrans += "sze"
                lineTrans += "sze"
            elif y == "ሡ":
                finalTrans += "szu"
                lineTrans += "szu"
            elif y == "ሢ":
                finalTrans += "szi"
                lineTrans += "szi"
            elif y == "ሣ":
                finalTrans += "sza"
                lineTrans += "sza"
            elif y == "ሤ":
                finalTrans += "szē"
                lineTrans += "szē"
            elif y == "ሥ":
                finalTrans += "szə"
                lineTrans += "szə"
            elif y == "ሦ":
                finalTrans += "szo"
                lineTrans += "szo"
    finalTrans += " "
    file.write(lineTrans + "\n")

print(finalTrans)


#file.write(finalTrans)