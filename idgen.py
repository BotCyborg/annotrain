"""
A very simple unique ID generator
"""
class IDGenerator:
    def __init__(self,val):
        self.id_gen = val
    
    def get(self,prefix="",postfix=""):
        idstr = prefix+"{}".format(self.id_gen)+postfix
        self.id_gen +=1
        return idstr