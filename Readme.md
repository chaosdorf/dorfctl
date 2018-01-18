# Dorfctl - A CLI for dorfmap

## Bugs and enhancements

For bug reports or enhancements, please open an [issue](https://github.com/A2nkF/dorfctl/issues) here.

## Installation

`sudo pip3 install -r requirements.txt`


## Usage

`./dorfctl.py [enable|disable|toggle|do] <device> [-h]`

Use 'do' for shutdown and wakeup.
You can't toggle amp's yet.

## Examples

Enable something

`./dorfctl.py enable regal1`

`./dorfctl.py enable tische`

Shutdown

`./dorfctl.py do shutdown`

`./dorfctl.py do wakeup`

Use presets

`./dorfctl.py Lounge hell`

## Targets

-----------------------------------------
List of targets:

    Shortcuts:
        shutdown
        wakeup
        amps

    Presets:
        hackcenter_weiss
        hackcenter_blau

    Devices:
        hackcenter
        rotlicht
        lounge
        regal1
        regal2
        regal3
        regal4
        regal5
        regal6
        regal7
        regal8
        treppe
        garderobe
        treppe_bild
        roere
        blau
        spiegelsäule
        putzlicht
        amp0
        amp1
        amp2
        amp3
        monitore links
        monitore rechts
        screen
        usb_charger
        logo
        ossendorf
------------------------------------------
## TODO

List of all devices
