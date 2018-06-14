"""
A very simple unique ID generator
"""
import uuid

class IDGenerator:
    def __init__(self,val):
        self.id_counter = val

    def int_val(self):
        return self.id_counter

    def get(self,pre="",post=""):
        return pre+fixstr(uuid.uuid4() )+post 
        