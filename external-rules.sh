#! /usr/bin/env python3

import sys
import subprocess

# Use this function for debugging
def debugStuff(outputStr):
    with open('/home/doug/.externalrules.log', 'a') as myfile:
        myfile.write(outputStr + '\n\n')

args = sys.argv
window_id = args[1]

props_raw = [x.split('=') for x in
         subprocess.check_output(['xprop', '-id', str(window_id)]).decode('utf-8').split('\n')]
props = {}

for p in props_raw:
    if len(p) != 2:
        continue
    props[p[0].strip()] = p[1].strip().replace('"', '')

#
# RULES
#

wmstr = props.get('WM_NAME(STRING)', None)

# Firefox Picture-In-Picture mode
if  wmstr == 'Picture-in-Picture':
    print('sticky=true state=floating sticky')
