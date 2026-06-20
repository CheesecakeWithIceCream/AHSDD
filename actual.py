import random
from dataclasses import dataclass
@dataclass
class square():
    position : int = 0
    player : str = ''
    pointer : int = 0

def displayBoard(gameboard):
    for row in range(len(gameboard)):
        print(str(gameboard[row].position) + ', ', end= " ")
    print()

def initPosition(gameboard):
    pointers = {5: 3, 12: -2, 16: 4, 23: -3, 27: -2, 32: 5, 36: -4, 45: 3, 48: -2}
    for index in range(len(gameboard)):                
        gameboard[index].position = index + 1    
        gameboard[index].pointer = pointers.get(index+1,0)      
    return gameboard

def diceroll(gameboard):
    roll=random.randint(1,6)
    for index in range(50):
        if gameboard[index].player !="":
            newPos = index +roll
            if newPos >49:
                print("Roll too high, stay at square", gameboard[index].position)
                return False
            
            print("Player moved from",gameboard[index].position, "to", gameboard[newPos].position)
            
            gameboard[newPos].player = "red"
            gameboard[index].player = ""
        
            pointerMove = gameboard[newPos].pointer
            if pointerMove !=0:
                print("The pointer has moved you", pointerMove, "squares")
                gameboard[newPos].player = ""
                newPos += pointerMove
                gameboard[newPos].player = "red"
                print("Now at", gameboard[newPos].position)

            if newPos ==49:
                print("Player has won")
                return True
            return False
    return False

gameboard = [square() for index in range(50)]     
gameboard[0].player = "red"    

displayBoard(gameboard)
gameboard = initPosition(gameboard) 
won = False
while not won:
    displayBoard(gameboard)
    won = diceroll(gameboard)
