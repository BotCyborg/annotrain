import cmd2

import os
from workspace import WorkSpace



class AnnoTrain(cmd.Cmd):
    """The annotrain shell"""

    prompt = 'ats>: '
    intro = "Welcome to the AnnoTrain shell!"

    ws = None
    def do_load(self,line):
        if os.path.isfile(line):
            ws = WorkSpace()
            ws.load(line)
            print("{} :loaded".format(line))
        else:
            print("Not found")
    
    def do_save(self,line):
        if ws is None:
            print ("workspace not loaded")
        else:
            ws.save()
    
    
    def do_exit(self,line):
        return True

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    AnnoTrain().cmdloop()