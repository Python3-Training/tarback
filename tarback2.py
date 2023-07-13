#!/usr/bin/env python3
'''
Mission: Quickly back-up Linux workstations using range-named archives.
=======
How to use `find` and `tar` to back-up your friendly, neighborhood, disk-delta.
2020/05/19: Updated to support hard-coded 'tagged' Options.locations. Also added the 'all' option.
2023/07/13: Added reporting, as well as 'day-gaps' to automatically backup ANY --key since it's last detected archival.

~~~ How To Re-Use ~~~
(1) Replace Options.locations with YOUR key & path location(s)
(2) Update Options.option with YOUR default key to use
(3) Change Options.DEFAULT_FOLDER to where you want to save your incremental backups
(=) Default invocation will run your default `option`` for the default `days`
(=) May also specify other `{days}` and / or `{option}` from the CLI

TODO: Support runtime `Options.locations` CRUD'ing.
'''
import os
import os.path
import sys
import time
import datetime
from time import strftime
from time import gmtime

class Options:
    DEFAULT_ALL = 'all'
    DEFAULT_OPTIONS_NAME = '/tarback.options'
    DEFAULT_OPTIONS = '.' + DEFAULT_OPTIONS_NAME
    DEFAULT_FOLDER  = '/mnt/c/tmp' # Where I keep MY incrementals

    def __init__(self):
        self.days = 7
        self.overlap = 2 # days to add to gap-days
        self.option = 'd_drive'
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

    def show_locations(self):
        for ss, akey in enumerate(self.locations,1):
            print(f'{ss:>03}.) {akey} = {self.locations[akey]}')

    @staticmethod 
    def Setup(file=DEFAULT_OPTIONS):
        ''' Set-up the reloadable options. '''
        znew = Options()
        cont = True
        print('Step 01: Enter backup locations')
        znew.locations.clear()
        while cont:
            zloc = input("Location: ")
            if not zloc:
                continue
            if zloc in znew.locations.values():
                print("Duplicate location ignored.")
                continue
            if not os.path.isdir(zloc):
                print(f"Unable to locate directory {zloc}")
                continue
            zkey = input('Enter location alias (key): ')
            if not zkey:
                continue
            zkey = zkey.replace(' ', '_')
            zkey = zkey.replace('\t', '_')
            xx = 0
            if zkey in znew.locations:
                zkey2 = zkey
                while zkey2 in znew.locations:
                    xx += 1
                    zkey2 = zkey + str(xx)
                print(f"Key '{zkey}' already used. Renamed to {zkey2}.")
                zkey = zkey2
            znew.locations[zkey] = zloc
            znew.show_locations()
            zyn = input('Done? ').lower()
            if zyn == 'y':
                cont = False

        print("Step 02: Select the default backup key.")
        for ss, zkey in enumerate(znew.locations,1):
            print(f'{ss}.) {zkey}')
        ZALL = ss+1
        print(f'{ZALL}.) ALL')
        znew.option = Options.DEFAULT_ALL
        znum = input(f"Enter default backup key-number: (1-{ZALL}) ")
        try:
            znum = int(znum)
            if znum != ZALL:
                znew.option = list(znew.locations)[znum - 1]
        except:
            pass

        print("Step 03: Select existing folder for default archive location.")
        while True:
            zloc = input('Default archive storage folder: ')
            if zloc and os.path.isdir(zloc):
                if zloc in znew.locations.values():
                    print("WARNING: Archive output is also a backup path.")
                    zyn = input("Would you like to change that? [y/N] ").lower()
                    if zyn == 'y':
                        continue
                znew.root = zloc
                break
            else:
                print('Invalid location. Ignored.')
        
        print("Step 04: Default days to backup.")
        znum = input("Enter number of days to include: ")
        try:
            znum = int(znum)
            znew.days = znum
        except:
            print(f'Invalid number. Using {znew.days} days.')
        while True:
            do_report(znew)
            zyn = input("Correct? [y/N] ").lower()
            if zyn == 'y':
                if znew.save():
                    print(f'Options saved to {Options.DEFAULT_OPTIONS}')
                    return znew
                else:
                    print(f'Unable to save options to {Options.DEFAULT_OPTIONS}!')
            elif zyn == 'n':
                break
            print("Please enter 'y' or 'n' ...")
            

    @staticmethod 
    def Load(file=DEFAULT_OPTIONS):
        result = Options()
        if not file:
            return result
        if not os.path.exists(file):
            return result
        with open(file) as fh:
            result.locations.clear()
            print("Reading stored options ...")
            adict =  eval(fh.read())
            for key in adict:
                result.__dict__[key] = adict[key]
        return result

    def save(self, file=DEFAULT_OPTIONS):
        if not file:
            return False
        with open(file, 'w') as fh:
            fh.write(str(self.__dict__))
        return True


def recent_archive_for(zroot, zkey):
    ''' Detect the last archive date for the archive key in the archive root. '''
    delta = False
    zmin = datetime.date(1971,1,2)
    for node in os.listdir(zroot):
        if node.startswith(zkey):
            zdate = node[len(zkey)+1:].split('_')[0]
            zsamp = datetime.date.fromisoformat(zdate)
            if zsamp >= zmin:
                zmin = zsamp
                delta = True
    if not delta:
        return None # it pays to be specific?
    return zmin


def detect_gap(zopts, zkey):
    ''' Detect the earliest archive date in the archive root. '''
    delta = False
    zmin = datetime.date.today()
    if isinstance(zopts, Options):
        if zkey == zopts.DEFAULT_ALL:
            for zloc in zopts.locations:
                ztime = recent_archive_for(zopts.root, zloc)
                if ztime and ztime <= zmin:
                    zmin = ztime
                    delta = True
        else:
            ztime = recent_archive_for(zopts.root, zkey)
            if ztime and ztime <= zmin:
                zmin = ztime
                delta = True
    if not delta:
        return None
    return zmin


def do_report(options):
    ''' Show the state of the archival effort. '''
    print(f'{sys.argv[0]} Configuration:\n')
    print(f'Default days: {options.days}')
    print(f'Storage root: {options.root}')
    print("\nKeyed locations include:")
    for able in options.locations:
        print(f'\t{able} = {options.locations[able]}')
        zlast = detect_gap(options, able)
        if zlast:
            zgap = datetime.date.today() - zlast
            print(f'\t\t\tLast archived on {zlast}, {zgap.days} days ago...')
        else:
            print(f'\t\t\tPrior archive not found...')
    print(f"\t{Options.DEFAULT_ALL} = BACKUP ALL OF THE ABOVE")
    print(f'Default: {options.option}')
    print(f"\nEdit {Options.DEFAULT_OPTIONS} to update.")


def tarback(options):
    ''' The actual archival process. '''
    if not isinstance(options, Options):
        return False, None
    if options.option == Options.DEFAULT_ALL:
        for key in options.locations:
            if key == Options.DEFAULT_ALL:
                continue # Safe coding means 'no accidents'?
            else:
                options.option = key
                tarback(options)
        options.option = Options.DEFAULT_ALL
        return True, Options.DEFAULT_ALL
    if not options.option in options.locations:
        return False, None
    zpath = options.locations[options.option]
    zdate = strftime("%Y-%m-%d", gmtime(time.time()))
    zfile = f'{options.root}/{options.option}_{zdate}_inc_{options.days}.tar'
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
    options = Options.Load()
    if Options.DEFAULT_ALL in options.locations:
        raise Exception(f"Error: Reserved dictionary location '{Options.DEFAULT_ALL}'")
    if len(sys.argv) >= 2:
        try:
            import argparse
            parser = argparse.ArgumentParser()
            parser.add_argument('--default', help='use hard-coded configuration', action='store_true', required=False)
            parser.add_argument('--config', help='custome configure', action='store_true', required=False)
            parser.add_argument('--days', help='number of archive days', type=int, default=options.days)
            parser.add_argument('--key', help='location alias', default=options.option, required=False)
            parser.add_argument('--info', help='show configuration', action='store_true', required=False)
            parser.add_argument('--gap', help='attempt days-since detection', action='store_true', required=False)
            results = parser.parse_args()
            options.days = results.days
            options.option = results.key
            if results.default:
                print("Reloading default configuration.")
                options = Options()
                options.save()
                print("Default configuration saved.")
                exit()
            if results.config:
                Options.Setup()
                exit()
            if results.info:
                do_report(options)
                exit()
            if results.key == Options.DEFAULT_ALL:
                print('... backing it all up ...!')
            elif results.key not in options.locations:
                raise Exception(f"Error: '{results.key}' not a key in {options.locations} ...")
            if results.gap:
                zthen = detect_gap(options, results.key)
                if zthen:
                    zdate = datetime.date.today() - zthen
                    options.days = zdate.days + options.overlap
        except Exception as ex:
            raise ex
            
    print(f"Find: Backing-up '{options.option}' for the past {options.days} days.")
    response = tarback(options)
    if response[0] is False:
        print(f'Error: Unable to create {response[1]}')
    else:
        print(f"\nBacked-up '{options.option}' for the past {options.days} days!")
        print(f'\nSuccess: Archive saved to {response[1]} ...')
    print(*response)
