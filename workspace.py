import shutil
import json
import os
import datetime
from dataset import Dataset
from annotation import Annotation
from model import Model



from config import *
from helperfunctions import *


class WorkSpace:
    def __init__(self):
        self.data_all = {}
        self.anno_all = {}
        self.model_all = {}
    

    def load(self,config_file=WORKSPACE_CONFIG_FILE):
        
        #workspace json dictionary
        wjd = None
        with open(config_file) as fp:
            wjd = json.load(fp)
        
        DATA_ROOT_DIR = wjd["DATA_ROOT_DIR"]
        self.load_data_all(wjd)
        self.load_anno_all(wjd)

    
    def load_anno_all(self,wjd):
        for aID, aset in wjd["anno_all"].items():
            a = Annotation(aID,name=aset['name'],address=aset['address'],tag=aset['tag'],
                desc=aset["description"],comment=aset["comment"],numfile=aset["numfile"],
                created_at=datetime_parse(  aset["created_at"])
                )
            a.add_dataset_ID(aset["dataset_ID"])
            self.add_annotation(a)

    def load_data_all(self, wjd):
        for dID, dset in wjd["data_all"].items():
            d = Dataset(dID,name=dset['name'],address=dset['address'],tag=dset['tag'],
                desc=dset["description"],comment=dset["comment"],numfile=dset["numfile"],
                created_at=datetime_parse(  dset["created_at"])
                )
            #pl = 
            for aID in dset["annotation_list"]:
                d.add_annotation_ID(aID)
            self.add_dataset(d)

    def link(self,dID,aID):
        self.data_all[dID].add_annotation_ID(aID)
        self.anno_all[aID].add_dataset_ID(dID)
    def all_data_as_jsondict(self):
        r = {}
        for dID, d in self.data_all.items():
            r[dID] = d.get_json_dict()
        return r

    def all_anno_as_jsondict(self):
        r = {}
        for aID, a in self.anno_all.items():
            r[aID] = a.get_json_dict()
        return r


    def save(self):
        wjd = {}
        wjd["DATA_ROOT_DIR"]= DATA_ROOT_DIR
        
        wjd["data_all"] = self.all_data_as_jsondict()
        wjd["anno_all"] = self.all_anno_as_jsondict()
        with open(WORKSPACE_CONFIG_FILE,"w") as fp:
            json.dump(wjd, fp,indent=4, sort_keys=True)

        
    def add_dataset(self, ds ):
        if ds.ID in self.data_all:
            print ("error! dataset collision")
            
        else:
            self.data_all[ds.ID] = ds
            print ("ds added",ds.ID)
    
    def add_annotation(self,an):
        if an.ID in self.anno_all:
            print ("error! annotation collision")
            exit(1)
        else:
            self.anno_all[an.ID] = an

    def add_model(self,m):
        if m.ID in self.model_all:
            print("error! model collision")
            exit(1)
        else:
            self.model_all[m.ID] = m

    def create_dataset(self,src,name=None):
        ID = gen_ID(pre="d")
        addr = DATA_ROOT_DIR+"/datasets/"+ID
        ds = Dataset(ID,address=addr,name=name)
        if(ds.populate(src)):
            self.add_dataset(ds)
        return ID

    def create_annotation(self,src,name=None):
        ID = gen_ID(pre="a")
        addr = DATA_ROOT_DIR+"/annosets/"+ID

        an = Annotation(ID,name=name,address=addr)

        if(an.populate(src)):
            self.add_annotation(an)
        return ID
            

