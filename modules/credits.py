import time
people= {'DOTTIE HOLLAND': 'CEO',
'DANIEL BOBB': 'Story Designer',
'NATHAN CONNER': 'Story Designer',
'FRANCISCO MOYA' :'Story Designer',
'JOSHUA MOYA': 'Story Designer', 
'TYLER RESURRECCION': 'Story Designer',  
'BARRY SCHIEBER': 'Story Designer', 
'DAVID SKIPP': 'Story Designer', 
'NICHOLAS TOUMA': 'Story Designer', 
'DYLAN WAGONER': 'Story Designer', 
'CARLOS CUEVAS': 'Puzzle Designer',
'CHRISTIAN HOFFA': 'Puzzle Designer',
'BENJAMIN SALINAS': 'Puzzle Designer', 
'ELIJAH STOKES': 'Puzzle Designer', 
'ZACHARY HULETT': 'Game Mechanic',
'TAKHYRA JACKSON' : 'Game Mechanic', 
'JONATHAN MORGAN' :'Game Mechanic', 
'KADE RAMER' :'Game Mechanic',
'CHRISTOPHER SIMPSON-HANSON': 'Game Mechanic', 
'REESE WITTIC': 'Game Mechanic'
'JONATHAN CURTIS': 'Programmer',
'SPENCER LIN': 'Programmer',
'ETHAN MONROE': 'Programmer', 
'ADDISON SCHEER': 'Progammer', 
        }
key= list(people.keys())
print('UNCURED credits:')
time.sleep(2)
for i in range(len(people)):
    time.sleep(2)
    print(f'{key[i]} - {people.get(key[i])}')

    
