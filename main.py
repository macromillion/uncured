from modules import currency, credits, data, scene_dialogues.py, inventory, json, titlecode


print(currency.get_credits())
currency.set_credits(150)
print(currency.get_credits())

# Args:
# prompt (str): What is the prompt or question to ask the user
# key_words (list_like): What words are you scanning for
# mask (lambda): Any other condition to check for before scanning


# Returns:
# (str): The first word in the response that is in the key_words list
def Get_Action(prompt, key_words, mask=None):

	user_input = input(prompt).lower()

	if mask:
		if mask(user_input):
			return True

	for word in key_words:
		if word in user_input:
			return word

	return False


#print(currency.get())

print(Get_Action("Where do you want to go?\n", ['mars']))
