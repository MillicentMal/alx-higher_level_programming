#!/usr/bin/python3
"""
make a get request to a given url and return the 
body
"""
import urllib.request

r= urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(r) as response:
    response = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(response))) 
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode("utf-8")))

