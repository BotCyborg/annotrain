import shutil
import datetime
import os

class Dataset:
    def __init__(self, ID=None,name=None,address=None,tag=None,desc = None,comment=None,created_at=None,numfile=None):
        self.ID = ID #unique ID
        self.name = name #usergiven name
        self.address = address #address to the folder
        self.annotation_list = [] #list of annotation available for this dataset
        self.tag = tag #user provided tag
        self.desc = desc #auto generated description
        self.comment  = comment #users comment
        self.created_at  = created_at #timestamp
        self.numfile = numfile #number of files contained in this dataset
    
    def add_property(self,name=None,tag=None,desc=None,comment=None):
        self.name = AC(self.name,name) #usergiven name
        self.tag = AC(self.tag,tag) #user provided tag
        self.desc = AC(self.desc,desc) #auto generated description
        #self.parent_model = AC(self.parent_model, parent_model)
        self.comment  = AC(self.comment, comment) #users comment
        #self.trained_on_dataset_ID = AC(self.trained_on_dataset_ID,trained_on_dataset_ID)
        #self.trained_on_annotation_ID = AC(self.trained_on_annotation_ID,trained_on_annotation_ID)

    
        
        

    def get_json_dict(self):
        #annotation_id_list = [x.ID for x in self.annotation_object_list]
        td = {
            "ID":self.ID,
            "name":self.name,
            "address":self.address,
            "annotation_list": self.annotation_list,
            "tag":self.tag,
            "desc": self.desc,
            "comment":self.comment,
            "created_at":str(self.created_at),
            "numfile":self.numfile
        }
        return td
        
    def populate(self,src):
        if self.address:
            if os.path.exists(self.address) :
                print ("error! data exists")
                return False
            if os.path.exists(src):
                self.created_at = datetime.datetime.now()
                shutil.copytree( src,self.address)
                return True
            else:
                print("error! invalid source folder")
            return False
        return True
    
    def add_annotation_ID(self,anID):
        if anID not in self.annotation_list:
            self.annotation_list.append(anID) 
            
#def populate(ID,name,address,annotation_list,tag,)

