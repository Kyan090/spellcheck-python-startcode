# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import math
import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")



    # timing function
    def howLong():
        startTime = 0
        endTime = 0
        timeElapsed = endTime - startTime

    
    # Linear Search
    def linearSearch(anArray, item):
        n = 0
        while n < len(anArray):
            if anArray[n] == item:
                return n
            n += 1



    # Binary Search
    def binarySearch(anArray, item):
        li = 0
        ui = len(anArray) - 1
        while li <= ui:
            mi = math.floor((li + ui) / 2)
            mi_value = anArray[mi]
            if mi_value == item:
                return mi
            elif item < mi_value:
                ui = mi - 1
            elif item > mi_value:
                li = mi + 1

        return None


    # Main Menu loop
    loop = True
    while loop == True:
        print("*** MAIN MENU ***")
        print("1. Spell Check a Word (linear Search)")
        print("2. Spell Check a Word (Binary Shearch)")
        print("3. Spell Check Alice In Wonderland (linear Search)")
        print("4. Spell Check Alice In Wonderland (Binary Search)")
        print("5. Exit")
        option = int(input("Enter Option #: "))
   

        if option == 1:
           word = input("Please enter a Word to Search: ")
           x = linearSearch(dictionary, word)
           print("Linear Search Starting...")
           if x == None:
               print("%s is NOT in the dictionary" % word) 
           else:
               print("%s is IN the Dictionary at Position %s" %(word, x))
        
        
        
        elif option == 2:
            word = input("Please enter a Word to Search: ")
            x = binarySearch(dictionary, word)
            print("Binary Search Starting...")
            if x == None:
               print("%s is NOT in the dictionary" % word) 
            else:
               print("%s is IN the Dictionary at Position %s" %(word, x))

        
        
        elif option == 3:
            notInDict = 0
            x = linearSearch(dictionary,aliceWords[20])
            print(x)
            print("Number of words not Found In Dictionary: %s" % notInDict)

        
        
        elif option == 4:
            print("4")
        
        
        
        elif option == 5:
            loop = False

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()


