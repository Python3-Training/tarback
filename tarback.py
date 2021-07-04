#!/usr/bin/env python3
'''
How to use `find` and `tar` to back-up your friendly, neighborhood, disk-delta.
'''
import sys

def tarback(zdays):
    import os
    import time
    from time import strftime
    from time import gmtime
    zdate = strftime("%Y-%m-%d", gmtime(time.time()))
    zcmd = f'find /d_drive -type f -mtime -{zdays} | tar -cvf ~/Desktop/{zdate}_inc.tar -T - '
    print('START:', zdate)
    print('~*' * 10)
    proc = os.popen(zcmd, 'r')
    for ss, line in enumerate(proc, 1):
        print(f'{ss}.)',line, end='')
    print('~*' * 10)
    print(zdate, f'{sys.argv[0]} DONE.', sep=': ')
    print(f'   [{zcmd}]')

zdays = 7
if len(sys.argv) == 2:
    try:
        zdays = int(sys.argv[1])
    except:
        print(f"Usage: {sys.argv[0]} number_of_days")
        
print(f"Find: Backing-up the past {zdays} days.")
tarback(zdays)
