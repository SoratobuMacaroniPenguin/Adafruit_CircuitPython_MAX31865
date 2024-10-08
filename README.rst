write SoratobuMacaroniPenguin

I hope to use Adafruit MAX31865 compatible on Wemos mini and Micropython 

/examples/MAX31865_simpletest.py and MAX31865.py library used simple tempature 

+ Wemos mini compatible (ESP8266)
+ Adafruit MAX31865 compatible
+ Micropython-1.23.0

============

Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-max31865/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/max31865/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_MAX31865/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_MAX31865/actions/
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython module for the MAX31865 thermocouple amplifier.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-max31865/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-max31865

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-max31865

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install adafruit-circuitpython-max31865


Usage Example
=============

See examples/max31865_simpletest.py for a demo of the usage.

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/max31865/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_max31865/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
