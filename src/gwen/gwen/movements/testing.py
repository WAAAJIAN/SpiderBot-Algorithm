import gwen.movements.maestro as  maestro
import time

servo = maestro.Controller('/dev/ttyAMA0')
servo.setSpeed(0, 60)
servo.setSpeed(1, 60)
servo.setSpeed(2, 60)

servo.setTarget(0, 6000)
servo.setTarget(1, 6000)
servo.setTarget(2, 7000)

servo.close
