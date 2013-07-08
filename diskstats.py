#!/usr/bin/env python

from optparse import OptionParser


def ignore_callback(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))

parser = OptionParser()
parser.add_option('-s', '--spaces', type='int', dest='SPACES', default=0, help='Spaces between colums')
parser.add_option('-i', '--ignore', type='string', dest='IGNORE_DEVS', default=['loop', 'ram'], help='Devices to ignore', action='callback', callback=ignore_callback)
parser.add_option('-o', '--only', dest='ONLY_DEV', help='Only show the specified device')
(options, args) = parser.parse_args()

#print 'options: %s' % options.__dict__
#print 'args: %s' % args

SPACES = int(options.__dict__.get('SPACES'))
IGNORE_DEVS = options.__dict__.get('IGNORE_DEVS')
ONLY_DEV = options.__dict__.get('ONLY_DEV')

#print 'SPACES: %s' % SPACES
#print 'IGNORE_DEVS: %s' % IGNORE_DEVS
#print 'ONLY_DEV: %s' % ONLY_DEV

dsfp = open('/proc/diskstats', 'rb')
ds = dsfp.read().split('\n')

header = {
    0: {'h': 'm', 'l': 1},
    1: {'h': 'm', 'l': 1},
    2: {'h': 'dev', 'l': 3},
    3: {'h': 'reads', 'l': 5},
    4: {'h': 'rd_mrg', 'l': 6},
    5: {'h': 'rd_sectors', 'l': 10},
    6: {'h': 'ms_reading', 'l': 10},
    7: {'h': 'writes', 'l': 6},
    8: {'h': 'wr_mrg', 'l': 6},
    9: {'h': 'wr_sectors', 'l': 10},
    10: {'h': 'ms_writing', 'l': 10},
    11: {'h': 'cur_ios', 'l': 7},
    12: {'h': 'ms_doing_io', 'l': 11},
    13: {'h': 'ms_weighted', 'l': 11},
}
#print header

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
