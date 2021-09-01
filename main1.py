from random import randint


class Player:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return '{}'.format(self.name,self.weight)
    
class Team:
    def __init__(self):
        self.playersList = []
        self.nameTeam = ""
    def chargePlayer(self,play):
        self.playersList.append([play])
    def showPlayers(self):
        i = 1
        for Player in self.playersList:
            print(str(i) + " - " + str(Player[0].name) + "\n")
            i=i+1
        
class PlayerList:
    def __init__(self):
        self.playersList = []
    def chargePlayer(self,play):
        self.playersList.append(play)
    def showPlayers(self):
        i = 0
        for Player in self.playersList:
            print(str(i) + " - " + str(Player.name) + "\n")
            i=i+1

menu = '''### MENÚ ###
- 1 Add Player
- 2 Add to Team
- 3 Salir'''

option = True
objectPlayersList = PlayerList()
objectTeamPlayers = Team()

while option == True :
    print(menu)
    op = int (input("Ingrese una Opción\n"))
    if op == 1:
        name = input("Nombre\n")
        weight = input("Peso\n")
        objectTransient = Player(name,weight)
        objectPlayersList.chargePlayer(objectTransient)
        print("Se agrego el jugador",objectTransient)
    elif op == 2:
        objectPlayersList.showPlayers()
        index = int (input("Ingrese el numero del player\n"))
        productTransient = objectPlayersList.playersList[index]
        objectTeamPlayers.showPlayers()
    elif op == 3:
        option=False