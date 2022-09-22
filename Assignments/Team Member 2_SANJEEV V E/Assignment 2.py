import random

t=random.randint(1,150)
h=random.randint(1,150)

if a>75:
    if b>75:
        print("hazard predected ,temp: {t1}  Hum: {h1}".format(t1=t,h1=h))
        print("Alarm ON")
    else:
        print("high temperature , temp:",t )
        print("Alarm ON")
else:
    print("all good ,temp: {t1}  Hum: {h1}".format(t1=t,h1=h))
    print("Alarm OFF")
