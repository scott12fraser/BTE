# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# class that defines cars info make , modle, enginesize and, price
class car :
    makeOfCar=''
    model = ''
    engineSize =''
    price= 0
    def car (self,make,model,engineSize,price):
        self.makeOfCar=make
        self.model = model
        self.engineSize = engineSize
        self.price = price
    def toString(self):
        return self.makeOfCar, self.model, self.engineSize, self.price
    
#garage object for cars to be added to and sold
class garage:       
  
  def garage():
    global carInvontory
    carInvontory= []
  garage()    
  def addTocarGarage(self, car):
   
    carInvontory.append(car)
  def sellCar(self,offer,car):
      if offer >= car.price:
          print('sold')
          carInvontory.remove(car)
      else:
          print("offer is not enogh, rejected ")
          
  def seeFullInvontory(self):
       for car in carInvontory:
           currentCar = car.toString()
           print(currentCar)

  def applieDisscount(self,discountPercentage,car):
      
       disscount = (car.price * discountPercentage)/100 
       car.price -= disscount
  def searchGarage(self,toFilter,keyWord):
        for car in carInvontory:
            
             if toFilter == 'Make':
               currentSearch = car.makeOfCar
             elif toFilter == 'model':
               currentSearch = car.model
             elif toFilter == 'engine':
               currentSearch = car.engineSize
             elif toFilter == 'price':
               currentSearch = car.price  
               
               
             if currentSearch == keyWord:
                print(car.toString())
    
    
car1 = car()
car2= car()
car3 = car()
car1.car('bmw','D3','3 liter',10000)
car2.car('bmw','m3','3.1 liter',12000)
car3.car('Audi','R8','V8',45000)
bmw= garage()

bmw.addTocarGarage(car1)
bmw.addTocarGarage(car2)
bmw.addTocarGarage(car3)
#bmw.seeFullInvontory()
bmw.searchGarage('Make', 'bmw')
bmw.sellCar(9000,car1)
bmw.seeFullInvontory()
bmw.applieDisscount(20, car1)
bmw.seeFullInvontory()
bmw.sellCar(9000,car1)