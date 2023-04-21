from modules import currency, data, dialogue, inventory, json, titlecode # , player
from modules.data import levels, puzzles, items, enemies

#	Args:
#	prompt (str): What is the prompt or question to ask the user
#	key_words (list_like): What words are you scanning for
#	mask (lambda): Any other condition to check for before scanning
#
#	Returns:
#	(str): The first word in the response that is in the key_words list

def Get_Action(prompt, key_words, mask=None):

	user_input = input(prompt).lower()

	if mask:
		if mask(user_input):
			return True

	for word in key_words:
		if word in user_input:
			return word

	return False


if __name__ == "__main__":

	# The title screen
	while True:
		if titlecode.show_title() == 'c':
			from modules import credits
		else:
			break
	
	# player = player.Player()
	current_level = levels[1]

	# The main game loop
	while True:

		print(current_level['name'])
		print(current_level['opening_statement'])
		for i in current_level['actions']:
			print(i)
		Get_Action('What do you do? ', current_level['actions'])