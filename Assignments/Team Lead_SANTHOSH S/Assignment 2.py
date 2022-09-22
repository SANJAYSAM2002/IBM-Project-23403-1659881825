import random
temperature = random.randint(0,200)
humidity = random.randint(0,150)
print("Temperature value = ",temperature)
print("Humidity Value = ",humidity)
if temperature > 80 and humidity > 70:
    print("alarm ON : Hazardous Predicted")
elif temperature > 80 and humidity < 70:
    print("alarm ON : High Temperature")
else:
    print("alarm OFF")
