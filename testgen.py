import json
import os
import sys
import random
import argparse

idgen = 0
froot = "dummy-data-sets"

if not os.path.exists(froot):
    os.makedirs(froot)

num_dset = 10

random.seed()

for i in range(10):
    #dset_name = "d{}".format(i)
    dset_name = "c{}".format(i)
    dset_addr = froot + "/"+dset_name

    if not os.path.exists(dset_addr):
        os.makedirs(dset_addr)
    for j in range(10+i):
        fname = "{}image.txt".format(j)
        content = "{} {}\n".format( random.randint(0, 50), random.randint(0,19))
        with open(dset_addr+"/"+fname,"w") as fp:
            fp.write(content)


