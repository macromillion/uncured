#make sure inventory.txt is empty before you start doing stuff
def get_inv():
  inventory = []
  with open('../data/inventory.txt', 'r') as items:
    for line in items:  #for every item, add it to a list
      inventory.append(line.replace('\n', ''))  #adds all the items to a list
  return inventory  #returns that list


def add_inv(item):
  with open('../data/inventory.txt', 'a') as items:
    items.write(item + '\n')  #adds an item to the inventory txt file
  return


def del_item(itemindex): #delete an item from the inventory
  with open('../data/inventory.txt','r') as items:
    lines=items.readlines()
  with open('../data/inventory.txt','w') as items: #rewrites the list minus the ones we want to delete
    for number,line in enumerate(lines):
      if number not in [itemindex]: #index of the item we want to delete, according to the list from get_inv()
        items.write(line)
  return


def clear_inv():
  open('../data/inventory.txt','w').close()
  return
