import os
#from cmd2 import Cmd 
import cmd2 
import argparse

from annotrain import AnnoTrain



class AnnoTrainShell(cmd2.Cmd):
    """The annotrain shell"""

    prompt = 'ats>: '
    intro = "Welcome to the AnnoTrain shell!"

    ws = None

    init_parser = argparse.ArgumentParser()
    init_parser.add_argument('-p','--projectname',help="Name of the project")
    init_parser.add_argument('-d','--dataroot',help="Root directory of the project storage")

    @cmd2.with_argparser(init_parser)
    def do_init(self,args):

        self.ws = AnnoTrain(p_name=args.projectname, data_root=args.dataroot)
        print ( "projectname={0}\npath={1}".format(args.projectname,args.dataroot))
    
    def do_save(self,args):
        self.ws.save()
    
if __name__ == '__main__':
    AnnoTrainShell().cmdloop()