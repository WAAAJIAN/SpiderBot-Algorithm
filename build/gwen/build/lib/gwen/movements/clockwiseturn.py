import gwen.movements.maestro as  maestro
import time

servo = maestro.Controller('/dev/ttyAMA0')
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

#Coxa
print("odd coxa go middle")
servo.setTarget(0, 6000)
servo.setTarget(6, 6000)
servo.setTarget(18, 6000)
time.sleep(0.3)

#Femur
print("odd femur down")
servo.setTarget(1, 5000)
servo.setTarget(7, 5000)
servo.setTarget(19, 5000)
time.sleep(0.3)

#Femur
print("even femur up")
servo.setTarget(4, 3000)
servo.setTarget(10, 3000)
servo.setTarget(22, 3000)
time.sleep(0.3)

#Coxa
print("even coxa go middle")
servo.setTarget(3, 6000)
servo.setTarget(9, 6000)
servo.setTarget(21, 6000)
time.sleep(0.3)

#Coxa
print("odd coxa move")
servo.setTarget(0, 8000)
servo.setTarget(6, 8000)
servo.setTarget(18, 8000)
time.sleep(0.3)

#Femur
print("even femur down")
servo.setTarget(4, 5000)
servo.setTarget(10, 5000)
servo.setTarget(22, 5000)
time.sleep(0.3)

#Femur
print("odd femur up")
servo.setTarget(1, 3000)
servo.setTarget(7, 3000)
servo.setTarget(19, 3000)
time.sleep(0.3)

#Coxa
print("odd coxa go middle")
servo.setTarget(0, 6000)
servo.setTarget(6, 6000)
servo.setTarget(18, 6000)
time.sleep(0.3)

#Coxa
print("even coxa move")
servo.setTarget(3, 8000)
servo.setTarget(9, 8000)
servo.setTarget(21, 8000)
time.sleep(0.3)

servo.close
