#!/usr/bin/env python3
'''
Mission: Test our SELECTIVE save / restore of tarback2 Options.
'''
import sys
sys.path.insert(0, '../tarback')

import os
import os.path

TC_FILE01 = "./~TC_File01.tmp"

if os.path.exists(TC_FILE01):
    os.unlink(TC_FILE01)

import tarback2

case01 = tarback2.Options()
case01.days = 123

case01.save(TC_FILE01)
case01b = tarback2.Options.Load(TC_FILE01)

for key in case01.locations:
    if key not in case01b.locations:
        raise Exception("Error: Load / Save Error.")

if case01.days != case01b.days:
    raise Exception("Error: Days did not save / restore properly?")

if os.path.exists(TC_FILE01):
    os.unlink(TC_FILE01)

print("Testing Success.")
