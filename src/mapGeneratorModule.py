'''
Created on Sep 5, 2017

@author: xd
'''
import random
import tileModule
import factionModule
class mapGenerator():

    def __init__(self,tileSet,length,height):
        self.tiles=tileSet
        self.length=length
        self.height=height
        
    def weightedRandom(self,objects,weights):
        mylist=[]
        for i in range(len(objects)):
            for t in range(weights[i]):
                mylist.append(objects[i])
        #print (mylist)
        return random.choice(mylist)
    
    #Picks a RANDOM VALID tileModule from the tiles
    def randomTile(self):
        tileModule=random.choice(random.choice(self.tiles))
        while tileModule.getFaction() != None:
            tileModule=random.choice(random.choice(self.tiles))
        return tileModule
    
    #Places a set of tiles beloning to a factionModule
    def placeTiles(self,locations,factionModule):
        #print ("I placed")
        for i in range(len(locations)):
            if locations[i].getFaction() != None:
                return False
        for i in range(len(locations)):
            locations[i].setFaction(factionModule)
     
    #Returns a Tile based on an offset and a reference point           
    def getTileOff(self,start,offset):
        x=start.getloc()[0]+offset[0]
        y=start.getloc()[1]+offset[1]
        if x>self.length or x<0:
            return None
        if y>self.height or y<0:
            return None
        #print (x,y)
        try:
            return self.tiles[x][y]
        except IndexError:
            return None
    
    def adjustWeights(self,side,weights):
        if side[0]==0 and side[1]==-1: #up
            a=0
            b=1
            c=2
            d=3
             
        elif side[0]==0 and side[1]==1: #down
            a=1
            b=0
            c=2
            d=3
        elif side[0]==-1 and side[1]==0: #left
            a=2
            b=1
            c=0
            d=3
        elif side[0]==1 and side[1]==0: #right
            a=3
            b=2
            c=1
            d=0
            
        if weights[a] >=15:
            weights[a]-=15
            weights[b]+=5
            weights[c]+=5
            weights[d]+=5
            
        elif weights[a] >=10:
    
            weights[a]-=10
            temp=weights.copy()
            temp.remove(weights[a])
            small1 = min(i for i in temp)
            temp.remove(small1)
            small2 = min(i for i in temp)
            
            weights[weights.index(small1)]+=5
            weights[weights.index(small2)]+=5
            
        elif weights[a] >=5:
    
            weights[a]-=5
            temp=weights.copy()
            temp.remove(weights[a])
            small1 = min(i for i in temp)
                       
            weights[weights.index(small1)]+=5
        else:
            print ("ERROR!")
            #print (weights)
    def createFactions(self,factions):
        
        for factionModule in factions:
            run=self.weightedRandom([1,2,3], [30,0,0]) #This is how many chunks each factionModule will have
            count=0
            while run>count:
                start=self.randomTile()
                size=self.weightedRandom([20,4,5], [305,0,0]) #The size in terms of blocks(+1) each chunk will contain
                block=[]
                block.append(start)
                searchWeight=[25,25,25,25]
                
                for t in range(size):
                    search=True
                    searchSet=[[0,-1],[0,1],[-1,0],[1,0]] # right Down Left Up directions for the NEXT block to be placed
                    tempSet=searchWeight.copy()
                    cont=True
                    blockedSides=0
                    
                    
                    while search:
                        if blockedSides<4:
                            
                            off=self.weightedRandom(searchSet, searchWeight) #Pick a direction
                            #searchSet.remove(off) #Remove that direction from the set to avoid checking multiple times
                            tempSet[searchSet.index(off)]=0
                            #print (searchWeight)
                            blockedSides+=1
                            nextTile=self.getTileOff(start,off) #Set the new tileModule to a tileModule in that direction
                            
                            if nextTile==None: #If the tileModule in the chosen offset is out of bounds, the getTileOff function will return None, This is to avoid any problems
                                #print("exited")
                                None
        
                            else:
                                if block.count(nextTile) == 0:
                                    
                                    if nextTile.getFaction() ==None: #make sure the new tileModule is an untouched tileModule
                                        #print ("found")
                                        self.adjustWeights(off,searchWeight)
                                        #print (searchWeight)
                                        #print (off)
                                        block.append(nextTile)
                                        start=nextTile
                                        search=False
                                #print (next.getloc())
                        else: #This occurs when all 4 directions are chosen, and none are valid. We then scrap work on this block and start a brand new search
                            #print ("ran out of spots")
                            search=False
                            cont=False
                if cont: #If everything has been worked out then we push the new blocks to the tiles
                    self.placeTiles(block,factionModule)
                    count+=1
    def getMap(self):
        return self.tiles