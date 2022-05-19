#!/usr/bin/env python3
'''
How to use `find` and `tar` to back-up your friendly, neighborhood, disk-delta.
2021/07/04: Created.
2020/05/19: Updated to support hard-coded 'tagged' Options.locations. Also added the 'all' option.

TODO: Support runtime `Options.locations` CRUD'ing.
'''
import os
import os.path
import sys
import time
from time import strftime
from time import gmtime

class Options:
    DEFAULT_ALL = 'all'
    DEFAULT_OPTIONS = './tarback.options'
    DEFAULT_FOLDER  = '/mnt/c/tmp' # Where I keep MY incrementals

    def __init__(self):
        self.days = 7
        self.root = Options.DEFAULT_FOLDER
        self.locations = { # A good-many devices!
            'd_drive':'/mnt/c/d_drive',
            'd_vidprod':'/mnt/c/d_vidprod',
            'd_optional':'/mnt/c/d_optional',
            'd_archive':'/mnt/e/d_archive',
            'd_assets':'/mnt/e/d_assets',
            'd_archive_static':'/mnt/e/d_archive_static',
            'd_archive_media':'/mnt/e/d_archive_media',
            }
    
    @staticmethod 
    def Load(file=DEFAULT_OPTIONS):
        if not file or not os.path.exists(file):
            return Options()
        with open(file) as fh:
            return eval(fh.read())

    def save(self, file=DEFAULT_OPTIONS):
        if not file:
            return False
        with open(file, 'w') as fh:
            fh.write(self.__dict__)
        return True


def tarback(options, zkey='default'):
    if not isinstance(options, Options):
        return False, None
    if zkey == Options.DEFAULT_ALL:
        for key in options.locations:
            tarback(options, key)
        return True, Options.DEFAULT_ALL
    if not zkey in options.locations:
        return False, None
    zpath = options.locations[zkey]
    zdate = strftime("%Y-%m-%d", gmtime(time.time()))
    zfile = f'{options.root}/{zkey}_{zdate}_inc{options.days}.tar'
    if not zpath or options.days < 1:
        return False, zfile
    zcmd = f'find {zpath} -type f -mtime -{options.days} | tar -cvf {zfile} -T -'
    print('START:', zcmd)
    print('~*' * 10)
    bOk = False # New!
    with os.popen(zcmd, 'r') as proc:
        for ss, line in enumerate(proc, 1):
            bOk = True
            print(f'{ss}.)',line, end='')
    print('EXIT', zcmd)
    return bOk, zfile


if __name__ == '__main__':
    option = 'default'
    options = Options.Load()
    if Options.DEFAULT_ALL in options.locations:
        raise Exception(f"Error: Reserved dictionary location '{Options.DEFAULT_ALL}'")
    if len(sys.argv) >= 2:
        try:
            import argparse
            parser = argparse.ArgumentParser()
            parser.add_argument('days', help='number of archive days', type=int, default=options.days)
            parser.add_argument('key', help='location alias', default='default')
            results = parser.parse_args()
            options.days = results.days
            if results.key == Options.DEFAULT_ALL:
                print('... backing it all up ...!')
            elif results.key not in options.locations:
                raise Exception(f"Error: '{results.key}' not in [{options.keys}]")
            option = results.key

        except Exception as ex:
            raise ex
            
    print(f"Find: Backing-up '{option}' for the past {options.days} days.")
    response = tarback(options, option)
    if response[0] is False:
        print(f'Error: Unable to create {response[1]}')
    else:
        print(f'Success: Archive saved to {response[1]} ...')
    print(*response)
