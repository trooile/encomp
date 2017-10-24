#!/usr/bin/python

from cmd import Cmd
from subprocess import call

class TestShell(Cmd):

    global domain
    domain = "unisal.br"

    def do_ex(self, args):
        #exit program (write "ex")
        '''Sair do programa'''
        print("Exit program")
        raise SystemExit

    def do_ss(self, args):
        #ssh program (write "ss")
        '''Conexão SSH está com erro'''
        call(["ssh"])
   
    def do_ip(self, args):
        #ifconfig program (write "ip")
        '''Mostra o IP da máquina'''
        call(["ifconfig"])
   
    def do_list(self, args):
        #mkdir program (write "+")
        '''Lista os arquivos'''
        call(["ls"])
   
    def do_gatway(self, args):
        #route program (write "rounter")
        '''Mostra o gateway'''
        call(["route"])

    def do_calc(self, args):
        #calc program (write "calc")
        '''Abre a calculadora'''
        call(["calc"])

    def do_cld(self, args):
        #cal program (write "cal")
        '''Abre o Calendário'''
        call(["cal"])

    def do_conexao(self, args):
        #ping program (write "ping unisal.br")
        '''Testa conexão com unisal.br'''
        call(["ping ", domain])

    def do_limpar(self, args):
        #cls program (write "cls")
        '''Limpa os comandos'''
        call(["cls"])
        
if __name__ == '__main__':
    prompt = TestShell()
    prompt.prompt = 'Unisal@Shell> '
    prompt.cmdloop('Starting the adventure')

