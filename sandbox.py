#sandbox for silly test codes
import datetime
import json
from dateutil.parser import parse as datetime_parse
from helperfunctions import *
#useful cmd tutorial https://pymotw.com/2/cmd/
import cmd

import cmd
class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = 'prompt: '
    intro = "Simple command processor example."

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'
    
    ruler = '-'
    
    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
'''
class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    #the docstring becomes the help
    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print ("hi,", person)
        else:
            print ('hi')
    
    def do_EOF(self, line):
        return True
    
    def do_exit(self,line):
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()
'''
'''
class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, line):
        print ("hello")
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
'''
'''
w = {}
w["a"] = "dhaka"
w["b"] = None

json.dump(w, open("sandbox.json","w"),indent=4, sort_keys=True)

p = None
with open("sandbox.json") as fp:
    p = json.load(fp)
print (p)
'''
'''
a = "test"
b = False

a = AC(a,b)

print(a)
'''

'''
ds = "2018-06-14 12:16:56.599762"

now = datetime_parse(ds)
print(now)
'''

'''
import json
import os
path = "alldata"
if not path :

    if os.path.exists(str(path)):
        print ("yes")
    else:
        print ("no")

else:
    print("None")

'''
'''
w = {"foo": {'testA':2,'testC':6},
    "bar": "{'testB':5}"
}

#parsed = json.loads(json.dumps(w)) #for indentation
json.dump(w, open("sandbox.json","w"),indent=4, sort_keys=True)
'''
'''
w = {}
a = {"kotha":[2,3]}
b = {"bolo":[4,5],
    "kotha": [10,20]
    }
w ["data1"] =  a 
w ["data2"] = b

def dataadder(d):
    r = d.get("kotha")
    print("now", r)
    r.append(7)

print(w)
dataadder(w.get("data1"))
print(w)
dataadder(w.get("data2"))
print(w)
'''
'''
    id_generator  = None
    if not os.path.exists(data_root):
        os.makedirs(data_root)
    #file_name = workspace_config_file
    if os.path.isfile(workspace_config_file) :
        with open(workspace_config_file) as fp:
            wd = json.load(fp)
            ld_idgen = int(wd["id_gen"])
            #print (id_gen+3)
            id_generator = IDGenerator(ld_idgen)

    else:
        id_generator = IDGenerator(0)

    if os.path.exists("dummy-data-sets/data/d1"):
        dst = data_root+"/"+id_generator.get(prefix="dd",postfix="")
        shutil.copytree( "dummy-data-sets/data/d1",dst)
'''
'''
    with open(file_name) as fp:
            md = json.load(fp)
            md["data_root"] = "alldata"
            parsed = json.loads(json.dumps(md)) #for indentation
            json.dump(parsed, open(file_name,"w"),indent=4, sort_keys=True)
'''
'''
    save_session(wd,id_generator,file_name)
    #print (id_generator.get("shuru","shesh"))
    
    print(uuid.uuid4())
    print(uuid.uuid4())
'''