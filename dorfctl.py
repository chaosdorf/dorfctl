# This is our CLI for Dorfmap
#!/usr/bin/env

import requests
import json
import sys

status = sys.argv[1]
device = sys.argv[2]
#print(sys.argv)

status_dict = {
    "enable": "on",
    "disable": "off",
    "toggle": "toggle",
}

trans_dict = {

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
    "roere": "loung_roere",
    "blau": "roere_blau",
    "spiegelsäule": "hackcenter_3spot",
    "hackcenter_blau": "hackcenter_blau",
    "hackcenter_weiss": "hackcenter_weiss",
    "putzlicht": "hackcenter_roehre",
    "amp0": "amp0",
    "amp0": "amp0",
    "amp1": "amp1",
    "amp2": "amp2",
    "amp2": "amp2",
    "amp3": "amp3",
    "amp3": "amp3",
    "monitore links": "hackcenter_psu1",
    "monitore rechts": "hackcenter_psu2",
    "tische": "tischerechts",
    "usb_charger": "ubercharger",


}
action = "preset"
foo = "preset"

if (status in status_dict):
    target = trans_dict[device]
    parts = target.split(':')
    action = status_dict[status]
    if (len(parts) == 1):
        foo = 'device'
        name = parts[0]
    else:
        name = parts[1] + ' ' + action
        action = parts[0]
        foo = action
else:
    name = ' '.join(sys.argv[1:])


#print(trans_dict[user_input])
json_dict = {
    "action": action,
}
json_dict[foo] = name
print(json_dict)
r = requests.post('http://dorfmap.chaosdorf.space:80/action', json = json_dict )
r.raise_for_status()
