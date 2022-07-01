#©Jetoson 2022inspired and taught by Bobby Stemming from decoding
#on freecodecamp.org youtube channel

import requests
import datetime
import time
import emoji

class APICall:
    '''A base class for API call'''
    def call(self, method, api_Url):
        if method.lower() == "get":
            r = requests.get(api_Url)

        match r.status_code:
            case 200 | 201 | 202:
                return r.json()["value"] 
            case _:
                raise TypeError("API error")
                

class ChuckNorris(APICall):
    '''Chuck Norris API'''
    url = "https://api.chucknorris.io/jokes/random?category="
    categories = ["animal","dev","food","history","money","political","science","sport","travel"]

    def __init__(self, category):
        self.category = category
        if not self.category in self.categories:
            raise TypeError("category options ['animal', 'dev'. 'food', 'history', 'money', 'political', 'science', 'sport', 'travel']")
    
    def get(self):
        api_url = f'{self.url}{self.category}'
        return self.call("GET", api_url)


def genere():   #Genere menu
    print("[1] animal")
    print("[2] dev")
    print("[3] food") 
    print("[4] money")
    print("[5] history")
    print("[6] political")
    print("[7] science")
    print("[8] sport")
    print("[9] travel")


'''Day-mentioning Salutation'''
today = datetime.datetime.now()
print("Hello there, Happy", end = ' ')
print(today.strftime("%A"))
time.sleep(1.4) #wait for seconds for UI/UX

'''Introducing smiley'''
print("I'm smiley", end = "")
print("\U0001f600", end = " ")
print(" I will generate random Chuck Norris jokes for you")
time.sleep(1.4)   #wait for seconds for UI/UX

print(" ")
print("*******************")
print("*** Genere Menu ***")
print("*******************")
time.sleep(1.4)   #wait for seconds for UI/UX 
print(" ")

genere()
choice = int(input("Enter your genere of choice: "))
while choice != 0 & choice < 10:
    match choice:
        case 1:
            choice = "animal"
        case 2:
            choice = "dev"
        case 3:
            choice = "food" 
        case 4:
            choice = "money" 
        case 5:
            choice = "history"
        case 6:
            choice = "political"
        case 7:
            choice = "science"
        case 8:
            choice = "sport"
        case 9:
            choice = "travel"
        case _:
            print("Choose generes from 1 - 9 as on the menu and 0 to exit")

 
    c = ChuckNorris(choice)
    temp = len(c.get())
    print(" ")
    for i in range(temp):
        print("#", end = "")
    print("##")

    print(c.get())

    for i in range (temp):
        print("#", end ="")
    print("##")
    print(" ")
    genere()
    choice = int(input("Enter your genere of choice: "))

print("Have a nice day, don't forget to smile", end = "")
print("\U0001f60A")
