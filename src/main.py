'''
Created on Aug 15, 2017

@author: Ashkan Zirakzadeh
'''
import pygame
import random
import time
import factionModule
import tileModule
import mapGeneratorModule

#This function will take a list of objects and list of weights, then return one of those objects. The weight will influence the odds of each object happening

        
        
    
length=25
height=25
tiles=[]
for l in range(length):
    tiles.append([])
    for h in range(length):
        tiles[l].append(tileModule.tile(l,h,None,(50,50,50))) #Fills with empty tiles
        


generator= mapGeneratorModule.mapGenerator(tiles, length, height)

dragon=factionModule.faction((255,0,0))
knight=factionModule.faction((200,200,200))
necro=factionModule.faction((128,0,128))
elf=factionModule.faction((0,255,0))
#Faction Colors

factions=[dragon,knight,necro,elf]

random.choice(factions).becomeAlly()

#Allocating Space to each factionModule

generator.createFactions(factions)

pygame.init()

screen=pygame.display.set_mode((length*25,height*25))

screen.fill((255,255,255))

tiles=generator.getMap()
for l in range(length):
    for h in range(height):
        tiles[l][h].render(screen)



for i in range(height):
    pygame.draw.line(screen,(0,0,0),[i*25,0],[i*25,height*25])
    
for i in range(length):
    pygame.draw.line(screen,(0,0,0),[0,i*25],[length*25,i*25])

pygame.display.flip()
    


time.sleep(1)
    