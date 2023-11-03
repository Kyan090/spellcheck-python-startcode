
# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import math
import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    
    # Linear Search
    def linearSearch(anArray, item):
        for i in range(len(anArray)):
            if anArray[i] == item:
                return i
        return -1    
        


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

        return -1


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
           x = linearSearch(dictionary, word.lower())
           start = time.time()
           print("Linear Search Starting...")
           if x == -1:
               print("%s is NOT in the dictionary" % word) 
           else:
               print("%s is IN the Dictionary at Position %s" %(word, x))
           end = time.time()
           print(end - start)

        
        
        elif option == 2:
            word = input("Please enter a Word to Search: ")
            x = binarySearch(dictionary, word.lower())
            start = time.time()
            print("Binary Search Starting...")
            if x == -1:
               print("%s is NOT in the dictionary" % word) 
            else:
               print("%s is IN the Dictionary at Position %s" %(word, x))
            end = time.time()
            print(end - start)

        
         
        elif option == 3:
            notInDict = 0
            start = time.time()
            for i in range(len(aliceWords)):
                x = linearSearch(dictionary, aliceWords[i].lower())
                if x == -1:
                    notInDict += 1
                end = time.time()
            print("number of words not found in dictionary: %s" % notInDict)
            print(end - start)

 



            
        elif option == 4:
            notInDict = 0
            start = time.time()
            for i in range(len(aliceWords)):
                x = binarySearch(dictionary, aliceWords[i].lower())
                if x == -1:
                    notInDict += 1
                end = time.time()
            print("number of words not found in dictionary: %s" % notInDict)         
            print(end - start)
        
        
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