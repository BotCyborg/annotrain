import shutil
import datetime
import os

class Annotation:
    def __init__(self,ID=None,name=None,address=None,dataset_ID = None,tag=None,desc=None,comment=None,created_at=None,numfile=None):
        self.ID = ID  #unique id
        self.name = name #usergiven Name
        self.address = address #address to the folder containing the annotations
        self.dataset_ID =dataset_ID #the related dataset ID
        self.tag = tag #user assigned
        self.desc = desc #descriptoin autogenerated by the system
        self.comment  = comment #user provided comment
        self.created_at = created_at #timestamp
        self.numfile = numfile
    
    def get_json_dict(self):
        #annotation_id_list = [x.ID for x in self.annotation_object_list]
        td = {
            "ID":self.ID,
            "name":self.name,
            "address":self.address,
            "dataset_ID": self.dataset_ID,
            "tag":self.tag,
            "description": self.desc,
            "comment":self.comment,
            "created_at":str(self.created_at),
            "numfile":self.numfile
        }
        return td

    def populate(self,src):
        if self.address:
            if os.path.exists(self.address) :
                print ("error! annotation exists")
                return False
            if os.path.exists(src):
                self.created_at = datetime.datetime.now()
                shutil.copytree( src,self.address)
                return True
            else:
                print("error! invalid source folder")
            return False
        return True
    
    
    # [TODO] check size and other compatibility

    def add_dataset_ID (self,dID):
        self.dataset_ID = dID
