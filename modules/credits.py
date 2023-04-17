import time
people= {'Dottie Holland': 'Leader',
'DANIEL BOBB': 'Story Designer',
'NATHAN CONNER': 'Story Designer',
'CARLOS CUEVAS': 'Puzzle Designer',
'JONATHAN CURTIS': 'Programmer',
'CHRISTIAN HOFFA': 'Puzzle Designer', 
'ZACHARY HULETT': 'Game Mechanic',
'TAKHYRA JACKSON' : 'Game Mechanic', 
'Spencer Lin': 'Programmer',
'ETHAN MONROE': 'Programmer', 
'JONATHAN MORGAN' :'Game Mechanic', 
'FRANCISCO MOYA' :'Story Designer',
'JOSHUA MOYA': 'Story Designer', 
'KADE RAMER' :'Game Mechanic',
'TYLER RESURRECCION': 'Story Designer', 
'BENJAMIN SALINAS': 'Puzzle Designer', 
'ADDISON SCHEER': 'Progammer', 
'BARRY SCHIEBER': 'Story Designer', 
'CHRISTOPHER SIMPSON-HANSON': 'Game Mechanic', 
'DAVID SKIPP': 'Story Designer', 
'ELIJAH STOKES': 'Puzzle Designer', 
'NICHOLAS TOUMA': 'Story Designer', 
'DYLAN WAGONER': 'Story Designer', 
'REESE WITTIC': 'Game Mechanic'}
key= list(people.keys())
print('UNCURED credits:')
time.sleep(2)
for i in range(len(people)):
    time.sleep()
    print(f'{key[i]} - {people.get(key[i])}')

    
