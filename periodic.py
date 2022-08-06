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
            splitshell = ''
        elif int(atom) <= 10:
            inshell = 2
            period = 2
            splitshell = '2,'
        elif int(atom) <= 18:
            inshell = 10
            period = 3
            splitshell = '2,8,'
        elif int(atom) <= 36:
            inshell = 18
            period = 4
            splitshell = '2,8,8,'

        self.period = period
        self.splitshell = splitshell
        self.inshell = inshell

        print(f'''\nThe {self.atom}{sussex} in the periodic table is {self.name}.

It can also be written as *{self.symbol}*''')


        self.furthermore()

    def furthermore(self):
        print('d')
        choice = input(f'''Input:
1 - Learn about it's structure
2 - Learn about the {self.classification}s
0 - Go back\n''')

        if choice == '0':
            pass
        elif choice == '1':
            self.info_structure()
        elif choice == '2':
            self.info_classification()
        else:
            print('I gave you a literal list of your choices you absolute set 8')
        
    def info_structure(self):

        print(f'''{self.name} is made of {self.atom} protons and a mean of {self.mass - self.atom} neutrons adding up to a relative atomic mass of {self.mass}.
 
{self.name} has {self.atom} electrons in {self.period} shells ({self.splitshell}{self.atom - self.inshell}).\n''')

    def info_classification():
        pass
    


Kill = False



with open('elements.csv',newline = '') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)

while Kill == False:
    try:
        try:
            num = int(input('What element would you like to learn about (type an integer to learn about the element. type "0" to exit)\n'))
        except IndexError:
            num = -1
            print('I have not got that far yet')
        except ValueError:
            num = -1
            print('Type an integer dumbass')
        if num == 0:
            Kill = True
        elif num == -1:
            pass
        else:
            element = Info(int(list_of_csv[num][0]),list_of_csv[num][1],int(list_of_csv[num][2]),list_of_csv[num][3],list_of_csv[num][4])
    except IndexError:
        num = -1
        print('I have not got that far yet')