
from machine import Pin, PWM
import time


buzzer = PWM(Pin(28))

def beep(frequence, duree):
    buzzer.freq(frequence) 
    buzzer.duty_u16(32768)  # duty_u16 : puissance , 32768 = 50%
    time.sleep(duree)      
    buzzer.duty_u16(0)     

print("Appuie sur le boutton")
while True:
    beep(1000, 0.5)       
    time.sleep(1)
    print("Le buzzer sonne !!")