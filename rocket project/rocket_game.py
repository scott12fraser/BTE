# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:04:41 2023

@author: scott
"""
import time
import json
from tkinter import *
from PIL import ImageTk,Image
root= Tk()
def main():
 
    acc_button= Button(root,text='accelrate', command =test().a)
    decc_button= Button(root,text='decelrate', command =test().d).pack()
    acc_button.pack()
    
    root.mainloop()
class test:
    def a(self):
        ship().create()
        computer().Accelrator('All_thrusters',0)
        p =50
        computer().Accelrator('All_thrusters',p)  
        A= computer().accelerometer()
        acc_lable= Label(root,text= A)             
        acc_lable.pack()        
                 
                      
        
            
    def d(self):
        p=0
        computer().Accelrator('All_thrusters',p)  
        A= computer().accelerometer()
        dcc_lable= Label(root,text= A)             
        dcc_lable.pack() 
    
    
class controlls():
    # runs the controll pannel gui and its functions 
    def control_pannel(self):
        #initatis the Gui controll pannel
      def _int_():
           
          
           def build_buttonF():
               build_button.destroy()
               ship().create()
               ship_img =  Image.open('ship_.png')
               ship_img = ImageTk.PhotoImage(ship_img)
               global ship_lable
               ship_lable= Label(image=ship_img)
               ship_lable.image = ship_img
               ship_lable.grid(row= 4, column=4,columnspan=2, rowspan=3)
              
               ship_GUI()
               
           def ship_GUI():
            v1 = DoubleVar()   
            input_acc= Scale( root, variable = v1, from_ = 0, to = 100, orient = HORIZONTAL)  
            input_acc.grid(row= 1, column=4,columnspan=2)
            self.acc_lable= Label(root,text= 'Accelration: 0')  
            self.acc_lable.grid(row= 3, column=4,columnspan=2)
            
            #call function acc and chanmges ship img in gui
            def acc_buttF(fun='acc'):
                 global ship_lable
                 percent = input_acc.get()
                
                 if percent == 100:
                     ap = 100
                 if percent==0 or fun !='acc':
                     ap = ''
                     percent = 0
                 if percent < 100 and percent>0:
                     ap =50
                 acc(percent)    
                 ship_img = ImageTk.PhotoImage(Image.open('ship_'+str(ap)+'.png'))
                 ship_lable.grid_forget()
                 ship_lable= Label(image=ship_img)
                 ship_lable.image = ship_img
                 ship_lable.grid(row= 4, column=4,columnspan=2, rowspan=3)
                 
                 
                 
            acc_button= Button(root,text='accelrate', command =lambda: acc_buttF())
            
            current_acc= computer().accelerometer()
            decc_button= Button(root,text='decelrate', command =lambda: acc_buttF('decc')).grid(row= 2, column=5)
            acc_button.grid(row= 2, column=4)
           global build_button
           build_button= Button(root,text='build ship', command =build_buttonF)
           build_button.pack()
           root.mainloop()
           #taskes in percentaghe and run the acclrator and displays out put from accelromter
      def acc(p):
                
                     
                     computer().Accelrator('All_thrusters',p)  
                     A= computer().accelerometer()
                     
                  
                     self.acc_lable.destroy()
                     self.acc_lable= Label(root,text= 'Accelration: ' + str(A))   
                     
                     self.acc_lable.grid(row= 3, column=4,columnspan=2) 
                     
      _int_()               
     
               
class ship():
    
    # takes in ship speacifcations and creates each part 
    def create(self,eng_mod='RS-25',tank_s=30,tank_m=30):
        s ={'TWeight':0,
          'All_thrusters':{'Thrust':0},
          'engine model': eng_mod,
          'tank':{'size':tank_s, 'mass':tank_m}
          
          
          }
          
        fuel_tank().create(s['tank']['size'],s['tank']['mass'])
        engine().create(s['engine model'])
        
        #find total mass
        def get_mass():
            m_e= engine().get()
            for key in m_e:
              m_e= m_e[key]['mass']
            m_t = fuel_tank().get()
            m_t = m_t['Tank']['mass']
            m= float(m_t) +float(m_e)
            
            return m
        s['TWeight'] = get_mass()
      
        j= json.dumps(s)
        # open file for writing, "w" 
        f = open('s.json','w')
        # write json object to file
        f.write(j)
        # close file
        f.close
    def update(self,d):
        s=d
        j= json.dumps(s)
        # open file for writing, "w" 
        f = open('s.json','w')
        # write json object to file
        f.write(j)
        # close file
        f.close
        
    def  get(self):
        d= 's.json'
        d = open(d)
        d= json.load(d)
        return d
class computer():
    #calclute force from thrust method
    def thrust_to_force(self,thrust):
        #One kilogram-force is therefore equal to 9.80665 N
        f= float(thrust) * 9.80665
        return f
    #accelration calculator take in mass and force return accelration     
    def Accelration_calculator(self,mass,force):
        A = float(force)/float(mass)
        return A
    def accelerometer(self,rang=10):
        for i in range(rang):
            def force():
                s= ship().get()
                t=  s['All_thrusters']['Thrust']
                
                f= self.thrust_to_force(t)
                
                return f
            force = force()
            mass = self.scales() 
      
            A = self.Accelration_calculator(mass, force)
            return A
    #calculates thruist from thrust and the accelrator percentage        
    def thrust_calculator(self,thrust,percentage = 100)   :
        p= float(percentage)/ 100
        t = p* thrust
        return t
    def Accelrator(self,thruster_name='All_thrusters',percentage = 100):
        t= self.thrust_calculator(213188,percentage)
        s= ship().get()
       
        s[thruster_name]['Thrust'] = t
        ship().update(s)
        engine().fuel_injector(t)
    def scales(self):
        s= ship().get()
        w= s['TWeight']
        return w
        
        
class engine :
    #loads and saves engin profiles for engine
    def engine_profilesr(self):
        #create dictionary
        d = {'RS-25':{'fuel': 'liquid - hydrogen',
                       'Thrust':213188, #  kilograms                
                        'max_temp': '6000',  # Fahrenheit
                        'mass':'3.5', # tonnes
                        'mass_flow_rate': '514.49' #kg/s
                        }}
       
        # create json object from dictionary
        j= json.dumps(d)
        # open file for writing, "w" 
        f = open('d.json','w')
        # write json object to file
        f.write(j)
        # close file
        f.close
        return 'd.json'
    
    # engine of ship takes in a fuel type return an amout of force
    def create(self,model= ''):
       
        d = self.engine_profilesr()
        d = open(d)
        d= json.load(d)
        print(d)
    def get(self)  :
        d= 'd.json'
        d = open(d)
        d= json.load(d)
        return d
    def fuel_injector(self,fuel):
        
        fuel_tank().update(fuel)
        
class fuel_tank :       
   # def fuel_tank_compute(self) :
   
        
    def get(self):
            t= 't.json'
            t = open(t)
            t= json.load(t)
            return t
    def update(self, up_a):
         t= self.get()
         A = t['Tank']['Amount_fuel']
         A = float(A)
         A= A + up_a
         t['Tank']['Amount_fuel'] =  A
         j= json.dumps(t)
        # open file for writing, "w" 
         f = open('t.json','w')
        # write json object to file
         f.write(j)
        # close file
         f.close
    def create(self,size=30,mass= 30,Amount=0.0):
             #create dictionary
        t = {'Tank':{'size': size,  # Liters
                        'mass': mass, # kg
                        'Amount_fuel': Amount # Liters
                        }}
       
        # create json object from dictionary
        j= json.dumps(t)
        # open file for writing, "w" 
        f = open('t.json','w')
        # write json object to file
        f.write(j)
        # close file
        f.close
        return t
        
        
        
        
        
        
        
        
        
        
        
        
        
        
e = engine()
f = fuel_tank()  
c = computer()


if __name__ == "__main__":
      controlls().control_pannel() 
   