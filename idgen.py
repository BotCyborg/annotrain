"""
A very simple unique ID generator
"""
class IDGenerator:
    def __init__(self,val):
        self.id_counter = val
        
    def int_val(self):
        return self.id_counter

    def get(self,prefix="",postfix=""):
        idstr = prefix+"{}".format(self.id_counter)+postfix
        self.id_counter +=1
        return idstr