#!/usr/bin/python3
"""Status 
"""

import requests

r = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print("\t -type: {}".format(type(r.text)))
print("\t -content: {}".format(r.status_code))

