import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
pirPin = 18


GPIO.setup(pirPin, GPIO.IN)

 
try:
    while True:
        if GPIO.input(pirPin) == GPIO.LOW:
            print "No motion"
            relayPin = 17
            GPIO.cleanup(relayPin)
            
        else:
            print "Motion Detected!"
            
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            relayPin = 17
            GPIO.setup(relayPin, GPIO.OUT)
            
            time.sleep(10.0)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()

        
            
   
