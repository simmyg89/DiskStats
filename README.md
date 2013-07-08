DiskStats
=========

Better linux diskstats visualization


Usage:

diskstats.py -h
```
usage: diskstats.py [-h] [-s SPACES] [-i IGNORE_DEVS] [-o ONLY_DEV] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -s SPACES, --spaces SPACES
                        Spaces between colums
  -i IGNORE_DEVS, --ignore IGNORE_DEVS
                        Devices to ignore comma separated
  -o ONLY_DEV, --only ONLY_DEV
                        Only show the specified device
  -l, --legend          Show columns legend
```

diskstats.py
```
 n_ma   n_mi         dev   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
  179      0     mmcblk0    2573     6110       100586         7560   247098   262131      4372624     16703790         0       6372710      16709440
  179      1   mmcblk0p1       0        0            0            0        0        0            0            0         0             0             0
  179      2   mmcblk0p2    2397     5365        91652         6900       60       71         1048        17080         0         10470         23950
  179      3   mmcblk0p3     175      745         8926          660   247038   262060      4371576     16686710         0       6362950      16685490
  179      4   mmcblk0p4       0        0            0            0        0        0            0            0         0             0             0
```

diskstats.py -l
```
LEGEND :
n_ma         -> Node Major
n_mi         -> Node Minor
dev          -> Device
reads        -> Reads Issued
rd_mrg       -> Reads Merged
rd_sectors   -> Sectors Read
ms_reading   -> Milliseconds Spent Reading
writes       -> Writes Completed
wr_mrg       -> Writes Merged
wr_sectors   -> Sectors Written
ms_writing   -> Milliseconds Spent Writing
cur_ios      -> I/Os currently in Progress
ms_doing_io  -> Milliseconds Spent Doing I/Os
ms_weighted  -> Weighted Milliseconds Spent Doing I/Os

 n_ma   n_mi         dev   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
  179      0     mmcblk0    2573     6110       100586         7560   247098   262131      4372624     16703790         0       6372710      16709440
  179      1   mmcblk0p1       0        0            0            0        0        0            0            0         0             0             0
  179      2   mmcblk0p2    2397     5365        91652         6900       60       71         1048        17080         0         10470         23950
  179      3   mmcblk0p3     175      745         8926          660   247038   262060      4371576     16686710         0       6362950      16685490
  179      4   mmcblk0p4       0        0            0            0        0        0            0            0         0             0             0
```
