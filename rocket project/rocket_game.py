# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:04:41 2023

@author: scott
"""
import time
import json

from tkinter import *
from PIL import ImageTk,Image
import threading
ship_displaying = False
global root
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
      def displays(stat):
          
          
        
           
          frame= Frame(root)   
          def distance_display():
                        global timer_time
                        frame.dis_lable= Label(root,text= '                                                                                             ' ) 
                        dis = computer().distanceometer()
                        frame.dis_lable.grid(row= 5, column=8)
                        frame.dis_lable= Label(root,text= 'Distance:'+ str(round(dis,2))+'m') 
                        frame.dis_lable.grid_forget()
                        frame.dis_lable.grid(row= 5, column=8)
                
                        return timer_time
          def timer_display():
                        global timer_time
                        frame.timer_lable= Label(root,text= '                                                                                             ' ) 
                     
                        frame.timer_lable.grid(row= 4, column=8)
                        frame.timer_lable= Label(root,text= 'Timer:'+ str(round(timemer_display_time,2))+'s') 
                        frame.timer_lable.grid_forget()
                        frame.timer_lable.grid(row= 4, column=8)
                
                        return timer_time
              
              
              
          def S_display():
              
               
              
                   
                
                       
                     
                       A= computer().accelerometer()
                       Ma = computer().max_accelration()
                       if A == Ma:
                         ap = 100
                       if str(A) == '0.0':
                        ap = ''
                       percent = 0
                       if A < Ma and A>0:
                        ap =50
                       ship_img = ImageTk.PhotoImage(Image.open('img/ship_'+str(ap)+'.png'))
                       frame.ship_lable= Label(image=ship_img)
                       frame.ship_lable.image = ship_img
                       frame.ship_lable.grid(row= 4, column=4,columnspan=2, rowspan=3)
                   
                       
                      
                       
                        
                    
               
                     
          def F_display():
                 
                       
                         
                        f= fuel_tank().get()
                      
                        f=f['Tank']['Amount_fuel']
                        
                        frame.fuel_lable= Label(root,text= '                                 ' ) 
                     
                        frame.fuel_lable.grid(row= 1, column=8)
                        frame.fuel_lable= Label(root,text= 'Fuel: ' + str(round(f,2))+'L') 
                        frame.fuel_lable.grid_forget()
                        frame.fuel_lable.grid(row= 1, column=8)
                
                    
                   
                   
                      
                        
                        
                       
                  
                  
                   
          def A_display():      
              
              
                  
                       A= computer().accelerometer()
                         
            
                  
                    
                       frame.acc_lable= Label(root,text= '                                                         ' )   
                      
                 
                       frame.acc_lable.grid(row= 3, column=4,columnspan=2) 
                       frame.acc_lable= Label(root,text= 'Acceleration: ' + str(round(A,2)))   
                       frame.acc_lable.grid_forget()
                 
                       frame.acc_lable.grid(row= 3, column=4,columnspan=2) 
                    
          def SP_display():      
              
              
                  
                       sp= computer().speedometer()
                         
            
                  
                    
                       frame.speed_lable= Label(root,text= '                                            ' )   
                      
                 
                       frame.speed_lable.grid(row= 3, column=2,columnspan=2) 
                       frame.speed_lable= Label(root,text= 'speed: ' + str(round(sp,2)) +'ms' ) 
                       frame.speed_lable.grid_forget()
                 
                       frame.speed_lable.grid(row= 3, column=2,columnspan=2)     
                     
                       
                         
                  
                   
                   
          
          S_display()         
          A_display()
          timer_display()
          F_display()
          SP_display()  
          distance_display()
        #frame.grid_forget()
            
             
             
      def _int_():
           
          
           def build_buttonF():
               build_button.pack_forget()
               ship().create()
               global status
               status = False
               
               print(threading.active_count())
               ship_img =  Image.open('img/ship_.png')
               ship_img = ImageTk.PhotoImage(ship_img)
               global ship_lable
               ship_lable= Label(image=ship_img)
               ship_lable.image = ship_img
               ship_lable.grid(row= 4, column=4,columnspan=2, rowspan=3)
               def start_start():
                  def start():
                   global status
                  
                   status = 'Running'
                   engine().fuel_injector()
                   start_button.grid_forget()
                   
                   ship_GUI()
                   timer_time1=0    
                   global timer_time
                   global timemer_display_time
                   global current_speed
                   global current_distance
                   current_speed = 0
                   timer_time = 0.0
                   current_distance=0
                   timemer_display_time = 0.0
                   start_check = False 
                   while status == 'Running':         
                      diff2 =time.time()  
                      
                     
                      #timer_time = timer_display(time.time(),diff2,timer_time)
                      #_dis = threading.Thread(target=displays,args= (status, ))   
                 
                 
                
                      
                      
                     # _dis.start() 
                      
                      
                      displays(status)
                      time.sleep(1)
                      A= computer().accelerometer()
                      
                      if A > 0.0:
                       start_check = True   
                       timer_time = computer().timer(time.time(),diff2, timer_time)
                      if start_check== True:
                          timemer_display_time = computer().timer(time.time(),diff2, timemer_display_time)
                  start_ = threading.Thread(target=start)   
                  start_.start()   
               start_button= Button(root,text='Start', command =start_start)
               start_button.grid(row= 1, column=5)
              
           #displays the gui after ship being built     
           def ship_GUI():
            v1 = DoubleVar()   
            input_acc= Scale( root, variable = v1, from_ = 0, to = 100, orient = HORIZONTAL)  
            input_acc.grid(row= 1, column=4,columnspan=2)
            #
            acc(0) 
            
            #call function acc and changes ship img in gui
            def acc_buttF(fun='acc'):
                 f = fuel_tank().get()['Tank']['Amount_fuel']
                 if f > 0.0:
                  print(threading.active_count())
                  percent = input_acc.get()
                
                 
                     #displays img of the ship changing based on the acceration input
                 
                  global current_speed
                  current_speed=  computer().speedometer()
                  global current_distance
                  current_distance= computer().distanceometer()
                  acc(percent) 
                 else:
                     print('')
             #function to display fuel amount     
            
                
            def refuel():
                f= fuel_tank().get()
             
                fuel_tank().update(f['Tank']['size'])
             
                #fuel_display()
             
                
                
            acc_button= Button(root,text='Accelerate', command =acc_buttF)
            fuel_button= Button(root,text='refuel', command =refuel).grid(row= 2, column=8)
            
            
            current_acc= computer().accelerometer()
            decc_button= Button(root,text='Decelerate', command =lambda: acc_buttF('decc')).grid(row= 2, column=5)
            acc_button.grid(row= 2, column=4)
           global build_button
          # fuel= Label(text='Tank Size: ')
           #Tnk_size = Entry()
           build_button= Button(root,text='build ship', command =build_buttonF)
           build_button.pack()
           print(threading.active_count())
           root.mainloop()
           #taskes in percentage and run the acclrator and displays out put from accelromter
      def acc(p):
                
                     
                     computer().Accelrator('All_thrusters',p)  
                     
                     
                     
      _int_()               
     
               
class ship():
    
    # takes in ship speacifcations and creates each part 
    def create(self,eng_mod='RS-25',tank_s=1000000,tank_m=30):
        global s
        s ={'TWeight':0,
          'All_thrusters':{'Thrust':0},
          'engine model': eng_mod,
          'tank':{'size':tank_s, 'mass':tank_m}
          
          
          }
      
        p= fuel_tank().create(s['tank']['size'],s['tank']['mass'])
        print(p)
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
      
      
    def update(self,d):
        s=d
        
        
    def  get(self):
      
        return s
class computer():
    #starts a timer when called 
    def timer(self,time1,diff2,timer_time1):
              
                        diff= time1 - diff2
                        
                        timer_timeT = diff +timer_time1
                        
                      
                
                        return timer_timeT
                    
    #calclute force from thrust method
    def thrust_to_force(self,thrust):
        #One kilogram-force is therefore equal to 9.80665 N
        f= float(thrust) * 9.80665
        return f
    #accelration calculator take in mass and force return accelration     
    def Accelration_calculator(self,mass,force):
        
        A = float(force)/float(mass)
        return A # metters per secon sqared ms2
    def max_accelration(self) :
            def force():
                t= engine().get()['RS-25']['Thrust']
               
                
                f= self.thrust_to_force(t)
                
                return f
            force = force()
            mass = self.scales() 
      
            A = self.Accelration_calculator(mass, force)
            return A
    def distance_cal(self,speed ,time ) :
        d= speed*time
        return d
    def distanceometer(self):
        speed=self.speedometer()
        time= timemer_display_time
        global current_distance
        dis1 =self.distance_cal(speed, time)
        distance= dis1 + current_distance
        return distance 
    def speed_calculator(self,timel,accelration,speed):
     
        speed1 = accelration * timel
        speedf = speed1 +speed
        return speed,speedf     
    def speedometer(self):
        global timer_time
        timel = timer_time
        accelration =  self.accelerometer()
        global current_speed
        speed = self.speed_calculator(timel,accelration,current_speed)
        current_speed = speed[0]
        return speed[1]# ms meters per second
    def accelerometer(self):
       
            def force():
                
                t=  s['All_thrusters']['Thrust']
                
                f= self.thrust_to_force(t)
                
                return f
            force = force()
            mass = self.scales() 
      
            A = self.Accelration_calculator(mass, force)
            return A # metters per secon sqared ms2
    #calculates thruist from thrust and the accelrator percentage        
    def thrust_calculator(self,thrust,percentage = 100)   :
        p= float(percentage)/ 100
        t = p* thrust
        return t
    def Accelrator(self,thruster_name='All_thrusters',percentage = 100):
        t= self.thrust_calculator(213188,percentage)
       
       
        s[thruster_name]['Thrust'] = t
       
        
         
         
         
         
    def scales(self):
       
        w= s['TWeight']
        
        return w
        
        
class engine :
    #loads and saves engin profiles for engine
    def engine_profilesr(self):
        #create dictionary
        d = {'RS-25':{'fuel': 'liquid - hydrogen',
                       'Thrust':213188, #  kilograms                
                        'max_temp': '6000',  # Fahrenheit
                        'mass':'3175.15', # kilograms
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
    def fuel_injector(self):
       
        def injection(stat =False):
           
         thruster_name = 'All_thrusters'   
         f=fuel_tank().get()['Tank']['Amount_fuel'] 
         t=s[thruster_name]['Thrust'] 
         print(f,t)
         enogh_fuel = False
         if f >= t:
             
             enogh_fuel = True
             try:
                  self.fuel_light.grid_forget()
             except:
                 pass
             self.fuel_light = Label(text= 'F', fg = 'green')
             self.fuel_light.grid(row= 3, column=8)
         def no_fuel():
             time.sleep(1)
             global current_speed
             current_speed=  computer().speedometer()
             global timer_time
             global current_distance
             current_distance= computer().distanceometer()
             f=fuel_tank().get()['Tank']['Amount_fuel'] 
             
             f2= 0- int(f)
             fuel_tank().update(f2)
             s[thruster_name]['Thrust'] =f
             self.fuel_light.grid_forget()
             fuel_light = Label(text= 'F', fg = 'red')
             fuel_light.grid(row= 3, column=8)
             #time.sleep(1)
             s[thruster_name]['Thrust'] =0
             timer_time = 0
             
             
             
             
         
         while stat == 'Running': 
           
          f=fuel_tank().get()['Tank']['Amount_fuel']  
          if f >0:
              self.fuel_light.grid_forget()
              self.fuel_light = Label(text= 'F', fg = 'green')
              self.fuel_light.grid(row= 3, column=8)
          t2 = s[thruster_name]['Thrust'] 
        
          #if t2 == 0:
           #   enogh_fuel = False
            
          if f >= t2:
          
           t2= 0- int(t2)
           fuel_tank().update(t2)
           f=fuel_tank().get()['Tank']['Amount_fuel'] 
           
           
          else :
              no_fuel()
              enogh_fuel = False
          time.sleep(1)     
              
         #if enogh_fuel != True:
           #no_fuel()
        global status   
                  
        inject = threading.Thread(target=injection, args= (status, ))
        inject.start()
class fuel_tank:       
   # def fuel_tank_compute(self) :
    
        
    def get(self):
           
            return self.t
    def update(self, up_a):
         t= self.get()
         A = t['Tank']['Amount_fuel']
         A = float(A)
         A= A + up_a
         t['Tank']['Amount_fuel'] =  A
         
    def create(self,size=10000000,mass= 30,Amount=100000.0):
             #create dictionary
             
        fuel_tank.t = {'Tank':{'size': size,  # Liters
                        'mass': mass, # kg
                        'Amount_fuel': Amount # Liters
                        }}
        return self.t
      
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
e = engine()
f = fuel_tank()  
c = computer()


if __name__ == "__main__":
      controlls().control_pannel()
   