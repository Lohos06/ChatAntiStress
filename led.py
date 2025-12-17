from machine import Pin, PWM
from time import sleep

r = PWM(Pin(0))
g = PWM(Pin(1))
b = PWM(Pin(2))

r.freq(1000)
g.freq(1000)
b.freq(1000)

def couleur(red, green, blue):
    r.duty_u16(red)
    g.duty_u16(green)
    b.duty_u16(blue)


try:
    while True:
        couleur(5000, 0, 0)     # rouge
        sleep(1)

        couleur(0, 5000, 0)     # vert
        sleep(1)

        couleur(0, 0, 5000)     # bleu
        sleep(1)

        couleur(5000, 5000, 5000)  # blanc doux
        sleep(1)

finally:
    couleur(0, 0, 0)