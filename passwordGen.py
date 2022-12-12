import string
import random

def passwordGen():
    stringOne = string.ascii_uppercase
    stringTwo = string.ascii_lowercase
    stringThree = string.digits 
    stringFour = string.punctuation
    
    passLen = int(input("Enter the password length you want to generate: "))
    passList = []
    passList.extend(list(stringOne))
    passList.extend(list(stringTwo))
    passList.extend(list(stringThree))
    passList.extend(list(stringFour))
    
    
    random.shuffle(passList)
    pas = ("".join(passList[0: passLen]))
    print(pas)

passwordGen()

