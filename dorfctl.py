#!/usr/bin/env python3

import requests
import json
import sys
import argparse
import tabulate
from bidict import bidict

parser = argparse.ArgumentParser(
    usage='./%(prog)s [enable|disable|toggle|do|status] <target> [-h]',
    formatter_class = argparse.RawDescriptionHelpFormatter,
    description="""Examples:

    Enable something

    ./dorfctl.py enable regal1

    ./dorfctl.py enable tische

    Shutdown

    ./dorfctl.py do shutdown

    ./dorfctl.py do wakeup

    Use presets

    ./dorfctl.py Lounge hell

    Check the status

    ./dorfctl.py status rotlicht

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
    """
)
#parser.add_argument('-l', help="Display possible targets")
parser.add_argument('command', help="Specify what you want to do.")
parser.add_argument('target', help="Specify the target.")
args = parser.parse_args()


command = args.command
target = args.target

command_dict = {
    "status":"status",
    "enable": "on",
    "disable": "off",
    "toggle": "toggle",
    'do': ''
}

status_dict = {
    "1":" is on",
    "0":" is off",
    "-1":" does not exist"
}

trans_dict = bidict({
    "shutdown": "shortcut:shutdown",
    "wakeup": "shortcut:unshutdown",
    "amps": "shortcut:amps",
    "hackcenter": "hackcenter_w",
    "rotlicht": "lounge_t2a",
    "lounge": "lounge_weiss",
    "regal1": "hackcenter_regal1",
    "regal2": "hackcenter_regal2",
    "regal3": "hackcenter_regal3",
    "regal4": "hackcenter_regal4",
    "regal5": "hackcenter_regal5",
    "regal6": "hackcenter_regal6",
    "regal7": "hackcenter_regal7",
    "regal8": "hackcenter_regal8",
    "treppe": "treppe_w",
    "garderobe": "treppe_garderobe",
    "treppe_bild": "treppe_bild",
    "roere": "lounge_roere",
    "blau": "roere_blau",
    "spiegelsäule": "hackcenter_3spot",
    "hackcenter_blau": "hackcenter_blau",
    "hackcenter_weiss": "hackcenter_weiss",
    "putzlicht": "hackcenter_roehre",
    "amp0": "amp0",
    "amp1": "amp1",
    "amp2": "amp2",
    "amp3": "amp3",
    "monitore links": "hackcenter_psu1",
    "monitore rechts": "hackcenter_psu2",
    "screen": "tischerechts",
    "usb_charger": "ubercharger",
    "logo": "logo",
    "ossendorf": "hackcenter_ws2812b"

})

action = "preset"
foo = "preset"

if (command in command_dict):
    target = trans_dict[target]
    parts = target.split(':')
    action = command_dict[command]
    if (len(parts) == 1):
        foo = 'device'
        name = parts[0]
    else:
        name = parts[1] + ' ' + action
        action = parts[0]
        foo = action

else:
    name = ' '.join(sys.argv[1:])

json_dict = {
    "action": action,
}
json_dict[foo] = name.strip()

if(command == "status"):
    foo = target
    r = requests.get('http://dorfmap.chaosdorf.space/get/' + foo)
    bar = str(r.content)
    list(bar)
    print(trans_dict.inv[target] + status_dict[bar[2]])

else:
    r = requests.post('http://dorfmap.chaosdorf.space:80/action', json = json_dict )
    print(json_dict)
    r.raise_for_status()
