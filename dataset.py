class Dataset:
    def __init__(self):
        self.ID = None #unique ID
        self.name = None #usergiven name
        self.address = None #address to the folder
        self.annotation_list = [] #list of annotation objects available for this dataset
        self.tag = None #user provided tag
        self.description = None #auto generated description
        self.comment  = None #users comment
        self.created_at  =None #timestamp


