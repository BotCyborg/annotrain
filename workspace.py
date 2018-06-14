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
        self.data_root = DEFAULT_DATA_ROOT_DIR
    

    def load(self,config_file=WORKSPACE_CONFIG_FILE):
        
        #workspace json dictionary
        wjd = None
        if not os.path.isfile(config_file) :
            wjd = {}
            return


        with open(config_file) as fp:
            wjd = json.load(fp)
        
        self.data_root = wjd["DATA_ROOT_DIR"]
        self.load_data_all(wjd)
        self.load_anno_all(wjd)
        self.load_model_all(wjd)

    

    def get_annotation_by_name(self,name):
        for aID, a in self.anno_all:
            if a.name == name:
                return aID
        else:
            return None

    def get_dataset_by_name(self,name):
        for dID, d in self.data_all:
            if d.name == name:
                return dID
        else: # beautiful for-else! 
            return None

    def load_model_all(self,wjd):
        if "model_all" not in wjd: return
        for mID, mset in wjd["model_all"].items():
            m = Model(mID,name= mset['name'],address=mset['address'],tag=mset['tag'],
                desc=mset["desc"],comment=mset["comment"],
                created_at=datetime_parse(  mset["created_at"])
                )                
            self.add_model(m)


    def load_anno_all(self,wjd):
        if "anno_all" not in wjd: return
        for aID, aset in wjd["anno_all"].items():
            a = Annotation(aID,name=aset['name'],address=aset['address'],tag=aset['tag'],
                desc=aset["desc"],comment=aset["comment"],numfile=aset["numfile"],
                created_at=datetime_parse(  aset["created_at"])
                )
            a.add_dataset_ID(aset["dataset_ID"])
            self.add_annotation(a)

    def load_data_all(self, wjd):
        if "data_all" not in wjd: return
        for dID, dset in wjd["data_all"].items():
            d = Dataset(dID,name=dset['name'],address=dset['address'],tag=dset['tag'],
                desc=dset["desc"],comment=dset["comment"],numfile=dset["numfile"],
                created_at=datetime_parse(  dset["created_at"])
                )
            
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

    def all_model_as_jsondict(self):
        r = {}
        for mID, m in self.model_all.items():
            r[mID] = m.get_json_dict()
        return r

    def save(self):
        wjd = {}
        wjd["DATA_ROOT_DIR"]= self.data_root
        
        wjd["data_all"] = self.all_data_as_jsondict()
        wjd["anno_all"] = self.all_anno_as_jsondict()
        wjd["model_all"] = self.all_model_as_jsondict()
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

    def create_model(self,src,name=None):
        ID = gen_ID(pre="m")
        addr = self.data_root+"/models/"+ID
        m = Model(ID,address=addr,name=name)
        if(m.populate(src)):
            self.add_model(m)
        return ID

    def create_dataset(self,src,name=None):
        ID = gen_ID(pre="d")
        addr = self.data_root+"/datasets/"+ID
        ds = Dataset(ID,address=addr,name=name)
        if(ds.populate(src)):
            self.add_dataset(ds)
        return ID

    def create_annotation(self,src,name=None):
        ID = gen_ID(pre="a")
        addr = self.data_root+"/annosets/"+ID

        an = Annotation(ID,name=name,address=addr)

        if(an.populate(src)):
            self.add_annotation(an)
        return ID
            

