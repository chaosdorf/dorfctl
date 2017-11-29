# This is our CLI for Dorfmap
#!/usr/bin/env

import requests
import json
import sys

status = sys.argv[1]
device = sys.argv[2]
#print(sys.argv)

trans_dict = {
    "enable": "on",
    "disable": "off",
    "toggle": "toggle",
    #
    "hackcenter": "hackcenter_w",
    "rotlicht": "lounge_t2a",
    "lounge": "lounge_weiss",
    "regal1": "hackcenter_regal1",
    "regal2": "hackcenter_regal2",
    "regal3": "hackcenter_regal3",
    "regal4": "hackcenter_regal4",
    "regal5": "hackcenter_regal5",
    "regal6": "hackcenter_regal6",
    


}
#print(trans_dict[user_input])
json_dict = {
    "action": trans_dict[status],
    "device": trans_dict[device]
}

r = requests.post('http://dorfmap.chaosdorf.space:80/action', json = json_dict )
r.raise_for_status()
