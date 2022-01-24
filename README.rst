Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-dymoscale/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/dymoscale/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_DymoScale/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_DymoScale/actions/
    :alt: Build Status

CircuitPython interface for `DYMO <http://www.dymo.com/en-US>`_ postage scales.

NOTE: This library will not work on embedded linux, only on microcontrollers.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-dymoscale/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-dymoscale

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-dymoscale

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-dymoscale

Usage Example
=============

Initialize the scale by passing it a data pin and a pin to toggle the units button:

.. code-block:: python

    # initialize the dymo scale
    units_pin = digitalio.DigitalInOut(board.D3)
    units_pin.switch_to_output()
    dymo = adafruit_dymoscale.DYMOScale(board.D4, units_pin)

Get the item's weight from the scale:

.. code-block:: python

    reading = dymo.weight
    print(reading.weight)

Get the item's units from the scale:

.. code-block:: python

    print(reading.units)

To toggle between units (simulate a button press):

.. code-block:: python

    dymo.toggle_unit_button(switch_unit=True)

To toggle the unit button, but preserve the unit displayed:

.. code-block:: python

    dymo.toggle_unit_button()


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/dymoscale/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_DymoScale/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
