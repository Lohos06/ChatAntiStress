import time
from machine import Pin, PWM

# Pins 
PIN_BTN = 6     # bouton sur GP6 
PIN_PWM = 28    # buzzer sur GP28

# Setup
btn = Pin(PIN_BTN, Pin.IN, Pin.PULL_UP)   
buzzer = PWM(Pin(PIN_PWM))
buzzer.duty_u16(0)

compteur = 0
SEUIL_STRESS = 10

def bip(ms=60, freq=1200):
    buzzer.freq(freq)
    buzzer.duty_u16(3000)
    time.sleep_ms(ms)
    buzzer.duty_u16(0)

while True:
    etat = btn.value()  # PULL_UP => 1 = relâché, 0 = appuyé

    if etat == 0:  # appui détecté
        compteur += 1
        print("Appui détecté (", compteur, ")")

        # buzzer
        bip(50, 1200)

        if compteur >= SEUIL_STRESS:
            print("+ de 10 appuis : calmez-vous !")
            bip(200, 300)
            time.sleep(1)
            compteur = 0  # reset

        # anti-spam : attendre relâchement
        while btn.value() == 0:
            time.sleep_ms(10)

    time.sleep_ms(20)
