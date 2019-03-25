import board
from adafruit_dymoscale import Scale

# initialize the scale's USB and g/oz button
dymo = Scale(board.D3, board.D4)

while True:
    try:
        dymo.get_scale_data()
        if dymo.units == 'oz':
            text = "%0.1f oz" % dymo.weight
        if dymo.units == 'g':
            text = "%0.1f g" % dymo.weight
        print(text)
    except RuntimeError:
        print("Failed to read data, is scale on?")
