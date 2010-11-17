# -*- coding: utf-8 -*-
"""
Created on Fri Aug 06 11:51:46 2010
Configure File - 
@author: Noe
"""

# Lets create the experiment object
class experiment:
    # vars
    sample = {}
    
    preload = {}
    pulloff = {}
    retraction = {}
    homeing = {}
    
    type = 'Limit Surface'
    
    def __init__(self):
        pass
        
    def setSample(self,Name = 'dumb',backingTHK = 'dumb', area = 'dumb'):
        '''
        setSample module - This is used to set the sample dict object, the purpose
        of the sample dict obj is to store the important descriptive parameters
        
        usage:
        1    testExperiment.setSample()
        2    testExperiment.setSample(Name = 'something', backingTHK = 400, area = 1.2)
        '''
        self.sample['name'] = Name
        self.sample['backingTHK'] = backingTHK
        self.sample['area'] = area
        
    def setPreload(self,minDist = 20,stepDist = 10,maxDist = 80,velocity = 1000, angle = 45):
        self.preload['min'] = minDist
        self.preload['step'] = stepDist
        self.preload['max'] = maxDist
        self.preload['velocity'] = velocity
        self.preload['angle'] = angle
        pass
    def setPulloff(self,minAng=0,stepAng=10,maxAng=90,velocity=1000,pulloffLen = 0):
        self.pulloff['min'] = minAng
        self.pulloff['step'] = stepAng
        self.pulloff['max'] = maxAng
        self.pulloff['velocity'] = velocity
        
        if pulloffLen == 0 and 'max' in self.preload:
            pulloffLen = 2*self.preload['max']
        elif not 'max' in self.preload and pulloffLen == 0:
            print 'Error: preload information not defined and no value given to pulloffLen'
        else:
            print 'User defined pulloffLen'
            
        self.pulloff['length'] = pulloffLen
        pass
        
    def setRetract(self,velocity=1000,retractLen = 0):
        pass
    def setHomeing(self,velocity=3000):
        pass
    
    def genTrajs(self):
        pass

    def printSample(self):
        print self.sample
    def printExperiment(self):
        pass
    def printEstTime(self):
        pass
    def printAll(self):
        pass
    def screenShot(self):
        pass
    

# populate the object
wedgeLS = experiment()
wedgeLS.setSample('testSample',400,0.82)
wedgeLS.printSample()

wedgeLS.setPulloff(pulloffLen = 100)

