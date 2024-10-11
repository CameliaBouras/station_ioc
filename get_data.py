#!/usr/bin/env python3
import os
import json

DATA_BASE = "/home/pi/Desktop/ioc_BOURAS/BDDtoWEB.txt"

def readfile(filename):
    if not os.path.isfile(filename):
        return {"lum": 0, "btn": 0}

    with open(filename, "r") as file:
        lines = file.readlines()
        lum = lines[0].split(": ")[1].strip().replace("%", "")
        btn = lines[1].split(": ")[1].strip()
        return {"lum": lum, "btn": btn}

print("Content-Type: application/json")
print()

data = readfile(DATA_BASE)
print(json.dumps(data))
