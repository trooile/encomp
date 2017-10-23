#!/usr/bin/python

from cmd import Cmd
from subprocess import call

class TestShell(Cmd): 

    def do_ex(self, args):
        #exit program (write "ex") 
    	print("Exit program")
	raise SystemExit

    def do_ss(self, args):
        #ssh program (write "ss") 
        call(["ssh"])
   
    def do_ip(self, args):
        #ifconfig program (write "ip")
        call(["ifconfig"])
   
    def do_mais(self, args):
        #mkdir program (write "+")
        call(["mkdir"])
   
    def do_gatway(self, args):
        #route program (write "rounter")
        call(["route"])

    def do_cal(self, args):
        #calc program (write "cal")
        call(["calc"])

if __name__ == '__main__':
    prompt = TestShell()
    prompt.prompt = 'Unisal@Shell> '
    prompt.cmdloop('Starting the adventure')

