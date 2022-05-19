#!/usr/bin/env python3
'''
How to use `find` and `tar` to back-up your friendly, neighborhood, disk-delta.
2021/07/04: Created.
'''
import sys

def tarback(zdays, zpath):
    import os
    import os.path
    import time
    from time import strftime
    from time import gmtime
    zdate = strftime("%Y-%m-%d", gmtime(time.time()))
    zfile = f'~/Desktop/{zdate}_inc{zdays}.tar'
    if not zpath or zdays < 1:
        return False, zfile
    zcmd = f'find {zpath} -type f -mtime -{zdays} | tar -cvf {zfile} -T -'
    print('START:', zcmd)
    print('~*' * 10)
    bOk = False
    with os.popen(zcmd, 'r') as proc:
        for ss, line in enumerate(proc, 1):
            bOk = True
            print(f'{ss}.)',line, end='')
    print('EXIT', zcmd)
    return bOk, zfile

zdays = 7
if len(sys.argv) == 2:
    try:
        zdays = int(sys.argv[1])
    except:
        print(f"Usage: {sys.argv[0]} number_of_days")
        
print(f"Find: Backing-up the past {zdays} days.")
response = tarback(zdays, '/d_drive')
if response[0] is False:
    print(f'Error: Unable to create {response[1]}')
else:
    print(f'Success: Archive saved to {response[1]} ...')
print(*response)
