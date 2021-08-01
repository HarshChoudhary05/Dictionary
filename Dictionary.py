import json #file type to be imported first
from difflib import get_close_matches #for the close matches of the word from the funtion

data =  json.load(open("data.json")) #we here have loaded the data which we have in our PC

def translate(word): #defining function
    word = word.lower() #for lower case words
    if word in data:   #if word is in dataset
        return data[word]   #return the word meaning
    elif word.title() in data:  #if the word has First letter capital
        return data[word.title()] #return the meaning
    elif word.upper() in data:   #if word is all upper case
        return data[word.upper()]  #return the meaning
    elif len(get_close_matches(word , data.keys())) > 0 :  #for the word with close matches get the close one
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0]) #getting to the closest one possible
        decide = input("press y for yes  n for no")  #decide if its the same word
        if decide == "y":  #if yes
            return data[get_close_matches(word, data.keys())[0]] #return with the closest meaning
        if decide == "n": #if not
            return ("You messed up with the spelling") #you entered the wrong spelling
        else:
            return ("You have entered wrong input please enter y or n") #please check your input
    else:
        print("You messed up with the spelling") #if not then check your spelling


word = input("Enter the word you want the meaning of") #enter the word
output = translate(word) #meaning of the word
if type (output) == list: #if it has many meanings print it in a list
    for item in output: #if it has many meanings
        print (item) #print everymeaning in different line

else:
    print(output) #otherwise print the meaning
