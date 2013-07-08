#!/usr/bin/env python

import os
import copy
import time
import argparse
from datetime import datetime


class DiskStats_Param(object):

    name = ''
    name_lenght = 0
    lenght = 0
    description = ''
    first_value = None
    last_value = None
    cur_value = None

    def __init__(self, name='', description=''):
        super(DiskStats_Param, self).__init__()

        self.name = name
        self.name_lenght = len(name)
        self.lenght = len(name)
        self.description = description

    def set_value(self, value):

        if self.first_value is None:
            self.first_value = int(copy.deepcopy(value))
        if self.cur_value is not None:
            self.last_value = int(copy.deepcopy(self.cur_value))
        self.cur_value = int(copy.deepcopy(value))

        self.lenght = max([len(str(x)) for x in [self.first_value, self.last_value, self.cur_value] if x is not None] + [self.name_lenght])

        return value

    def get_first_value(self):

        return self.first_value

    def get_last_value(self):

        return self.last_value

    def get_value(self):

        return self.cur_value

    def get_name_lenght(self):

        return self.name_lenght

    def get_lenght(self):

        return self.lenght

    def __str__(self):

        return '%s - %s' % (self.name, self.cur_value)


class DiskStats_DiskParams(object):

    def __init__(self, name=''):
        super(DiskStats_DiskParams, self).__init__()

        self.__diskname = name

        self.__params = {
            #'n_ma': DiskStats_Param('n_ma', 'Node Major'),
            #'n_mi': DiskStats_Param('n_mi', 'Node Minor'),
            #'dev': DiskStats_Param('dev', 'Device'),
            'reads': DiskStats_Param('reads', 'Reads Issued'),
            'rd_mrg': DiskStats_Param('rd_mrg', 'Reads Merged'),
            'rd_sectors': DiskStats_Param('rd_sectors', 'Sectors Read'),
            'ms_reading': DiskStats_Param('ms_reading', 'Milliseconds Spent Reading'),
            'writes': DiskStats_Param('writes', 'Writes Completed'),
            'wr_mrg': DiskStats_Param('wr_mrg', 'Writes Merged'),
            'wr_sectors': DiskStats_Param('wr_sectors', 'Sectors Written'),
            'ms_writing': DiskStats_Param('ms_writing', 'Milliseconds Spent Writing'),
            #'cur_ios': DiskStats_Param('cur_ios', 'I/Os currently in Progress'),
            'ms_doing_io': DiskStats_Param('ms_doing_io', 'Milliseconds Spent Doing I/Os'),
            'ms_weighted': DiskStats_Param('ms_weighted', 'Weighted Milliseconds Spent Doing I/Os'),
        }

        self.__params_pos = {
            #0: 'n_ma',
            #1: 'n_mi',
            #2: 'dev',
            3: 'reads',
            4: 'rd_mrg',
            5: 'rd_sectors',
            6: 'ms_reading',
            7: 'writes',
            8: 'wr_mrg',
            9: 'wr_sectors',
            10: 'ms_writing',
            #11: 'cur_ios',
            12: 'ms_doing_io',
            13: 'ms_weighted',
        }

    def params_list(self):

        return [self.__params_pos[x] for x in self.__params_pos]

    def get_param_position(self, position):

        if position in self.__params_pos.keys():
            return self.__params[self.__params_pos[position]]
        return None

    def get_param_name(self, name):

        if name in self.__params.keys():
            return self.__params[name]
        return None

    def set_value_position(self, position, value):

        if position in self.__params_pos.keys():
            self.__params[self.__params_pos[position]].set_value(value)
            return value
        return None

    def get_value_position(self, position):

        if position in self.__params_pos.keys():
            return self.__params[self.__params_pos[position]].get_value()
        return None

    def get_first_value_position(self, position):

        if position in self.__params_pos.keys():
            return self.__params[self.__params_pos[position]].get_first_value()
        return None

    def set_value_name(self, name, value):

        if name in self.__params.keys():
            self.__params[name].set_value(value)
            return value
        return None

    def get_value_name(self, name):

        if name in self.__params.keys():
            return self.__params[name].get_value()
        return None

    def get_first_value_name(self, name):

        if name in self.__params.keys():
            return self.__params[name].get_first_value()
        return None


class DiskStats_Disks(object):

    __disks = {}

    def __str__(self):

        return '%s' % str(self.get_disks())

    def params_list(self):

        return DiskStats_DiskParams().params_list()

    def max_param_name_lenght(self, name):

        return max([self.__disks[disk].get_param_name(name).get_lenght() for disk in self.__disks])

    def max_param_position_lenght(self, position):

        return max([self.__disks[disk].get_param_position(position).get_lenght() for disk in self.__disks])

    def add_disk(self, disk):

        if not disk in self.__disks.keys():
            self.__disks[disk] = DiskStats_DiskParams(disk)

    def get_disks(self):

        return [x for x in self.__disks]

    def set_disk_param_position(self, disk, position, value):

        self.add_disk(disk)
        if disk in self.__disks.keys():
            self.__disks[disk].set_value_position(position, value)
            return value
        return None

    def get_disk_param_position(self, disk, position):

        self.add_disk(disk)
        if disk in self.__disks.keys():
            return self.__disks[disk].get_value_position(position)
        return None

    def get_disk_first_param_position(self, disk, position):

        self.add_disk(disk)
        if disk in self.__disks.keys():
            return self.__disks[disk].get_first_value_position(position)
        return None

    def set_disk_param_name(self, disk, name, value):

        self.add_disk(disk)
        if disk in self.__disks.keys():
            self.__disks[disk].set_value_name(name, value)
            return value
        return None

    def get_disk_param_name(self, disk, name):

        self.add_disk(disk)
        if disk in self.__disks.keys():
            return self.__disks[disk].get_value_name(name)
        return None

    def get_disk_first_param_name(self, disk, name):

        self.add_disk(disk)
        if disk in self.__disks.keys():
            return self.__disks[disk].get_first_value_name(name)
        return None


class DiskStats(object):

    def __init__(self, SPACES=0, IGNORE_DEVS=None, ONLY_DEVS=None, LEGEND=False):
        super(DiskStats, self).__init__()

        if not isinstance(IGNORE_DEVS, (list, tuple)):
            IGNORE_DEVS = []

        if not isinstance(ONLY_DEVS, (list, tuple)):
            ONLY_DEVS = None

        self.SPACES = SPACES
        self.IGNORE_DEVS = IGNORE_DEVS
        self.ONLY_DEVS = ONLY_DEVS
        self.LEGEND = LEGEND

        self.disks = DiskStats_Disks()

    def read(self):

        ds = ''
        try:
            #dsfp = open('diskstats_test', 'rb')
            dsfp = open('/proc/diskstats', 'rb')
            ds = dsfp.read().split('\n')
            dsfp.close()
        except IOError:
            print 'Cannot open /proc/diskstats'
            exit(0)

        for disk in ds:
            diskdict = {}
            for p in disk.split(' '):
                if p != '':
                    #if self.params[len(diskdict)].lenght < len(p):
                    #    self.params[len(diskdict)].max_lenght = len(p)
                    diskdict[len(diskdict)] = p

            if diskdict.get(2, None) is not None:

                if not any(ign in diskdict[2] for ign in self.IGNORE_DEVS):
                    if self.ONLY_DEVS is None or (self.ONLY_DEVS is not None and any(only in diskdict[2] for only in self.ONLY_DEVS)):
                        self.disks.add_disk(diskdict[2])
                        for p in diskdict:
                            self.disks.set_disk_param_position(diskdict[2], p, diskdict[p])

        #print 'disks: %s' % self.disks

    def legend(self):

        dp = DiskStats_DiskParams()

        if self.LEGEND:
            print ''
            print 'LEGEND :'
            plist = dp.params_list()
            maxl = max([dp.get_param_name(p).get_name_lenght() for p in plist])
            for p in plist:
                print '%s' % dp.get_param_name(p).name,
                print ' ' * (maxl - dp.get_param_name(p).get_name_lenght()),
                print '-> %s' % dp.get_param_name(p).description
            print ''

    def show(self):

        dp = DiskStats_DiskParams()

        self.legend()

        dev_name = 'Device'

        max_dev_name = max([len(str(x)) for x in self.disks.get_disks()] + [len(dev_name)])

        print ' ' * (max_dev_name - len(dev_name)),
        print '%s' % dev_name,
        print ' ' * self.SPACES,
        for p in dp.params_list():
            print ' ' * (self.disks.max_param_name_lenght(p) - dp.get_param_name(p).get_name_lenght()),
            print '%s' % dp.get_param_name(p).name,
            print ' ' * self.SPACES,
        print ''

        for d in sorted(self.disks.get_disks()):
            print ' ' * (max_dev_name - len(str(d))),
            print '%s' % d,
            print ' ' * self.SPACES,
            for p in dp.params_list():
                print ' ' * (self.disks.max_param_name_lenght(p) - len(str(self.disks.get_disk_param_name(d, p)))),
                print '%s' % self.disks.get_disk_param_name(d, p),
                print ' ' * self.SPACES,
            print ''

        print ''

    def realtime(self, cicles=5, wait=5):

        dp = DiskStats_DiskParams()

        self.read()
        first_dt = datetime.now()
        self.show()

        while not cicles == 0:

            cicles -= 1

            time.sleep(wait)

            os.system('clear')
            print 'First reading: %s' % first_dt
            self.read()
            print 'Current reading: %s' % datetime.now()
            print ''

            for d in sorted(self.disks.get_disks()):
                print 'Disk: %s' % d

                print '     ',

                for p in dp.params_list():
                    print ' ' * (self.disks.max_param_name_lenght(p) - dp.get_param_name(p).get_name_lenght()),
                    print '%s' % dp.get_param_name(p).name,
                    print ' ' * self.SPACES,
                print ''

                print 'FIRST',

                for p in dp.params_list():
                    print ' ' * (self.disks.max_param_name_lenght(p) - len(str(self.disks.get_disk_first_param_name(d, p)))),
                    print '%s' % self.disks.get_disk_first_param_name(d, p),
                    print ' ' * self.SPACES,
                print ''

                print 'CURR ',

                for p in dp.params_list():
                    print ' ' * (self.disks.max_param_name_lenght(p) - len(str(self.disks.get_disk_param_name(d, p)))),
                    print '%s' % self.disks.get_disk_param_name(d, p),
                    print ' ' * self.SPACES,
                print ''

                print 'DIFF ',

                for p in dp.params_list():
                    diff = self.disks.get_disk_param_name(d, p) - self.disks.get_disk_first_param_name(d, p)
                    print ' ' * (self.disks.max_param_name_lenght(p) - len(str(diff))),
                    print '\033[1;41m%s\033[1;m' % diff if diff != 0 else '%s' % diff,
                    print ' ' * self.SPACES,
                print '\n'


if __name__ == '__main__':

    class split_action(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, values.split(','))

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--spaces', type=int, dest='SPACES', default=0, help='Spaces between colums')
    parser.add_argument('-i', '--ignore', type=str, dest='IGNORE_DEVS', default=['loop', 'ram'], help='Devices to ignore, comma separated; default=loop,ram', action=split_action)
    parser.add_argument('-o', '--only', type=str, dest='ONLY_DEVS', default=None, help='Only show the specified devices, comma separated', action=split_action)
    parser.add_argument('-l', '--legend', dest='LEGEND', default=False, action="store_true", help='Show columns legend')
    parser.add_argument('-r', '--realtime', dest='REALTIME', default=False, action="store_true", help='Realtime Monitoring')
    parser.add_argument('-c', '--cicles', type=int, dest='CICLES', default=5, help='Realtime Cicles, -1 mean infinite')
    parser.add_argument('-w', '--wait', type=int, dest='WAIT', default=5, help='Realtime Cicles Wait in seconds')
    args = parser.parse_args()

    #print 'args: %s' % args

    SPACES = int(args.__dict__.get('SPACES'))
    IGNORE_DEVS = args.__dict__.get('IGNORE_DEVS')
    ONLY_DEVS = args.__dict__.get('ONLY_DEVS')
    LEGEND = args.__dict__.get('LEGEND')
    REALTIME = args.__dict__.get('REALTIME')
    CICLES = int(args.__dict__.get('CICLES'))
    WAIT = int(args.__dict__.get('WAIT'))

    #print 'SPACES: %s' % SPACES
    #print 'IGNORE_DEVS: %s' % IGNORE_DEVS
    #print 'ONLY_DEVS: %s' % ONLY_DEVS
    #print 'LEGEND: %s' % LEGEND
    #print 'REALTIME: %s' % REALTIME
    #print 'CICLES: %s' % CICLES
    #print 'WAIT: %s' % WAIT

    ds = DiskStats(SPACES, IGNORE_DEVS, ONLY_DEVS, LEGEND)

    if REALTIME:
        ds.realtime(CICLES, WAIT)

    else:
        ds.read()
        ds.show()
