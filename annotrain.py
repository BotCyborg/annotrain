import json
import os
import sys
import random
import argparse
import shutil

from idgen import IDGenerator
data_root = "alldata"

md = {} #the meta_data dictionary loaded from medatada.json



def save_session(dd,id_generator,file_name):
        dd["id_gen"] = id_generator.int_val()
        parsed = json.loads(json.dumps(dd)) #for indentation
        json.dump(parsed, open(file_name,"w"),indent=4, sort_keys=True)

if __name__ == "__main__":
    id_generator  = None
    if not os.path.exists(data_root):
        os.makedirs(data_root)
    file_name = "metadata.json"
    if os.path.isfile("metadata.json") :
        with open(file_name) as fp:
            md = json.load(fp)
            ld_idgen = int(md["id_gen"])
            #print (id_gen+3)
            id_generator = IDGenerator(ld_idgen)

    else:
        id_generator = IDGenerator(0)

    if os.path.exists("dummy-data-sets/data/d1"):
        dst = data_root+"/"+id_generator.get(prefix="dd",postfix="")
        shutil.copytree( "dummy-data-sets/data/d1",dst)
    '''
    with open(file_name) as fp:
            md = json.load(fp)
            md["data_root"] = "alldata"
            parsed = json.loads(json.dumps(md)) #for indentation
            json.dump(parsed, open(file_name,"w"),indent=4, sort_keys=True)
    '''
    save_session(md,id_generator,file_name)
    #print (id_generator.get("shuru","shesh"))