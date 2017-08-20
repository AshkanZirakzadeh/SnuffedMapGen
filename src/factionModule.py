'''
Created on Aug 20, 2017

@author: Ashkan Zirakzadeh
'''
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