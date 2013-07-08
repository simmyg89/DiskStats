DiskStats
=========

Better linux diskstats visualization


Usage:

diskstats.py -h
```
usage: diskstats.py [-h] [-s SPACES] [-i IGNORE_DEVS] [-o ONLY_DEVS] [-l] [-r]
                    [-c CICLES] [-w WAIT]

optional arguments:
  -h, --help            show this help message and exit
  -s SPACES, --spaces SPACES
                        Spaces between colums
  -i IGNORE_DEVS, --ignore IGNORE_DEVS
                        Devices to ignore, comma separated; default=loop,ram
  -o ONLY_DEVS, --only ONLY_DEVS
                        Only show the specified devices, comma separated
  -l, --legend          Show columns legend
  -r, --realtime        Realtime Monitoring
  -c CICLES, --cicles CICLES
                        Realtime Cicles, -1 mean infinite
  -w WAIT, --wait WAIT  Realtime Cicles Wait in seconds

```

diskstats.py
```
    Device   n_ma   n_mi   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
   mmcblk0    179      0    2605     6110       100874         7580   247117   262149      4372920     16708780         0       6374040      16714450
 mmcblk0p1    179      1       0        0            0            0        0        0            0            0         0             0             0
 mmcblk0p2    179      2    2429     5365        91940         6920       76       88         1312        21670         0         11400         28560
 mmcblk0p3    179      3     175      745         8926          660   247041   262061      4371608     16687110         0       6363350      16685890
 mmcblk0p4    179      4       0        0            0            0        0        0            0            0         0             0             0
```

diskstats.py -l
```
LEGEND :
n_ma         -> Node Major
n_mi         -> Node Minor
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

    Device   n_ma   n_mi   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
   mmcblk0    179      0    2605     6110       100874         7580   247117   262149      4372920     16708780         0       6374040      16714450
 mmcblk0p1    179      1       0        0            0            0        0        0            0            0         0             0             0
 mmcblk0p2    179      2    2429     5365        91940         6920       76       88         1312        21670         0         11400         28560
 mmcblk0p3    179      3     175      745         8926          660   247041   262061      4371608     16687110         0       6363350      16685890
 mmcblk0p4    179      4       0        0            0            0        0        0            0            0         0             0             0
```

diskstats.py -r
```
First reading: 2013-07-08 17:45:32.746584
Current reading: 2013-07-08 17:45:54.096858

Disk: mmcblk0
       n_ma   n_mi   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
FIRST   179      0    2605     6110       100874         7580   247117   262149      4372920     16708780         0       6374040      16714450
CURR    179      0    2605     6110       100874         7580   247117   262149      4372920     16708780         0       6374040      16714450
DIFF      0      0       0        0            0            0        0        0            0            0         0             0             0

Disk: mmcblk0p1
       n_ma   n_mi   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
FIRST   179      1       0        0            0            0        0        0            0            0         0             0             0
CURR    179      1       0        0            0            0        0        0            0            0         0             0             0
DIFF      0      0       0        0            0            0        0        0            0            0         0             0             0

Disk: mmcblk0p2
       n_ma   n_mi   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
FIRST   179      2    2429     5365        91940         6920       76       88         1312        21670         0         11400         28560
CURR    179      2    2429     5365        91940         6920       76       88         1312        21670         0         11400         28560
DIFF      0      0       0        0            0            0        0        0            0            0         0             0             0

Disk: mmcblk0p3
       n_ma   n_mi   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
FIRST   179      3     175      745         8926          660   247041   262061      4371608     16687110         0       6363350      16685890
CURR    179      3     175      745         8926          660   247041   262061      4371608     16687110         0       6363350      16685890
DIFF      0      0       0        0            0            0        0        0            0            0         0             0             0

Disk: mmcblk0p4
       n_ma   n_mi   reads   rd_mrg   rd_sectors   ms_reading   writes   wr_mrg   wr_sectors   ms_writing   cur_ios   ms_doing_io   ms_weighted
FIRST   179      4       0        0            0            0        0        0            0            0         0             0             0
CURR    179      4       0        0            0            0        0        0            0            0         0             0             0
DIFF      0      0       0        0            0            0        0        0            0            0         0             0             0
```
