## import RPi.GPIO as GPIO
#importing libraries

from cmu_graphics import *
from pysinewave import SineWave

##GPIO.setwarnings(False)
##GPIO.setmode(GPIO.BOARD)
##GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
#the silly little variables
test = Label("test", 200, 200, visible = False)
sinewave = SineWave(pitch = 23)
count = 0

#the function
def onKeyPress(key):
    if(key == 'a'):
        global count
        count += 1
        #modulus
        if(count % 2 == 1):
            print("sdf")
            sinewave.play()
            test.visble =True
        else:
            sinewave.stop()
            test.visible = False

## for RPi testing purposes
#def buttonPress():
    #if(GPIO.input(__) == GPIO.HIGH):
        #print("sdf")
        #sinewave.play()
    #elif(GPIO.input(__) == GPIO.LOW):
        #print("fds")
        #sinewave.stop()

cmu_graphics.run()