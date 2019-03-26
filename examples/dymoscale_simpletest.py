import board
from adafruit_dymoscale import Scale

# initialize the dymo scale
dymo = Scale(board.D3, board.D4)

while True:
    print("{:0.1f}  {}".format(dymo.weight, dymo.units))
    # to avoid sleep mode, we'll toggle the units pin.
    # if we don't want to switch the units on the next read...
    dymo.toggle_unit_button()

    # if we do want to switch the units on the next read...
    # dymo.toggle_unit_button(switch_units=True)
