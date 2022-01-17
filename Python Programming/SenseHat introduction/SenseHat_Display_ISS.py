from sense_hat import SenseHat
sense = SenseHat()

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
black=(0,0,0)

temp = sense.get_temperature()
press = sense.get_pressure()
humid = sense.get_humidity()

if temp > 18.3 and temp < 26.7:
    temp_color = green
else:
    temp_color = red
    
if press > 999 and temp < 1027:
    press_color = green
else:
    press_color = red    

if humid > 55 and humid < 65:
    humid_color = green
else:
    humid_color = red    
    
formatted_temp = str("{:.2f}".format(temp))
formatted_press = str("{:.2f}".format(press))
formatted_humid = str("{:.2f}".format(humid))

sense.show_message(
    'Temperature: ' + formatted_temp + " celsius",
    text_colour=temp_color,
    back_colour=white,
    scroll_speed=(0.08)
    )


sense.show_message(
    'Pressure: ' + formatted_press + " millibar",
    text_colour=press_color,
    back_colour=white,
    scroll_speed=(0.08)
    )

sense.show_message(
    'Humidity: ' + formatted_humid + "%",
    text_colour=humid_color,
    back_colour=white,
    scroll_speed=(0.08)
    )

sense.clear()


