import math
import matplotlib.pyplot as plt
import random as rd
import numpy as npy

#ISLAND
# resources: Trees, Bushes
# prey: Rabbits
# predator: Fox
# Decomposers: Mushrooms

# а) фактори зовнішнього впливу:
# — кліматичні зміни (температура, опали тощо);
# 6) внутрішні фактори:
# — конкуренція;
# — паразитизм;
# — хижацтво;
# — захворюваність та її поширення;

# Predation: Simulate hunting and predation patterns based on population densities.
# Resource competition
# Reproduction
# Diseases
# DLH = demolish likelyhood

AREA = 30
BOUNDARIES = 365
temperature = {"Wet" : 19, "Dry" : 40}
timestep = 0.01
end = 104
koef = 0.98541

t = npy.arange(0,end,timestep)

class DLH:
    climate: int # num variants
    disease: int
    predation: int 
    resource: int
    def __init__(self, climate, disease, predation, resource):
        self.climate = climate
        self.disease = disease
        self.predation = predation
        self.resource = resource

class treeSpecies:
    population: int = 0
    maxAge: int
    DfertilityRates: float
    curFrates: float
    dlh : DLH
    resources: float = 1.000007
    popArray = []
    
    def __init__(self, population: int = 130000, maxAge: int = 200, fertilityRates: float = 1.0015): # per week
        self.population = population
        self.maxAge = maxAge
        self.DfertilityRates = fertilityRates
        self.curFrates = fertilityRates
        self.popArray.append(self.population)
        
    def demolish(self):
        if (rd.randrange(int(self.dlh.climate)) == 1):
            self.population-=1
        if (rd.randrange(int(self.dlh.disease)) == 1):
            self.population-=3
        if (rd.randrange(int(self.dlh.predation)) == 1):
            self.population-=1
        if (rd.randrange(int(self.dlh.resource)) == 1):
            self.population-=1
    def setFertility(self, curSeason):
        if curSeason == "Wet":
            self.curFrates = self.DfertilityRates + 0.00316
        else: self.curFrates = self.DfertilityRates + 0.0031
        
    def update(self, curSeason):
        self.dlh = DLH(int(temperature[curSeason]/10), 10*temperature[curSeason]/10, 10000, 50)
        self.setFertility(curSeason)
        self.demolish()
        self.population*=self.curFrates*(timestep+koef)
        self.popArray.append(self.population)
    
    def getDensity(self):
        return self.population/AREA
        
class bushesSpecies:
    population: int = 0
    maxAge: int
    DfertilityRates: float
    curFrates: float
    dlh : DLH
    resources: float = 1.00003
    popArray = []
    
    def __init__(self, population: int = 150000, maxAge: int = 20, fertilityRates: float = 1.0019): # per week
        self.population = population
        self.maxAge = maxAge
        self.DfertilityRates = fertilityRates
        self.curFrates = fertilityRates
        self.popArray.append(self.population)
        
    def demolish(self):
        if (rd.randrange(int(self.dlh.climate)) == 1):
            self.population-=1
        if (rd.randrange(int(self.dlh.disease)) == 1):
            self.population-=2
        if (rd.randrange(int(self.dlh.predation)) == 1):
            self.population-=1
        if (rd.randrange(int(self.dlh.resource)) == 1):
            self.population-=0.5
    def setFertility(self, curSeason):
        if curSeason == "Wet":
            self.curFrates = self.DfertilityRates + 0.0028
        else: self.curFrates = self.DfertilityRates + 0.0027
        
    def update(self, curSeason):
        self.dlh = DLH(int(temperature[curSeason]/10), temperature[curSeason], 1000, 50)
        self.setFertility(curSeason)
        self.demolish()
        self.population*=self.curFrates*(timestep+koef)
        self.popArray.append(self.population)
    
    def getDensity(self):
        return self.population/AREA
    
class mushroomsSpecies:
    population: int = 0
    maxAge: int
    DfertilityRates: float
    curFrates: float
    dlh : DLH
    resources: float = 1.00008
    popArray = []
    
    def __init__(self, population: int = 150000, maxAge: int = 20, fertilityRates: float = 1.00202): # per week
        self.population = population
        self.maxAge = maxAge
        self.DfertilityRates = fertilityRates
        self.curFrates = fertilityRates
        self.popArray.append(population)
        
    def demolish(self):
        if (rd.randrange(int(self.dlh.climate)) == 1):
            self.population-=1
        if (rd.randrange(int(self.dlh.disease)) == 1):
            self.population-=1
        if (rd.randrange(int(self.dlh.predation)) == 1):
            self.population-=1
        if (rd.randrange(int(self.dlh.resource)) == 1):
            self.population-=1
    def setFertility(self, curSeason):
        if curSeason == "Wet":
            self.curFrates = self.DfertilityRates + 0.0027
        else: self.curFrates = self.DfertilityRates + 0.0026
        
    def update(self, curSeason):
        self.dlh = DLH(int(temperature[curSeason]/10), temperature[curSeason], 1000, 50)
        self.setFertility(curSeason)
        self.demolish()
        self.population*=self.curFrates*(timestep+koef)
        self.popArray.append(self.population)
    
    
    def getDensity(self):
        return self.population/AREA
    
class rabbitSpecies:
    population: int = 0
    DfertilityRates: float
    curFrates: float
    dlh : DLH
    Pdeath = 0.1
    popArray = []
    
    def __init__(self, population: int = 200, maxAge: int = 7, fertilityRates: float = 1.02): # per week
        self.population = population
        self.maxAge = maxAge
        self.DfertilityRates = fertilityRates
        self.curFrates = fertilityRates
        self.popArray.append(population)
        
    def demolish(self):
        if (rd.randrange(int(self.dlh.climate)) == 1):
            self.population-=5
        if (rd.randrange(int(self.dlh.disease)) == 1):
            self.population-=2
        if (rd.randrange(int(self.dlh.resource)) == 1):
            self.population-=2
    def setFertility(self, curSeason):
        self.curFrates = self.DfertilityRates+(0.005/temperature[curSeason])
        
    def update(self, curSeason, curWeek, predPopulaion, resIndex):
        self.dlh = DLH(int(temperature[curSeason]), temperature[curSeason], 20, 80)
        self.setFertility(curSeason)
        xd = self.popArray[curWeek-1] * (self.curFrates - self.Pdeath*predPopulaion[curWeek-1]) #######
        
        next_x = resIndex - 1 + 0.0014 + self.popArray[curWeek-1] + xd * timestep
        self.popArray.append(next_x)
        self.population = next_x
        self.demolish()
    
    def getDensity(self):
        return self.population/AREA

class foxSpecies:
    population: int = 0
    DfertilityRates: float
    curFrates: float
    dlh : DLH
    Pdeath = 0.4
    RforNewFox = 0.013
    popArray = []
    
    def __init__(self, population: int = 40, maxAge: int = 4, fertilityRates: float = 1.0024): # per week
        self.population = population
        self.maxAge = maxAge
        self.DfertilityRates = fertilityRates
        self.curFrates = fertilityRates
        self.popArray.append(population)
        
    def demolish(self):
        if (rd.randrange(int(self.dlh.climate)) == 1):
            self.population-=5
        if (rd.randrange(int(self.dlh.disease)) == 1):
            self.population-=2
        if (rd.randrange(int(self.dlh.resource)) == 1):
            self.population-=2
    def setFertility(self, curSeason):
        self.curFrates = self.DfertilityRates+(0.00005/temperature[curSeason])
        
    def update(self, curSeason, curWeek, preyPopulaion):
        self.dlh = DLH(int(temperature[curSeason]), temperature[curSeason], 20, 80)
        self.setFertility(curSeason)
        yd = -self.popArray[curWeek-1]*(self.Pdeath - self.RforNewFox*preyPopulaion[curWeek-1])
        
        next_y = self.popArray[curWeek-1] + yd * timestep
        self.popArray.append(next_y)
        self.population = next_y
        self.demolish()
    
    def getDensity(self):
        return self.population/AREA

class Simulation:
    def __init__(self):
        self.year = 0
        self.curSeason = "Wet"
        
        self.trees = treeSpecies()
        self.bushes = bushesSpecies()
        self.mushrooms = mushroomsSpecies() #############
        self.resourcesIndex = (self.trees.resources + self.bushes.resources + self.mushrooms.resources) / 3 - 0.00001
        
        self.foxes = foxSpecies()
        self.rabbits = rabbitSpecies()
    
    def update(self):
        pass
    
    def step(self):
        self.update()
        self.trees.update(self.curSeason)
        self.bushes.update(self.curSeason)
        self.mushrooms.update(self.curSeason)
    
    def run(self):
        s = 0
        for i in range(1, len(t)):
            if i < 2600 + (self.year*len(t)):
                self.curSeason = "Wet"
            elif i > 2600 + (self.year*len(t)):
                self.curSeason = "Dry"
            if i == 5200: self.year+=1
            self.step()
            self.rabbits.update(self.curSeason, i, self.foxes.popArray, self.resourcesIndex)
            self.foxes.update(self.curSeason, i, self.rabbits.popArray)
            # print(f"week {i}: season: {self.curSeason}")
        
    def graphAnimals(self):
        plt.plot(t, self.foxes.popArray)
        plt.plot(t, self.rabbits.popArray)
        plt.xlabel('Time')
        plt.ylabel('Population Size')
        plt.legend(('Foxes', 'Rabbits'))
        plt.title('Species population graph')
        plt.show()
    
    def graphPlants(self):
        plt.plot(t, self.bushes.popArray)
        plt.plot(t, self.trees.popArray)
        plt.plot(t, self.mushrooms.popArray)
        plt.xlabel('Time')
        plt.ylabel('Population Size')
        plt.legend(('Bushes', 'Trees', 'Mushrooms'))
        plt.title('Plants population graph')
        plt.show()

def main():
    sim = Simulation()
    sim.run()
    sim.graphPlants()
    print(sim.bushes.population)
    print(sim.trees.population)
    print(sim.mushrooms.population)

main()