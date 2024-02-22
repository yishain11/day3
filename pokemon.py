import random 
Types = {'fire':{'fire':1,'water':2,'earth':1,'wind':2},
         'water':{'fire':1,'water':1,'earth':2,'wind':1},
         'earth':{'fire':2,'water':1,'earth':1,'wind':2},
         'wind':{'fire':1,'water':2,'earth':1,'wind':1}}


#######################################################
#############        Pokemon       ####################
#######################################################
class Pokemon:
    def __init__(self, name, level, strength, speed, type, life):
         self.name=name
         self.level=level
         self.strength=strength
         self.speed=speed
         self.type=type
         self.life=life

    def attack(self,type2):
         return Types[self.type][type2]* (random.randint(1,20) + self.strength)
    
    def isDead(self):
         return self.life <= 0
    

#player A pokemons
a1 = Pokemon('a1', 1, 5, 2, 'fire', 120)
a2 = Pokemon('a2', 2, 8, 4, 'wind', 120)
a3 = Pokemon('a3', 3, 9, 1, 'earth', 120)
a4 = Pokemon('a4', 4, 4, 3, 'fire', 120)
a5 = Pokemon('a5', 5, 7, 5, 'water', 120)

#player B pokemons
b1 = Pokemon('b1', 1, 5, 2, 'fire', 120)
b2 = Pokemon('b2', 2, 8, 4, 'wind', 120)
b3 = Pokemon('b3', 3, 9, 1, 'water', 120)
b4 = Pokemon('b4', 4, 4, 3, 'wind', 120)
b5 = Pokemon('b5', 5, 7, 5, 'earth', 120)


#######################################################
#############        Player       #####################
#######################################################

class Player:
    def __init__(self,dict,currPokemon):
         self.dict = dict
         self.currPokemon = currPokemon
    def getCurrPokemon(self):
         return self.dict[self.currPokemon]
         
    def updatePokemon(self):
        for i in self.dict:
            if self.dict[i].life > 0:
                self.currPokemon = i
                return i
        return -1
        
           
playerA = Player({ 1:a1,
            2:a2,
            3:a3,
            4:a4,
            5:a5
           },0)

playerB = Player({ 1:b1,
            2:b2,
            3:b3,
            4:b4,
            5:b5
           },0)

players = {1:playerA , 2: playerB}



    
#######################################################
#############        Game       #######################
#######################################################

def gameOver(winner):
     print("Game Over")
     print('The winner is player {} and the loser is player {} '.format(winner, 3 - winner))


     

def gameStarts(firstPlayer):
     currentPlayer = firstPlayer
     while(True):
          oponnentPlayer = 3 - currentPlayer
          attcackPokemon = players[currentPlayer].getCurrPokemon()
          oponnentPokemon = players[oponnentPlayer].getCurrPokemon()
          #attack
          aName = attcackPokemon.name
          oName = oponnentPokemon.name
          damage = attcackPokemon.attack(oponnentPokemon.type)
          oponnentPokemon.life = oponnentPokemon.life - damage
          print('{} attacks {}, deals {} damage, now {} has {} amount of life after the attack'.
                format(aName, oName,damage,oName,oponnentPokemon.life))
          if oponnentPokemon.isDead():
            result = players[oponnentPlayer].updatePokemon()
            print('{} is dead!'.format(oponnentPokemon.name))
            newPokemon = players[oponnentPlayer].getCurrPokemon()
            print('{} has joined the fight!'.format(newPokemon.name))
            if result == -1:
                gameOver(currentPlayer)
                break
          currentPlayer = 3 - currentPlayer
     


               
 
#######################################################
#############        GameInit       ###################
#######################################################    

     
#starting the game, each player selects a pokemon randomly:
A = random.randint(1,5)
B = random.randint(1,5)
playerA.currPokemon = A
playerB.currPokemon = B
pokemonA = playerA.getCurrPokemon()
pokemonB = playerB.getCurrPokemon()

#check which pokemon has a higher score:

randomNumA = random.randint(1,20)
randomNumB = random.randint(1,20)

playerAScore = pokemonA.speed + randomNumA
playerBScore = pokemonB.speed + randomNumB

if playerAScore >= playerBScore:
     gameStarts(1)
          
else:
     gameStarts(2)


