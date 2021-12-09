from typing import Sized
import PySimpleGUI as sg
import os
import subprocess
import sys

class TelaFastR:
    def __init__(self):
        layout=[
            [sg.Text('1.Escolha o cenario :')],
            [sg.Radio('Budget Scenario','experimento',key='budget'),sg.Radio('Adequate Scenario','experimento',key='adequate')],

            [sg.Text('2.Escolha a cobertura :')],
            [sg.Radio('Function','coverage',key='function'),
            sg.Radio('Line','coverage',key='line'),
            sg.Radio('Branch','coverage',key='branch')],

            [sg.Text('3.Escolha o projeto e versão :')],
            [sg.Radio('Flex v3','entity',key='flex'),
            sg.Radio('Flex v3','entity',key='flex'),
            sg.Radio('Grep v3','entity',key='grep'),
            sg.Radio('Gzip v1','entity',key='gzip'),
            sg.Radio('Make v1','entity',key='make'),
            sg.Radio('Sed v6','entity',key='sed'),
            sg.Radio('Chart v0','entity',key='chart'),
            sg.Radio('Closure v0','entity',key='closure'),
            sg.Radio('Lang v0','entity',key='lang'),
            sg.Radio('Math v0','entity',key='math'),
            sg.Radio('Time v0','entity',key='time')],

            [sg.Text('4.Escolha quantidade de repetições :'), sg.Input(size=(15,0), key='repeticao')],
            
            [sg.Button('Executar teste')]
        ]
        self.janela = sg.Window("Dados Usuario").layout(layout)

    def Iniciar(self):
        while True:

            senario = ""
            cobertura = ""
            projeto = ""
            self.button, self.values = self.janela.Read()

            repeticao = self.values['repeticao']
            budget = self.values['budget']
            adequate = self.values['adequate']

            function = self.values['function']
            line = self.values['line']
            branch = self.values['branch']

            flex = self.values['flex']
            grep = self.values['grep']
            gzip = self.values['gzip']
            make = self.values['make']
            sed = self.values['sed']

            if(budget == True):
                senario = "experimentBudget.py"
            elif(adequate == True):
                senario = "experimentAdequate.py"

            if(function == True):
                cobertura = "function"
            elif(line == True):
                cobertura = "covarege"
            elif(branch == True):
                cobertura = "branch"

            if(flex == True):
                projeto = "flex v3"
            elif(grep == True):
                projeto = "grep v3"
            elif(gzip == True):
                projeto = "gzip v1"
           
            executarCmd = f'py py/{senario} {cobertura} {projeto}'
            print(executarCmd)

           # os.system('py experimentBudget.py function flex v3 10')
           # subprocess.run(['py experimentBudget.py function flex v3 10'], stderr=sys.stderr, stdout=sys.stdout)
            process = subprocess.Popen(executarCmd, stdout=subprocess.PIPE)
            output, error = process.communicate()

            if(process.returncode == 0):
                print("Done:")
            else:
                print("Failed:")

            print(output)
            print(self.values)


tela = TelaFastR()
tela.Iniciar()

