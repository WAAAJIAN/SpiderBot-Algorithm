import gwen.movements.maestro
import time

servo = gwen.movements.maestro.Controller('/dev/ttyAMA0')
print("starting")
servo.setSpeed(0, 60)
servo.setSpeed(1, 60)
servo.setSpeed(2, 60)
servo.setSpeed(3, 60)
servo.setSpeed(4, 60)
servo.setSpeed(5, 60)
servo.setSpeed(6, 60)
servo.setSpeed(7, 60)
servo.setSpeed(8, 60)
servo.setSpeed(9, 60)
servo.setSpeed(10, 60)
servo.setSpeed(11, 60)
servo.setSpeed(12, 60)
servo.setSpeed(13, 60)
servo.setSpeed(14, 60)
servo.setSpeed(15, 60)
servo.setSpeed(16, 60)
servo.setSpeed(17, 60)
servo.setSpeed(18, 60)
servo.setSpeed(19, 60)
servo.setSpeed(20, 60)
servo.setSpeed(21, 60)
servo.setSpeed(22, 60)
servo.setSpeed(23, 60)

#Stand Up
#Coxa
servo.setTarget(0, 6000)
servo.setTarget(3, 6000)
servo.setTarget(6, 6000)
servo.setTarget(9, 6000)
servo.setTarget(18, 6000)
servo.setTarget(21, 6000)
print("done coxa")
time.sleep(0.5)

#Tibia
servo.setTarget(2, 4500)
servo.setTarget(5, 4200)
servo.setTarget(8, 4500)
servo.setTarget(11, 4900)
servo.setTarget(20, 5700)
servo.setTarget(23, 4900)
print("done Tibia")
time.sleep(0.5)

#Femur
servo.setTarget(1, 4500)
servo.setTarget(4, 4500)
servo.setTarget(7, 4500)
servo.setTarget(10, 4500)
servo.setTarget(19, 4500)
servo.setTarget(22, 4500)
print("done Femur")
time.sleep(0.5)

print("Stood up")

servo.close




