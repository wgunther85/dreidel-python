import random
import math

class Player:
    def __init__(self):
        self.name = ""
        self.tokens = 20
    
    # assign name to player
    def getName(self, incomingname):
        self.name = incomingname
        return self.name
    
    #Lose one token from pocket and add it to the pot
    def lostToken(self, incomingpot):
        self.tokens -= 1
        incomingpot += 1
        return incomingpot

    # Print name and total tokens
    def printInfo(self):
        print(self.name, "has", self.tokens, "tokens")
      
    #roll the die
    def roll(self, incomingpot):
        self.result = random.randint(1, 4)
        dreidel = ''

        #if NUN is rolled
        if self.result == 1:
            dreidel = 'NUN'
            print(self.name, "'s turn: Dreidel falls on... NUN: nothing happnes")

        #if Gimmel is rolled
        elif self.result == 2:
            dreidel = 'GIMMEL'
            print(self.name, "'s turn: Dreidel falls on... GIMMEL: you get the pot")
            self.tokens += incomingpot
            incomingpot = 0
        
        #if Hey is rolled
        elif self.result == 3:
            dreidel = 'HEY'
            print(self.name, "'s turn: Dreidel falls on... HEY: you receive half the pot")
            self.change = math.ceil(incomingpot/2)
            self.tokens += self.change
            incomingpot = incomingpot//2
        
        #if Shin is rolled
        elif self.result == 4:
            dreidel = 'SHIN'
            print(self.name, "'s turn: Dreidel falls on... SHIN: lose a token")
            self.tokens -= 1
            incomingpot += 1

        return dreidel, incomingpot

#Main Program
print("Welcome to the Dreidel Game!")
pot = 0

#create instances
p1 = Player()
p2 = Player()

#Create players names'
name1 = input("Enter Player 1 name: \n")
name2 = input("Enter Player 2 name: \n")
print()

p1.getName(name1)
p2.getName(name2)

while True:
    #Ante up the pot
    print("Ante Up: Everyone put a token in the pot")

    pot = p1.lostToken(pot)
    pot = p2.lostToken(pot)    

    p1.printInfo()
    p2.printInfo()
    
    print("Pot tokens:", pot)

    #Begin Turn 1 with dreidel roll
    dreidel, pot = p1.roll(pot)
    p1.printInfo()

    if dreidel == 'GIMMEL':
        print("//Ante up again after Gimmel")
        pot = p1.lostToken(pot)
        pot = p2.lostToken(pot)
        
    print("Pot tokens:", pot)

    #Begin Turn 2 with dreidel roll
    dreidel, pot = p2.roll(pot)
    p2.printInfo()
    
    #Continue?
    while True:
        try: 
            play = input("Continue: (y/n)\n")

            if play.lower() != 'y' and play.lower() != 'n':
                raise ValueError('Please enter "y" or "n".')
            
            break

        except ValueError as err:
            print(err)
            print()

    if play == "n":
        break
    
    print()

print('Game Over')


    