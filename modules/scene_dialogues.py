import time
def p(dialogue, delay):
  if dialogue[-1] != '!':
    print(dialogue + '...')
  else:
    print(dialogue)
  time.sleep(delay)
  return p

p('A helicopter lands on a hospital', 2)
p('Stepping out of the helicopter is you, a government agent', 3)
p('You are tasked and debriefed to an asteroid that crashed a couple days ago to study a rapidly spreading virus', 5)
p('Your helicopter lands at the hospital helipad', 2.5)
p('You decend to the floor below but find all the roof doors locked', 3.2)
"""
Section 1 and 2
"""
p('You have now reached the crush site', 2)
p('You collect and chip away pieces of the asteroid to bring back to the base', 3.5)
p('But as you collect the samples, the asteriod begins to crack', 3)
p('You step back and watch it crumble', 2.2)
p('All of a sudden, your hazard suit warns you a spike of radiation', 3.3)
p('The asteroid is going to explode',2.5)
p('You call for extraction and are told to fend off the now alerted uncured until they can resue you.', 5)

"""
Fight off the uncured zombies
"""

p('You successfully fend off the uncured horde', 2.5)
p('A helicopter flies above you and sends down a rope for you to climb', 3.5)
p('As you fly back to your base, the asteroid explodes', 2.7)
"""
more descriptions
"""
p('It sends out a shockwave across the world', 2.5)
p('You arrive at the base', 2)
p('General: '+ playername +', our scientists are unable to find a cure for this new virus', 4.5)
p("General: It's beyond our technology", 2)
p('General: However, over at our Mars base, we have the equipment to help find a cure', 4.5)
p('General: We have received word an asteroid from the same field the one we got struck-',4)
p('Boom!', 4)
p('An explosion shakes the base', 3)
p('The ground crumbles and a sinkhole appears', 4)
