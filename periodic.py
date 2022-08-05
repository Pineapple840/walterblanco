import csv
import os

class Info():
    def __init__(self, atom, name, mass, symbol, classification):
        self.atom = atom
        self.name = name
        self.mass = mass
        self.symbol = symbol
        self.classification = classification

        if atom == 1:
            sussex = 'st'
        elif atom == 2:
            sussex = 'nd'
        elif atom == 3:
            sussex = 'rd'
        else:
            sussex = 'th'

        if int(atom) <= 2:
            inshell = 0
            period = 1
        elif atom <= 10:
            inshell = 2
            period = 2
        elif atom <= 18:
            inshell = 8
            period = 3


        

        print(f'''\nThe {atom}{sussex} in the periodic table is {name}.

#Symbol

It can also be written as *{symbol}*

#Mass

{name} is made of {atom} protons and {mass - atom} neutrons adding up to a relative atomic mass of {mass}.
  
#Electrons
 
{name} has {atom} electrons and {atom - inshell} of those are on its outer shell.

#Position
 
{name} is on row {period} and is classed as a {classification}\n''')

Kill = False



with open('elements.csv',newline = '') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)

while Kill == False:
    try:
        num = int(input('What element would you like to learn about (type a number learn about the element. type "0" to exit)\n'))
    except ValueError:
        print('Type a number dumbass')
        num = -1
    if num == 0:
        Kill = True
    elif num == -1:
        pass
    else:
        element = Info(int(list_of_csv[num][0]),list_of_csv[num][1],int(list_of_csv[num][2]),list_of_csv[num][3],list_of_csv[num][4])