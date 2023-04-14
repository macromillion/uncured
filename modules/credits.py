import time
people= {'Dottie Holland': 'Owner',
'DANIEL BOBB': '',
'NATHAN CONNER': '',
'CARLOS CUEVAS': '',
'JONATHAN CURTIS': 'Programmer',
'CHRISTIAN HOFFA': '', 
'ZACHARY HULETT': 'Game Mechanic',
'TAKHYRA JACKSON' : 'Game Mechanic', 
'Spencer Lin': 'Programmer',
'ETHAN MONROE': 'Programmer', 
'JONATHAN MORGAN' :'', 
'FRANCISCO MOYA' :'',
'JOSHUA MOYA': '', 
'KADEN RAMER' :'',
'TYLER RESURRECCION': '', 
'BENJAMIN SALINAS': '', 
'ADDISON SCHEER': 'Progammer', 
'BARRY SCHIEBER': '', 
'CHRISTOPHER SIMPSON-HANSON': 'Game Mechanic', 
'DAVID SKIPP': '', 
'ELIJAH STOKES': '', 
'NICHOLAS TOUMA': '', 
'DYLAN WAGONER': '', 
'ANTHONY WITTIC': ''}
key= list(people.keys())
print('UNCURED credits:')
time.sleep(2)
for i in range(len(people)):
    time.sleep()
    print(f'{key[i]} - {people.get(key[i])}')

    