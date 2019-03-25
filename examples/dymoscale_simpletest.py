import board
from adafruit_dymoscale import Scale

# initialize the dymo scale
dymo = Scale(board.D3, board.D4)

while True:
    dymo.get_scale_data()
    if dymo.units == 'oz':
        text = "%0.1f oz" % dymo.weight
    if dymo.units == 'g':
        text = "%0.1f g" % dymo.weight
    print(text)
    # to avoid sleep mode, we'll toggle the units pin
    dymo.toggle_unit_pin()