levels = {
 1: {
  'items': [1],  # 0-3 e.g.: [52, 82, 73]
  'difficulty': 2,  # range 1-3
  'enemies': 1,  # 0-3, dont make every room have a monster
  'opening_statement': [],
  'options': [],  # these will be level numbers e.g.: [1, 5, 6]
  'name': 'Entrance',  # Just a name of the room starting with a capital letter
  'puzzles': [],  # keep this empty for now
  'actions': []
 },

 2: {
  'items': [],
  'difficulty': 1,
  'enemies': 1,
  'options': [],
  'name': 'Entrance',
  'puzzles': [],
  'actions': []
 }
}

# the puzzles and their solutions
puzzles = {
 1: {
  'name':
  'Green Door',  # The name of the puzzle
  'solution_items': [
   1
  ],  # This is made a list only for scalability, it is advised to only use one solution item
  'opening_statement':
  'You see a door with a deep green coat of paint, now peeling from age.',  # This statement will be returned when the player enters the room
  'no_item_errors': [
   'The door is locked, there is a green keycard reader nearby.',
   'I don\'t think that worked.', 'It wont budge.'
  ],  # This error will return when the user gets the wrong solution, this will be random 
    'actions': []
 },
 2: {
  'name': ''
  'actions': []
 }
}

# the items and their ids for the game
"""
Name - A short descriptive name of the item, preferred 2 words.
Durability - This is the number of SUCCESSFUL uses before it breaks, check if the durability if 1 before using then use the item then print that the item broke.
"""
items = {
 1: {
  'name':
  'Green Keycard',
  'durability':
  1,
  'description':
  'This keycard is worn and battered, I would be suprised if it works.'
 },
	2: {
  'name':
  'Cure',
  'durability':
  1,
  'description':
  'Cures humanity from the virus.'
 },
	3: {
  'name':
  'Martian Key',
  'durability':
  1,
  'description':
  'This key gives access to Mars.'
 },
  4: {
  'name':
  'Asteroid Piece',
  'durability':
  1,
  'description':
  'From the big asteroid, this piece of rock helps with crafting the cure to the virus.'
 },
  5: {
  'name':
  'Butts pie', 
  'durability':
  1,
  'description':
  'This rare item will heal your entire hp.'
 },
  6: {
  'name':
  'Stem Pack I', #heals 20 appearance should look more advance the higher the level
  'durability':
  1,
  'description':
  'A strange looking syringe that heals part of your health bar.'
 },
  7: {
  'name':
  'Stem Pack II', #heals 40
  'durability':
  1,
  'description':
  'A strange looking syringe that heals part of your health bar.'
  },
  8: {
  'name':
  'Stem Pack III', #heals 60
  'durability':
  1,
  'description':
  'A strange looking syringe that heals part of your health bar.'
 },
   9: {
  'name':
  'Backpack I', 
  'durability': #infinite durability
  0,
  'description':
  'A backpack that stores your items what do you expect.  '
 },
   10: {
  'name':
  'Backpack II', 
  'durability':
  0,
  'description':
  'A slighty bigger backpack that stores your items what do you expect.  '
 },
   11: {
  'name':
  'Backpack III', 
  'durability':
  0,
  'description':
  'A bigger backpack that stores your items what do you expect.  '
 }
 }
""
Enemy stats
"""
enemies= {
1:{
  'name': 
  '',
  'health':
  0, 
  'speed':
  0,
  'items equipped':
  [],
  'armor':
  0,
  'drop_item_when_killed':
  []
  },

}
}
