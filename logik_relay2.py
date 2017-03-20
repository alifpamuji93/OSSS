import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

def relay():
    matikan = raw_input ("Matikan Lampu ? [y/t] : ")
    if matikan=='y' or matikan=='Y':
        GPIO.cleanup()
        
    elif matikan=='t' or matikan=='T':
        relay()
    else:
        print "NB : input yang anda masukkan SALAH!\n"
        relay()
        
relay()

