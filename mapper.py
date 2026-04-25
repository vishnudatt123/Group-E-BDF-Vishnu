#!/usr/bin/env python
import sys

for line in sys.stdin:
    if "Item_Identifier" in line:
        continue

    data = line.strip().split(',')

    item_type = data[4]
    item_mrp = float(data[5])

    print("%s\t%s" % (item_type, item_mrp))
