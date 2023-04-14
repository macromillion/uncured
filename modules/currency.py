# Get credits from credits.txt
def get_credits():
	with open('./data/credits.txt', 'r') as read_file:
		return read_file.readlines()[0]


def set_credits(credits: int):
	with open('./data/credits.txt', 'w') as set_file:
		set_file.write(credits)


# Call the function in the main.py
def change_credits(change: int):
	with open('./data/credits.txt', 'w') as change_file:
		change_file.write(int(change_file.readlines()[0]) + credits)
