"""
Authors: Shanielle Hall and Alyn Tetteh
ID: snh325, aet78
Date: 09/25/2025
Description: Spellchecks to see if a word from a file is a part of the english vocabulary
"""

"""
import the spellchecker class so that it is available for use in this file
"""
import spellchecker

"""
repeatedly asks the user for a file until it gets a file that exists.
Reads the file and returns the content of the file
"""
def get_file():
    while True:
        filename = input("Enter the name of the file to read: ")
        try:
            file = open(filename, "r")
            return file
        except FileNotFoundError:
            print("Could not open file.")
            
"""
main script of the file
"""

def main():
    print("Welcome to Text File Spellchecker.")
    file = get_file()
    
    correctWords = 0
    incorrectWords = 0
    lineNumber = 1
    
    #instantiate the file
    FileChecker = spellchecker.Spellchecker("english_words.txt")
    
    #reads every line in the file, splitting it. for each word the file, checks if the word is part of the english_words.txt
    for line in file:
        words = line.split()
        for word in words:
            #if the word is not apart of the file, prints as a spelling error, and increments incorrectWords by 1
            if not FileChecker.check(word):
                incorrectWords += 1
                print("Possible Spelling Error on line ", lineNumber, word)
            #if the word is apart of the file, increments correctWords by 1
            else:
                correctWords += 1
        #moves the lineNumber up by one
        lineNumber+=1
        
    #calculates the passing percentage    
    passingPercentage = (correctWords)/(correctWords + incorrectWords)
    
    print(f"{correctWords:,}", "words passed spell checker.")
    print(f"{incorrectWords:,}", "words failed spell checker.")
    print(f"{passingPercentage:.2%} of words passed.")
    
    file.close()


#runs the file
if __name__ == "__main__":
    main()
