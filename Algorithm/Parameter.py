from math import *
import datetime

period = 30000   # period of a leg cycle (its not time!)
x_offset = 0     # initial x position of leg (vertical axis)
y_offset = 150   # initial y position of leg (horizontal axis from the center)
z_offset = 130   # initial z position of leg (height of bot)
steps = 1500     # speed of motion

ctc = (91.37, 105.47) # ctc[0] for middle legs, ctc[1] for corner legs
cl = 76.42 # length of coxa
fl = 60    # length of femur
tl = 157.21   # length of tibia

offset_angle_map = {0: 54, 1: 54, 2: 0, 5: 0, 3: -54, 4: -54} # offset angle of each leg from y axis

#leg_max_length = 358.44 # maximum y position that leg can go to

#Matrix for transform coordinate on each leg
M0 = [[sin(radians(30)), cos(radians(30))], [sin(radians(60)), -cos(radians(60))]]    # leg 0
M1 = [[sin(radians(30)), cos(radians(30))], [-sin(radians(60)), cos(radians(60))]]    # leg 1
M2 = [[1, 0], [0, 1]]                                                                 # leg 2
M3 = [[sin(radians(30)), -cos(radians(30))], [sin(radians(60)), cos(radians(60))]]    # leg 3
M4 = [[sin(radians(30)), -cos(radians(30))], [-sin(radians(60)), -cos(radians(60))]]  # leg 4
M5 = [[1, 0], [0, -1]]                                                                # leg 5
transformMat = {0: M0, 1: M1, 2: M2, 3: M3, 4: M4, 5: M5}

def vectorMull(m1, m2): # transform vector (Matrix Multiplication)
    m3 = [(m1[0][0])*(m2[0]) + (m1[0][1])*(m2[1]), (m1[1][0])*(m2[0]) + (m1[1][1])*(m2[1])]
    #print(m1," x ", m2," = ",m3)
    return m3

def polarVector(angle, value = 1):
    return [value * cos(radians(angle)), value * sin(radians(angle))]

def delay(ms):
    start_time = datetime.datetime.now()
    target_time = start_time + datetime.timedelta(milliseconds=ms)
    while datetime.datetime.now() < target_time:
        pass
