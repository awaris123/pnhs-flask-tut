import json
import random

class Hero(object):
    
    origins = ["parents shot outside of a theater", "Uncle died, then bit by spider", "captured by terrorists, built suit to escape", \
                    "Injected with super-soldier serum",  "crashed onto earth in escape pod", "struck by ligtinng"]

    staticPowerList = ["super speed", "super strength", "x-ray vision", "web-sliniging", "genius billionaire", "flight", "telekenisis", \
                            "laser eyes", "ice powers", "teleportation", "telepathy", "shape-shifter", "invisibility", "phase-shifting"]
    
    Counter = 0

    @staticmethod
    def genPowers():
        length = len(Hero.staticPowerList)
        idx = random.randint(0, length-1)
        return Hero.staticPowerList[idx]
    
    @staticmethod
    def genOrigin():
        length = len(Hero.origins)
        idx = random.randint(0, length-1)
        return Hero.origins[idx]


    def __init__(self, name):
        self._name = name
        self._power = Hero.genPowers()
        self._origin = Hero.genOrigin()
        self._uid = Hero.Counter
        Hero.Counter += 1

    def getName(self):
        return self._name
    
    def setName(self, newName):
        self._name = newName
    
    def getPower(self):
        return self._power

    def getOrigin(self):
        return self._origin
    
    def getUid(self):
        return self._uid
    
    def toDict(self):
        ht = {
            "name" : self.getName(),
            "power":self.getPower(),
            "origin":self.getOrigin(),
            "uid":self.getUid()
        }
        return ht
    
    def json(self):
        return json.dumps(self.toDict())
    
  

        
