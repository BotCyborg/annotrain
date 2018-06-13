import json
import os
import sys
import random
import argparse

from idgen import IDGenerator
data_root = "alldata"

dd = {} #the data dictionary





if __name__ == "__main__":
    id_generator  = None
    if not os.path.exists(data_root):
        os.makedirs(data_root)
    file_name = "metadata.json"
    if os.path.isfile(data_root+"/"+"metadata.json") :
        dd = json.load(open(file_name))
        ld_idgen = int(dd["id_gen"])
        #print (id_gen+3)
        id_generator = IDGenerator(ld_idgen)

    else:
        id_generator = IDGenerator(0)
    
    print (id_generator.get("shuru","shesh"))