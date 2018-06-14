import json
import os
import sys
import random
import argparse
import shutil
import uuid
import datetime

from workspace import WorkSpace





#uuid4 promises unique id for next approx(3600) years. Fingers crossed!


'''
def save_session(dd,id_generator,file_name):
        #dd["id_gen"] = id_generator.int_val()
        #parsed = json.loads(json.dumps(dd)) #for indentation
        json.dump(dd, open(file_name,"w"),indent=4, sort_keys=True)
'''


if __name__ == "__main__":
    ws = WorkSpace()

    d1 = ws.create_dataset("dummy-data-sets/data/d1","tanvir")
    
    d2 = ws.create_dataset("dummy-data-sets/data/d2","sambit")
    a1 = ws.create_annotation("dummy-data-sets/a/a1","atan1")
    
    a2 = ws.create_annotation("dummy-data-sets/a/a2","asam")
    a3 = ws.create_annotation("dummy-data-sets/a/a1","atan2")
    
    ws.link(d1,a1)
 
    ws.link(d2,a2)
    ws.link(d1,a3)
    ws.save()
   

    print("Done")