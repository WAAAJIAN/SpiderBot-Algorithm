from math import *
import maestro
import datetime

servo = maestro.Controller('/dev/ttyAMA0')

#stand = [[0,200,60]*3]
# need settle the position for each leg in case of stand/walk, and make height customisable

period = 20000 # period of a whole semicircle (speed)
x_offset = 0
y_offset = 200
z_offset = 60
steps = 250 # determine how smooth the transit

ctc = 81
cl = 32.44
fl = 75
tl = 160

leg_max_length = 348.44

class Spider:
    def __init__(self):
        self.leg_count = 6
        self.leg = [TriLeg(0,0),TriLeg(1,0),TriLeg(0,1),TriLeg(1,1),TriLeg(0,2),TriLeg(1,2)]
        #self.leg = [TriLeg(0,0,0,1,2)]
        '''
        0       1       
         \     /
          \   /
    5 - - - - - - - 2    
          /   \   
         /     \ 
        4       3    
        '''
        self.time = 0
        self.step = steps
        self.leg_y = y_offset + ctc

    def twist(self,angle):
        curr_angle = angle

        while(curr_angle > 0):
            if (curr_angle > 15): # in 200 60 (y,z) more than 15 will raise math error
                twist_angle = 15
            else:
                twist_angle = curr_angle
            distance = self.leg_y * sin(radians(twist_angle))
            self.cycle(distance, self.step)
            curr_angle -= twist_angle
        
    def cycle(self, distance, step):
        while (self.time < period * 1.5):
            for i in self.leg:
                if i.set == 0 and self.time < period:
                    i.calculatePos(distance, self.time)
                if i.set == 1 and self.time > period/2:
                    i.calculatePos(distance, self.time - period/2)
            self.time += step
            delay(step)
        self.time = 0

class TriLeg:
    def __init__(self, set, pos, c, f, t):
        self.set = set # 0 or 1
        self.pos = pos # 0 for front, 1 for middle, 2 for back
        self.coxa = c
        self.femur = f
        self.tibia = t
        self.x = x_offset
        self.y = y_offset
        self.z = z_offset
        self.a = 0
        self.b = 0
        self.c = 180

    def calculatePos(self,distance,time):
        phrase = (time/period) * 360
        if(time <= period/2):
            self.x = - (distance*cos(radians(phrase)) + x_offset - distance)
            self.z = distance*sin(radians(phrase)) + z_offset
            self.y =  sqrt(((y_offset+ctc)**2)-(self.x**2))-ctc 
        else:
            self.x = - (distance*cos(radians(phrase)) + x_offset - distance)
            self.z = z_offset
            self.y = y_offset
        print("position: ", self.x,",",self.y,",",self.z)
        self.IK()
        self.run()
    
    '''
    def checkValid(self):
        if(self.a>60 or self.a<-60) or (self.b>60 or self.b<-60) or (self.c>180 or self.c<60):
            print("Invalid Input")
            return False
        else:
            return True
    '''

    def IK(self):
        y3 = self.y-ctc
        y2 = sqrt((self.y**2)+(self.x**2))-cl
        theta = atan(self.z/y2)
        l = sqrt((y2**2)+(self.z**2))

        self.a = degrees(atan(self.x/y3))
        self.b = degrees(acos(((fl**2)+(l**2)-(tl**2))/(2*fl*l))-theta)
        self.c = degrees(acos(((fl**2)+(tl**2)-(l**2))/(2*fl*tl)))
        print("angle: ",self.a,",",self.b,",",self.c,"\n")

    def angleToDC(self):
        self.a = 50 * self.a + 6000
        self.b = -50 * self.b + 6000
        self.c = 50 * self.c


    def run(self):
        self.angleToDC()
        servo.setTarget(self.c, self.a)
        servo.setTarget(self.f, self.b)
        servo.setTarget(self.t, self.c)
        delay(100)
        


def delay(ms):
    start_time = datetime.datetime.now()
    target_time = start_time + datetime.timedelta(milliseconds=ms)
    while datetime.datetime.now() < target_time:
        pass

girl = Spider()

while(1):
    angle = int(input("enter angle: "))
    girl.twist(angle)