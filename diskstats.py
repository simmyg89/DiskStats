#!/usr/bin/env python

import argparse


class ignore_callback(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, value.split(','))

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--spaces', type=int, dest='SPACES', default=0, help='Spaces between colums')
parser.add_argument('-i', '--ignore', type=str, dest='IGNORE_DEVS', default=['loop', 'ram'], help='Devices to ignore', action=ignore_callback)
parser.add_argument('-o', '--only', dest='ONLY_DEV', help='Only show the specified device')
parser.add_argument('-l', '--legend', dest='LEGEND', default=False, action="store_true", help='Show columns legend')
args = parser.parse_args()

#print 'args: %s' % args

SPACES = int(args.__dict__.get('SPACES'))
IGNORE_DEVS = args.__dict__.get('IGNORE_DEVS')
ONLY_DEV = args.__dict__.get('ONLY_DEV')
LEGEND = args.__dict__.get('LEGEND')

#print 'SPACES: %s' % SPACES
#print 'IGNORE_DEVS: %s' % IGNORE_DEVS
#print 'ONLY_DEV: %s' % ONLY_DEV
#print 'LEGEND: %s' % LEGEND

try:
    dsfp = open('/proc/diskstats', 'rb')
    ds = dsfp.read().split('\n')
    dsfp.close()

except IOError:
    print 'Cannot open /proc/diskstats'
    exit(0)

header = {
    0: {'h': 'n_ma', 'l': 4, 'd': 'Node Major'},
    1: {'h': 'n_mi', 'l': 4, 'd': 'Node Minor'},
    2: {'h': 'dev', 'l': 3, 'd': 'Device'},
    3: {'h': 'reads', 'l': 5, 'd': 'Reads Issued'},
    4: {'h': 'rd_mrg', 'l': 6, 'd': 'Reads Merged'},
    5: {'h': 'rd_sectors', 'l': 10, 'd': 'Sectors Read'},
    6: {'h': 'ms_reading', 'l': 10, 'd': 'Milliseconds Spent Reading'},
    7: {'h': 'writes', 'l': 6, 'd': 'Writes Completed'},
    8: {'h': 'wr_mrg', 'l': 6, 'd': 'Writes Merged'},
    9: {'h': 'wr_sectors', 'l': 10, 'd': 'Sectors Written'},
    10: {'h': 'ms_writing', 'l': 10, 'd': 'Milliseconds Spent Writing'},
    11: {'h': 'cur_ios', 'l': 7, 'd': 'I/Os currently in Progress'},
    12: {'h': 'ms_doing_io', 'l': 11, 'd': 'Milliseconds Spent Doing I/Os'},
    13: {'h': 'ms_weighted', 'l': 11, 'd': 'Weighted Milliseconds Spent Doing I/Os '},
}
#print header

if LEGEND:
    print ''
    print 'LEGEND :'
    maxl = max([header[x]['l'] for x in header])
    for p in header:
        print '%s' % header[p]['h'],
        print ' ' * (maxl - len(header[p]['h'])),
        print '-> %s' % header[p]['d']

disks = {}

for disk in ds:
    diskdict = {}
    for p in disk.split(' '):
        if p != '':
            #print 'p = -%s-' % p
            if header[len(diskdict)]['l'] < len(p):
                header[len(diskdict)]['l'] = len(p)
            diskdict[len(diskdict)] = p
            
    if diskdict.get(2, None) is not None:
        if ONLY_DEV is not None and not ONLY_DEV == '':
            if ONLY_DEV in diskdict[2]:
                disks[diskdict[2]] = diskdict
        elif not any(id in diskdict[2] for id in IGNORE_DEVS):
            disks[diskdict[2]] = diskdict

print ''

for p in header:
    #print 'p = -%s-' % p
    print ' ' * (header[p]['l'] - len(header[p]['h'])),
    print '%s' % header[p]['h'],
    print ' ' * SPACES,
print ''
    
for d in sorted(disks, key=lambda x: disks[x][2]):
    for p in disks[d]:
        #print 'p = -%s-' % p
        print ' ' * (header[p]['l'] - len(disks[d][p])),
        print '%s' % disks[d][p],
        print ' ' * SPACES,
    print ''

print ''
