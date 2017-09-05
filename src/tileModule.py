'''
Created on Aug 20, 2017

@author: Ashkan Zirakzadeh
'''
import pygame

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
    def getFaction(self):
        return self.faction