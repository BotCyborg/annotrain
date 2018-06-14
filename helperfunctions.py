import uuid

#id_counter = 0

def gen_ID(pre="",post=""):
    return pre+str(uuid.uuid4())+post
    #id_counter +=1
    #return pre+str(id_counter)+post