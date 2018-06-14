import os
import datetime
import shutil

from helperfunctions import *


class Model:

    def __init__(self,ID=None,name=None,address=None,desc=None,comment=None, tag=None,
                created_at=None,mtype=None,parent_model=None,trained_on_dataset_ID = None,
                trained_on_annotation_ID=None):

        self.ID = ID #unique ID
        self.name = name #usergiven name
        self.address = address
        self.tag = tag
        self.mtype = mtype #type of the training model
        self.parent_model_ID = None #the initial model object
        self.desc = desc #auto generated description
        self.comment = comment
        self.created_at = created_at #timestamp
        self.trained_on_dataset_ID = trained_on_dataset_ID
        self.trained_on_annotation_ID = trained_on_annotation_ID
        
    def add_property(self,name=None,tag=None,desc=None,comment=None,parent_model_ID=None,
                    trained_on_dataset_ID=None,trained_on_annotation_ID=None):
        self.name = AC(self.name,name) #usergiven name
        self.tag = AC(self.tag,tag) #user provided tag
        self.desc = AC(self.desc,desc) #auto generated description
        self.parent_model_ID = AC(self.parent_model_ID, parent_model_ID)
        self.comment  = AC(self.comment, comment) #users comment
        self.trained_on_dataset_ID = AC(self.trained_on_dataset_ID,trained_on_dataset_ID)
        self.trained_on_annotation_ID = AC(self.trained_on_annotation_ID,trained_on_annotation_ID)

    def assign_parent_model(self,parent_model_ID):
        self.add_property(parent_model_ID=parent_model_ID)

    def populate(self,src):
        if self.address:
            if os.path.exists(self.address) :
                print ("error! model exists")
                return False
            if os.path.exists(src):
                self.created_at = datetime.datetime.now()
                shutil.copytree( src,self.address)
                return True
            else:
                print("error! invalid source folder")
            return False
        return True

    def get_json_dict(self):
        
        td = {
            "ID":self.ID,
            "name":self.name,
            "address":self.address,
            "mtype":self.mtype,
            "parent_model":self.parent_model_ID,
            "tag":self.tag,
            "desc": self.desc,
            "comment":self.comment,
            "created_at":str(self.created_at),
            "trained_on_dataset_ID":self.trained_on_dataset_ID,
            "trained_on_annotation_ID":self.trained_on_annotation_ID
            
        }
        return td