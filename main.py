#!-*- coding: utf8 -*-
import os, sys

print ("Este programa tem a tarefa de juntar arquivos .mol em uma base .sdf.\n")

#base = raw_input('Qual o nome da base? \n') \\ Python 2
#user = raw_input('Qual o nome do usuário? \n')	\\ Python 2

base = input('Qual o nome da base? \n') 	#Python 3
user = input('Qual o nome do usuário? \n')	#Python 3

path = os.path.abspath("")
files = [f for f in os.listdir(path) if f.endswith('.mol')]
file = open( base + '.sdf', 'a')

for nameSubstance in files:
	fileAux = open( nameSubstance , 'r')	
	nameSubstance = nameSubstance.replace(".mol","") 
	file.write(nameSubstance)
	
	contentArq = fileAux.read()
	contentArq = contentArq.replace("\n\n\n  ","\n\n\n ")
	contentArq = contentArq.replace("\n$$$$","")
	file.write(contentArq)

	fileAux.close()

	file.write("> <molfile>\n" + nameSubstance + "\n\n")
	file.write("> <user>\n" + user + "\n\n")
	file.write("$$$$\n")

file.close()  
print ("Base criada com sucesso!")
