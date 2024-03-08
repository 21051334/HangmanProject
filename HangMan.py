import random
import os

def getSingleWord():
    with open("words.txt",'r') as word:
        wordlist = word.readlines()
        impureword= wordlist[random.randint(0, len(wordlist))]
        pureword =impureword.split('\n')
        #print(pureword[0])
        return pureword[0]
        
def wordspace(l):
    for i in range (len(l)):
        print (l[i],end=" ")
    print() 
    
    
    
def hangman(tries):
    print()
    arr = [
        [" "," ","O"],
        ["\n","--"],["|"],["--","\n"],
        [" "," ","|"],
        ["\n"," ","/"],
        [" ", "\\"],
        [""]
    ] 
    for i in range(tries):
        for j in range(len(arr[i])):
            print(arr[i][j],end="")
word = getSingleWord()
#  O
#--|--
#--|--
# / \
tries = 0
chance = 8
g = set()
l =["_" for i in range(len(word))]
wordspace(l)
hangman(tries)


while tries != chance:
    if word.upper() ==''.join(l):
        print("\nWooohh!I am going to live!")
        break
    print("Guess the word?")
    guess = input("\nWhat could be the next letter?")
    os.system("cls")
    g.add(guess)
    if len(g) > 0:
        for i in g:
            print("(",end="")
            print(i,end="")
            print(")",end="")
    print("\n")  
    if guess in word:
        index = [i for i,l in enumerate(word) if l == guess]
        for i in index:
            l[i] = guess.upper() 
            
    hangman(tries)
    print()
    print()       
    wordspace(l)   
    
    
    
    if guess not in word:
        tries += 1
        hangman(tries)
        print()
        print()
        wordspace(l)
        
else:
    print("\nI trusted You...")
    print(f"The word was,{word}.")
    # os.system("cls")
#from wordfile or textfile it selects the single word  