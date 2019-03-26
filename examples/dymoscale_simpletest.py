import board
import digitalio
import adafruit_dymoscale

# initialize the dymo scale
units_pin = digitalio.DigitalInOut(board.D3)
units_pin.switch_to_output()
dymo = adafruit_dymoscale.DYMOScale(board.D4, units_pin)

while True:
    reading = dymo.weight
    text = "{} g".format(reading.weight)
    print(text)
    # to avoid sleep mode, we'll toggle the units pin.
    # if we don't want to switch the units on the next read...
    dymo.toggle_unit_button()

    # if we do want to switch the units on the next read...
    # dymo.toggle_unit_button(switch_units=True)
