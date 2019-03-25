#!/usr/bin/env python3

# Antonio Karlo Mijares

from fabric.api import *

# Will get the hostname of this worker:
def getHostname():
    name = run("hostname")
    print(name)