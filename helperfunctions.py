import uuid
from dateutil.parser import parse# as datetime_parse

def datetime_parse(ds):
    if ds:
        return parse(ds)
    else:
        return None
        
#id_counter = 0

def gen_ID(pre="",post=""):
    return pre+str(uuid.uuid4())+post
    #id_counter +=1
    #return pre+str(id_counter)+post

#check if b is None. if not return b else return a
def AC(a,b):
    return a if b is None else b
    