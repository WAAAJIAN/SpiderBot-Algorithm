import maestro
import datetime
from Parameter import *

servo = maestro.Controller('/dev/ttyAMA0')

# Rotation "Matrix"
R = lambda x, theta1, theta2 : (
    (0, ctc[x] * acos(theta2) * (1 - acos(theta1)), ctc[x] * acos(theta2) * asin(theta1)),
    (ctc[x], * asin(theta2) * (1 - acos(theta1)), 0 , ctc[x] * asin(theta2) * asin(theta1)),
    (0 , 0 , 0)) # to be include : yawing vector

class Spider:
    def __init__(self):
        self.leg = {0: Leg(0,0,0,0,1,2), 1: Leg(1,1,0,3,4,5), 2: Leg(2,1,1,6,7,8), 3: Leg(3,1,2,9,10,11), 4: Leg(4,0,2,18,19,20), 5: Leg(5,0,1,21,22,23)}

        '''
            0 (0,0)   1 (1,0)
             \     /
              \   /
    5 (0,1)- - - - - - - 2 (1,1)
              /   \ 
             /     \ 
            4 (0,2)   3 (1,2)
        '''
        self.time = 0

    def rotate_x(self, angle):
        for i in self.leg:
            if i.leg == 0 or i.leg == 5 or i.leg == 4: i.rotating(0, -angle) 
            else: i.rotating(0, angle)

class Leg:
    def __init__(self, leg, c, f, t):
        self.leg = leg             # 0 ~ 5, No. of leg, reference to graph on top
        self.coxa = c              # servo pin for coxa
        self.femur = f             # servo pin for femur
        self.tibia = t             # servo pin for tibia
        self.x = x_offset
        self.y = y_offset
        self.z = z_offset
        self.a = 0                 # angle of coxa
        self.b = 0                 # angle of femur
        self.c = 180               # angle of tibia
        
        self.offset = 0 if self.leg in (2, 5) else 1
        self.offset_angle = offset_angle_map[self.leg]

    def transformCoor(self):
        self.y -= y_offset
        newVec = vectorMull(transformMat[self.leg], [self.y, self.x])
        self.y = newVec[0] + y_offset
        self.x = newVec[1]

    def rotating(self, type, angle): # type : 0 = roll, 1 = pitch, 2 = yaw
        R_c = R(self.offset, angle, self.offset_angle)[type]
        self.x += R_c[0]
        self.y += R_c[1]
        self.z += R_c[2]

    # to be implemented: find the limit for both ik and actual leg
    ''' 
    def checkValid(self):
        if(self.a>60 or self.a<-60) or (self.b>60 or self.b<-60) or (self.c>180 or self.c<60):
            print("Invalid Input")
            return False
        else:
            return True
    '''

    def IK(self):
        y3 = self.y-ctc[self.offset]
        y2 = sqrt((self.y**2)+(self.x**2))-cl
        theta = atan(self.z/y2)
        l = sqrt((y2**2)+(self.z**2))

        self.a = degrees(atan(self.x/y3))
        self.b = degrees(acos(((fl**2)+(l**2)-(tl**2))/(2*fl*l))-theta)
        self.c = degrees(acos(((fl**2)+(tl**2)-(l**2))/(2*fl*tl)))
        print("angle: ",self.a,",",self.b,",",self.c)

    def angleToDC(self): # to be implemented: test servo target value instead of having all map to 3000~9000
        self.a = int((100 * self.a)/3 + 6000)
        self.b = int((-100 * self.b)/3 + 6000)
        self.c = int((100 * self.c)/3 + 2000)
        print("output: ",self.a,",",self.b,",",self.c,"\n")

    def run(self):
        self.angleToDC()
        servo.setTarget(self.coxa, self.a)
        servo.setTarget(self.femur, self.b)
        servo.setTarget(self.tibia, self.c)


def main():
    girl = Spider()

main()