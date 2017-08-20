'''
Created on Aug 15, 2017

@author: Ashkan Zirakzadeh
'''
import pygame
import random
import time

class tile:
    def __init__(self,x,y,faction,visual):
        self.x=x
        self.y=y
        self.faction=faction
        self.visual=visual
        self.default=True
    def getloc(self):
        return [self.x,self.y]
    def render(self,screen):
        if self.faction!=None:
            pygame.draw.rect(screen,self.faction.getColor(),(self.x*25,self.y*25,25,25))
            if self.faction.isAlly():
                pygame.draw.rect(screen,(255,255,50),(self.x*25,self.y*25,10,10))
                
        else:
            pygame.draw.rect(screen,self.visual,(self.x*25,self.y*25,25,25))
            
    def setFaction(self,fact):
        self.faction=fact
    def setDefault(self):
        self.default=False
    def isDefault(self):
        return self.default

class faction:
    def __init__(self,color):
        self.area=None
        self.bonus=None
        self.ally=False
        self.color=color
    def becomeAlly(self):
        self.ally=True
    def isAlly(self):
        return self.ally
    def getColor(self):
        return self.color


#This function will take a list of objects and list of weights, then return one of those objects. The weight will influence the odds of each object happening
def weightedRandom(objects,weights):
    mylist=[]
    for i in range(len(objects)):
        for t in range(weights[i]):
            mylist.append(objects[i])
    #print (mylist)
    return random.choice(mylist)

#Picks a RANDOM VALID tile from the tiles
def randomTile():
    tile=random.choice(random.choice(tiles))
    while not tile.isDefault():
        tile=random.choice(random.choice(tiles))
    return tile

#Places a set of tiles beloning to a faction
def placeTiles(locations,faction):
    #print ("I placed")
    for i in range(len(locations)):
        if not locations[i].isDefault():
            return False
    for i in range(len(locations)):
        locations[i].setFaction(faction)
        locations[i].setDefault()
 
#Returns a Tile based on an offset and a reference point           
def getTileOff(start,offset):
    x=start.getloc()[0]+offset[0]
    y=start.getloc()[1]+offset[1]
    if x>10 or x<0:
        return None
    if y>10 or y<0:
        return None
    #print (x,y)
    try:
        return tiles[x][y]
    except IndexError:
        return None
    
    
length=10
height=10
tiles=[]
for l in range(length):
    tiles.append([])
    for h in range(length):
        tiles[l].append(tile(l,h,None,(50,50,50))) #Fills with empty tiles
        



dragon=faction((255,0,0))
knight=faction((200,200,200))
necro=faction((128,0,128))
elf=faction((0,255,0))
#Faction Colors

factions=[dragon,knight,necro,elf]

random.choice(factions).becomeAlly()

#Allocating Space to each faction

for faction in factions:
    run=weightedRandom([1,2,3], [30,0,0]) #This is how many chunks each faction will have
    count=0
    while run>count:
        start=randomTile()
        size=weightedRandom([3,4,5], [35,35,35]) #The size in terms of blocks(+1) each chunk will contain
        block=[]
        block.append(start)
        for t in range(size):
            search=True
            searchSet=[[1,0],[0,1],[-1,0],[0,-1]] # right Down Left Up directions for the NEXT block to be placed
            cont=True
            while search:
                if len(searchSet)>=1:
                    off=random.choice(searchSet) #Pick a direction
                    searchSet.remove(off) #Remove that direction from the set to avoid checking multiple times
                    nextTile=getTileOff(start,off) #Set the new tile to a tile in that direction
                    
                    if nextTile==None: #If the tile in the chosen offset is out of bounds, the getTileOff function will return None, This is to avoid any problems
                        #print("exited")
                        None

                    else:
                        if block.count(nextTile) == 0:
                            
                            if nextTile.isDefault(): #make sure the new tile is an untouched tile
                                #print ("found")
                                block.append(nextTile)
                                start=nextTile
                                search=False
                        #print (next.getloc())
                else: #This occurs when all 4 directions are chosen, and none are valid. We then scrap work on this block and start a brand new search
                    #print ("ran out of spots")
                    search=False
                    cont=False
        if cont: #If everything has been worked out then we push the new blocks to the tiles
            placeTiles(block,faction)
            count+=1
                
                
            
        


pygame.init()

screen=pygame.display.set_mode((length*25,height*25))

screen.fill((255,255,255))

for l in range(length):
    for h in range(height):
        tiles[l][h].render(screen)



for i in range(height):
    pygame.draw.line(screen,(0,0,0),[i*25,0],[i*25,height*25])
    
for i in range(length):
    pygame.draw.line(screen,(0,0,0),[0,i*25],[length*25,i*25])

pygame.display.flip()
    


time.sleep(1)
    