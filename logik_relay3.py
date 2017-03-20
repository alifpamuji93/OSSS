import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

def relayon():
        print "\n ==========\n| Selesai! |\n =========="
        nyalakan = raw_input ("\nNyalakan lagi ? [y/t] : ")
        if nyalakan=='y' or 'Y':
            GPIO.setwarnings(False)
            
            relay()
        elif nyalakan=='t' or nyalakan=='T':
            relay()
        else:
            print "NB : input yang anda masukkan SALAH!\n"
            relay()
           
def relay():
    matikan = raw_input ("Matikan Lampu ? [y/t] : ")
    if matikan=='y' or matikan=='Y':
        GPIO.cleanup()
        relayon()
    
            
    elif matikan=='t' or matikan=='T':
        relay()
    else:
        print "NB : input yang anda masukkan SALAH!\n"
        relay()
        
relay()

