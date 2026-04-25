#!/usr/bin/env python
import sys

current_type = None
total = 0
count = 0

for line in sys.stdin:
    item_type, item_mrp = line.strip().split('\t')
    item_mrp = float(item_mrp)

    if current_type == item_type:
        total += item_mrp
        count += 1

    else:
        if current_type:
            print("%s\t%s" % (current_type, total/count))

        current_type = item_type
        total = item_mrp
        count = 1

if current_type:
    print("%s\t%s" % (current_type, total/count))
