"""
this file contains all the display related stuff
"""
import test_rpg_config as con
import test_rpg_battle_stats_and_vars as var
import test_rpg_battle_other_functions as func
import test_rpg_battle_skill_list as lst
import random

#this displays the cost to run for sp and pwr
def run_cost_message():
    sp = 0
    pwr = 0
    if (var.pLStats.health_type == 1 or var.pLStats.health_type == 3) and var.pLStats.exists >= 1:
        sp += 1
    elif (var.p1Stats.health_type == 1 or var.p1Stats.health_type == 3) and var.p1Stats.exists >= 1:
        sp += 1
    elif (var.p2Stats.health_type == 1 or var.p2Stats.health_type == 3) and var.p2Stats.exists >= 1:
        sp += 1
    elif (var.p3Stats.health_type == 1 or var.p3Stats.health_type == 3) and var.p3Stats.exists >= 1:
        sp += 1
        
    if var.pLStats.health_type == 4 and var.pLStats.exists >= 1:
        pwr += 1
    elif var.p1Stats.health_type == 4 and var.p1Stats.exists >= 1:
        pwr += 1
    elif var.p2Stats.health_type == 4 and var.p2Stats.exists >= 1:
        pwr += 1
    elif var.p3Stats.health_type == 4 and var.p3Stats.exists >= 1:
        pwr += 1
    
    if sp >= 1 and pwr >= 1:
        return f'- (cost:{lst.run_battle_cost}sp/{lst.run_battle_cost*lst.pwr_exchange_rate}pwr)'
    elif sp >= 1:
        return f'- (cost:{lst.run_battle_cost}sp)'
    elif pwr >= 1:
        return f'- (cost:{lst.run_battle_cost*lst.pwr_exchange_rate}pwr)'
    else:
        return f''

#general party actions
def party_actions(stats, side_text):
    print(f' What will {stats.name} do? {side_text}')
    print(f'({con.option_1})|Fight    ')
    print(command_or_skill_check(stats))
    print(f'({con.option_3})|Defend   ')
    print(back_or_run_check(stats))

#displays Command or Skill options depending on char
def command_or_skill_check(stats):
    if stats.id == 1:
        return f'({con.option_2})|Command  '
    else:
        return f'({con.option_2})|Skill    '

#check to show the run option
def back_or_run_check(stats):
    if stats.party_slot > 1:
        return f'({con.option_back})|Back     '
    else:
        return f'({con.option_4})|Run  {run_cost_message()}'

#list of enemy targets
def targets():
    global enemy1_exists
    global enemy2_exists
    global enemy3_exists
    
    if var.e1Stats.exists == 1:
        print(f'({con.option_1}){display_single_hp_sp(var.e1Stats)}')
    if var.e2Stats.exists == 1:
        print(f'({con.option_2}){display_single_hp_sp(var.e2Stats)}')
    if var.e3Stats.exists == 1:
        print(f'({con.option_3}){display_single_hp_sp(var.e3Stats)}')
    if var.e4Stats.exists == 1:
        print(f'({con.option_4}){display_single_hp_sp(var.e4Stats)}')
    print(f'({con.option_back})|back')
    
#list of party targets
def targets_allies():
    global pL_exists
    global p1_exists
    global p2_exists
    global p3_exists
    
    if var.pLStats.exists == 1:
        print(f'({con.option_1}){display_single_hp_sp(var.pLStats)}')
    if var.p1Stats.exists == 1:
        print(f'({con.option_2}){display_single_hp_sp(var.p1Stats)}')
    if var.p2Stats.exists == 1:
        print(f'({con.option_3}){display_single_hp_sp(var.p2Stats)}')
    if var.p3Stats.exists == 1:
        print(f'({con.option_4}){display_single_hp_sp(var.p3Stats)}')
    print(f'({con.option_back})|back')
    
#clears the screen with 30 print statments
def clear_screen():
    for i in range(30):
        print()

#this is for the battle message thing.
def battle_message_display():
    #nobody
    if con.enemy1 == 0 and con.enemy2 == 0 and con.enemy3 == 0 and con.enemy4 == 0:
        return f'* But nobody came.'
    #fred only
    elif con.enemy1 == var.FredStats.id and con.enemy2 == 0 and con.enemy3 == 0 and con.enemy4 == 0:
        if var.turn_number_message >= 5:
            var.turn_number_message = 2
        if var.turn_number_message == 1:
            return f'* You engage Fred.'
        elif var.turn_number_message == 2:
            return f'* Fred.'
        elif var.turn_number_message == 3:
            return f'* Smells of Mushrooms fill the air.'
        elif var.turn_number_message == 4:
            return f'* You feel the spores going down your back.'
    #1 testman only
    elif con.enemy1 == var.TestmanStats.id and con.enemy2 == 0 and con.enemy3 == 0 and con.enemy4 == 0:
        if var.turn_number_message >= 5:
            var.turn_number_message = 2
        if var.turn_number_message == 1:
            return f'* Testman Approaches!'
        elif var.turn_number_message == 2:
            return f'* Testman stands by.'
        elif var.turn_number_message == 3:
            return f'* Testman offers you some tea.'
        elif var.turn_number_message == 4:
            return f"* Smells like Testman."
    #3 moldsmals
    elif con.enemy1 == var.MoldsmalStats.id and con.enemy2 == var.MoldsmalStats.id and con.enemy3 == var.MoldsmalStats.id and con.enemy4 == 0:
        if var.turn_number_message >= 6:
            var.turn_number_message = 2
        if var.turn_number_message == 1:
            return f'* You tripped into a line of Moldsmals.'
        elif var.turn_number_message == 2:
            return f'* Moldsmal waits pensively.'
        elif var.turn_number_message == 3:
            return f'* Moldsmal burbles quietly.'
        elif var.turn_number_message == 4:
            return f"* Moldsmal is ruminating."
        elif var.turn_number_message == 5:
            return f"* The aroma of lime gelatin wafts through."
    #fred + hamy + creation + willow 
    elif con.enemy1 == var.FredStats.id and con.enemy2 == var.HamyStats.id and con.enemy3 == var.CreationStats.id and con.enemy4 == var.WillowStats.id:
        while 0==0:
            if var.turn_number_message >= 6:
                var.turn_number_message = 2
            if var.turn_number_message == 1:
                return f'* Here comes the B-Team!'
            elif var.turn_number_message == 2 and var.e2Stats.exists == 1:
                return f'* Hamy fidgets with {pronouns(var.HamyStats, 3)} HAM-PAC(tm).'
            elif var.turn_number_message == 3 and var.e3Stats.exists == 1:
                if var.e2Stats.exists == 1:
                    return f'* Creation looms over you.'
                else:
                    return f'* Creation stares at you'
            elif var.turn_number_message == 4 and var.e4Stats.exists == 1:
                return f"* Willow flaps {pronouns(var.WillowStats, 3)} wings impatiently."
            elif var.turn_number_message == 5 and var.e1Stats.exists == 1:
                return f"* Fred."
            else:
                if var.turn_number_message == 2:
                    return f'* You feel science judging your very soul.'
                elif var.turn_number_message == 3:
                    return f'* Sparks fly through the air.'
                elif var.turn_number_message == 4:
                    return f"* Smells of various food items and robots."
                elif var.turn_number_message == 5:
                    return f"* Mitochondria is the powerhouse of the cell."
    else:
        if var.turn_number_message >= 5:
            var.turn_number_message = 2
        if var.turn_number_message == 1:
            return f'* The enemy(s) approach!'
        elif var.turn_number_message == 2:
            return f'* The enemy(s) are doing something.'
        elif var.turn_number_message == 3:
            return f'* Smells like you.'
        elif var.turn_number_message == 4:
            return f"* what."
        
#basic info showing
def display_hp_and_sp():
    print(f'Cycle: {var.battle_cycle}' if var.battle_cycle > 0 else '')
    print(battle_message_display())
    func.shovel_rng()
    print(f'--ENEMY-----------------------------------------')
    display_enemy_hp_sp()
    print(f'--PARTY-----------------------------------------')
    display_party_hp_sp()
    print(f'------------------------------------------------')

#adds spaces before a word, used to keep a string the same length
def reverse_space_check(what, add_what, length):
    add_amount = length - len(what)
    if len(what) < length:
        for add in range(add_amount):
            what = add_what + what
    return what

#adds spaces behind a word, used to keep a string the same length
def space_check(what, add_what, length):
    add_amount = length - len(what)
    if len(what) < length:
        for add in range(add_amount):
            what += add_what
    return what

#general stat display.
def display_single_hp_sp(stats):
    return f"""|{stats.display_name} |  {f"{reverse_space_check(f'{stats.cur_hp}/{stats.max_hp}hp', ' ', 9)}{reverse_space_check(f'{stats.cur_sp}/{stats.max_sp}sp', ' ', 10)}" if stats.health_type == 1 else ""}{f"{reverse_space_check(f'{stats.cur_hp}/{stats.max_hp}hp', ' ', 9)}          " if stats.health_type == 2 else ""}{f"{reverse_space_check(f'{stats.cur_sp}/{stats.max_sp}sp', ' ', 19)}" if stats.health_type == 3 else ""}{f"{reverse_space_check(f'{stats.cur_pwr}/{stats.max_pwr}pwr', ' ', 11)}        " if stats.health_type == 4 else ""}{f" {stats.charge}chrg" if stats.id == 4 else "      "}{f" (Downed)" if stats.alive == 0 else ""}{f" (Attacking)" if stats.action == 1 else ""}{f" (Defending)" if stats.action == 2 else ""}{f" (Commanding)" if stats.action >= 100 and stats.action < 200 else ""}{f" (Skilling)" if stats.action >= 200 else ""}"""

#displays party stats
def display_party_hp_sp():
    if var.pLStats.exists == 1:
        print(display_single_hp_sp(var.pLStats))
    if var.p1Stats.exists == 1:
        print(display_single_hp_sp(var.p1Stats))
    if var.p2Stats.exists == 1:
        print(display_single_hp_sp(var.p2Stats))
    if var.p3Stats.exists == 1:
        print(display_single_hp_sp(var.p3Stats))

#displays enemy stats
def display_enemy_hp_sp():
    if var.e1Stats.exists == 1:
        print(display_single_hp_sp(var.e1Stats))
    if var.e2Stats.exists == 1:
        print(display_single_hp_sp(var.e2Stats))
    if var.e3Stats.exists == 1:
        print(display_single_hp_sp(var.e3Stats))
    if var.e4Stats.exists == 1:
        print(display_single_hp_sp(var.e4Stats))

#used for messages that need they/them/their/theirs/themself in 4 different genders, uses the gender var in char stats
def pronouns(stats, typ):
    #subject = 1
    #object = 2
    #possessive adj = 3
    #possessive pron = 4
    #reflexive = 5
    if stats.gender == 2:
        if typ == 1:
            return 'she'
        elif typ == 2:
            return 'her'
        elif typ == 3:
            return 'her'
        elif typ == 4:
            return 'hers'
        elif typ == 5:
            return 'herself'
        else:
            return 'error'
    elif stats.gender == 1:
        if typ == 1:
            return 'he'
        elif typ == 2:
            return 'him'
        elif typ == 3:
            return 'his'
        elif typ == 4:
            return 'his'
        elif typ == 5:
            return 'himself'
        else:
            return 'error'
    elif stats.gender == 3:
        if typ == 1:
            return 'it'
        elif typ == 2:
            return 'it'
        elif typ == 3:
            return 'its'
        elif typ == 4:
            return 'its'
        elif typ == 5:
            return 'itself'
        else:
            return 'error'
    else:
        if typ == 1:
            return 'they'
        elif typ == 2:
            return 'them'
        elif typ == 3:
            return 'their'
        elif typ == 4:
            return 'theirs'
        elif typ == 5:
            return 'themselves'
        else:
            return 'error'

#--battle-messages-----------------------------------------------------------------------------
#shown if thing's health goes below 0 or if they had refused hit
def downed_refuse_messages(message, yr_stats, other_stats):
    #yr_stats var doesnt work lol
    
    #crit deaths
    if message == 1 and yr_stats.crit >= 1:
        rng_message = random.randint(1,10)
        if rng_message == 1:
            print(f'X {other_stats.name} was destroyed...')
        elif rng_message == 2:
            print(f'X {other_stats.name} was disseminated...')
        elif rng_message == 3:
            print(f'X {other_stats.name} was obliterated...')
        elif rng_message == 4:
            print(f'X {other_stats.name} was hit by a small island sized truck')
        elif rng_message == 5:
            print(f'X {other_stats.name} was exploadicated')
        elif rng_message == 6:
            print(f'X {other_stats.name} was boomed to the moon')
        elif rng_message == 7:
            print(f'X {other_stats.name} fell to a crit? lame...')
        elif rng_message == 8:
            print(f'X Critical hits are fair and balanced ({other_stats.name} fell)')
        elif rng_message == 9:
            print(f'X C R I T I C A L  H I T  ({other_stats.name} was downed)')
        elif rng_message == 10:
            print(f"X Imagine falling to a crit {other_stats.name}, couldn't be me")
    
    #normal deaths
    elif message == 1:
        rng_message = random.randint(1,13)
        if other_stats.id == var.SomethingStats.id:
            print(f"X I'm sorry")
        elif rng_message == 1:
            print(f'X {other_stats.name} fell!')
        elif rng_message == 2:
            print(f'X {other_stats.name} went down!')
        elif rng_message == 3:
            print(f'X {other_stats.name} became toast...')
        elif rng_message == 4:
            print(f'X {other_stats.name} bit the dust...')
        elif rng_message == 5:
            print(f'X {other_stats.name} O.K.')
        elif rng_message == 6:
            print(f'X {other_stats.name} down!')
        elif rng_message == 7:
            print(f'X {other_stats.name} stubbed their toe and fell')
        elif rng_message == 8:
            print(f'X {other_stats.name} fainted!')
        elif rng_message == 9:
            print(f'X {other_stats.name} needs to rest...')
        elif rng_message == 10:
            print(f'X {other_stats.name} tripped')
        elif rng_message == 11:
            print(f'X {other_stats.name} got oofed')
        elif rng_message == 12:
            print(f'X {other_stats.name} collapsed!')
        elif rng_message == 13:
            print(f'X {other_stats.name} got dunked on')
    
    #refuse messages
    elif message == 2:
        refuse_rng_mes = random.randint(1,5)
        if refuse_rng_mes == 1:
            print(f'/ But {other_stats.name} refused')
        elif refuse_rng_mes == 2:
            print(f'/ {other_stats.name} did not succumb')
        elif refuse_rng_mes == 3:
            print(f'/ But {other_stats.name} did not fall')
        elif refuse_rng_mes == 4:
            print(f'/ {other_stats.name} carried on anyway')
        elif refuse_rng_mes == 5:
            print(f'/ {other_stats.name} tanked the hit')
    else:
        print(f'? error death message')

#mesages used in skill/actions
def battle_messages(yr_stats, other_stats):
    """
    symbol key: (put at front of text mesages)
    ! attack
    % magic
    ~ miss
    # defend
    ] command
    ) other action
      nothing
    + heal/buff
    - debuff
    > dialogue
    * information
    ? check
    ^ upped
    X downed
    / refuse
    """
    #displays -CRIT- if thing was a crit
    crit ="-CRIT- " if yr_stats.crit > 0 else ""
    #norm hp showing
    if other_stats.health_type == 1 or other_stats.health_type == 2:
        if other_stats.cur_hp <= 0 and other_stats.refuse > 0:
            cur_hp = "1"
        elif other_stats.cur_hp <= 0:
            cur_hp = other_stats.cur_hp - 10
        else:
            cur_hp = other_stats.cur_hp
        show_health = f'{cur_hp}/{other_stats.max_hp}hp'
    #sp health type showing
    elif other_stats.health_type == 3:
        show_health = f'{other_stats.cur_sp}/{other_stats.max_sp}sp'
    #pwr health type showing
    elif other_stats.health_type == 4:
        if other_stats.cur_pwr <= 0 and other_stats.refuse > 0:
            cur_hp = "1"
        else:
            cur_hp = other_stats.cur_pwr
        show_health = f'{cur_hp}/{other_stats.max_pwr}pwr'
    else:
        show_health = 0
    #checks if the target is the same char as the user
    same = True if other_stats.id == yr_stats.id else False
    
    #miss mesages
    if yr_stats.miss == 0:
        rng_message = random.randint(1,3)
        if rng_message == 1:
            print(f'''~ {yr_stats.name}'s attack whiffs {other_stats.name}''')
        elif rng_message == 2:
            print(f'''~ {other_stats.name} narrowly dodged {yr_stats.name}'s attack''')
        elif rng_message == 3:
            print(f'''~ {yr_stats.name}'s attack misses {other_stats.name}''')
        elif rng_message == 0:
            print(f'''~ miss''')
    
    #nothing
    elif yr_stats.action == -1:
        print(f'  {yr_stats.name} does nothing')
    #basic attack
    elif yr_stats.action == 1:
        print(f'! {yr_stats.name} hits {other_stats.name} for {yr_stats.dmg}dmg {crit}({show_health})')
    #defending
    elif yr_stats.action == 2:
        print(f'# {yr_stats.name} defends')
    #heal
    elif yr_stats.action == 102 or yr_stats.action == 301:
        if other_stats.health_type == 1 or other_stats.health_type == 2:
            if same:
                if other_stats.cur_hp == other_stats.max_hp:
                    print(f'''+ {yr_stats.name} maxes out {pronouns(yr_stats, 3)} hp ({show_health})''')
                else:
                    print(f'+ {yr_stats.name} heals {pronouns(yr_stats, 5)} for {yr_stats.dmg}hp ({show_health})')
            else:
                if other_stats.cur_hp == other_stats.max_hp:
                    print(f'''+ {yr_stats.name} maxes out {other_stats.name}'s hp ({show_health})''')
                else:
                    print(f'+ {yr_stats.name} heals {other_stats.name} for {yr_stats.dmg}hp ({show_health})')
        else:
            if same:
                print(f'+ {yr_stats.name} heals {pronouns(yr_stats, 5)} for {yr_stats.dmg}hp (0/0hp)')
            else:
                print(f'+ {yr_stats.name} heals {other_stats.name} for {yr_stats.dmg}hp (0/0hp)')
    #multi-swipe
    elif yr_stats.action == 201:
        print(f'! {yr_stats.name} Swipes {other_stats.name} for {yr_stats.dmg}dmg {crit}({show_health})')
    #distract
    elif yr_stats.action == 202:
        num = random.randint(1,20)
        if num == 1:
            print(f') {yr_stats.name} distracks the enemys!')
        else:
            print(f') {yr_stats.name} distracts the enemys!') 
    #cheer
    elif yr_stats.action == 203:
        if other_stats.health_type == 1 or other_stats.health_type == 3:
            if same:
                if other_stats.cur_sp == other_stats.max_sp:
                    print(f'+ {yr_stats.name} cheers {pronouns(yr_stats, 5)} on, maxing out {pronouns(other_stats, 3)} sp ({other_stats.cur_sp}/{other_stats.max_sp}sp)')
                else:
                    print(f'+ {yr_stats.name} cheers {pronouns(yr_stats, 5)} on, restoring {yr_stats.dmg}sp ({other_stats.cur_sp}/{other_stats.max_sp}sp)')
            else:
                if other_stats.cur_sp == other_stats.max_sp:
                    print(f'+ {yr_stats.name} cheers {other_stats.name} on, maxing out {pronouns(other_stats, 3)} sp ({other_stats.cur_sp}/{other_stats.max_sp}sp)')
                else:
                    print(f'+ {yr_stats.name} cheers {other_stats.name} on, restoring {yr_stats.dmg}sp ({other_stats.cur_sp}/{other_stats.max_sp}sp)')
        else:
            if same:
                print(f'+ {yr_stats.name} cheers {pronouns(yr_stats, 5)} on, restoring {yr_stats.dmg}sp (0/0sp)')
            else:
                print(f'+ {yr_stats.name} cheers {other_stats.name} on, restoring {yr_stats.dmg}sp (0/0sp)')
    #burn
    elif yr_stats.action == 302:
        if yr_stats.to_party == 1:
            print(f'''- {other_stats.name}'s defences were lowered a little''')
        else:
            print(f'% {yr_stats.name} burns {other_stats.name} for {yr_stats.dmg}dmg {crit}({show_health})')
    #greencalm
    elif yr_stats.action == 303:
        if other_stats.health_type == 1:
            if same:
                print(f'''+ {yr_stats.name} calms {pronouns(yr_stats, 5)} for {yr_stats.dmg}hp and {yr_stats.crit}sp ({show_health})({other_stats.cur_sp}/{other_stats.max_sp}sp)''')
            else:
                print(f'''+ {yr_stats.name} calms {other_stats.name} for {yr_stats.dmg}hp and {yr_stats.crit}sp ({show_health})({other_stats.cur_sp}/{other_stats.max_sp}sp)''')
        elif other_stats.health_type == 2:
            if same:
                print(f'''+ {yr_stats.name} calms {pronouns(yr_stats, 5)} for {yr_stats.dmg}hp and {yr_stats.crit}sp ({show_health})(0/0sp)''')
            else:
                print(f'''+ {yr_stats.name} calms {other_stats.name} for {yr_stats.dmg}hp and {yr_stats.crit}sp ({show_health})(0/0sp)''')
        elif other_stats.health_type == 3:
            if same:
                print(f'''+ {yr_stats.name} calms {pronouns(yr_stats, 5)} for {yr_stats.dmg}hp and {yr_stats.crit}sp (0/0hp)({other_stats.cur_sp}/{other_stats.max_sp}sp)''')
            else:
                print(f'''+ {yr_stats.name} calms {other_stats.name} for {yr_stats.dmg}hp and {yr_stats.crit}sp (0/0hp)({other_stats.cur_sp}/{other_stats.max_sp}sp)''')
        else:
            if same:
                print(f'''+ {yr_stats.name} calms {pronouns(yr_stats, 5)} for {yr_stats.dmg}hp and {yr_stats.crit}sp (0/0hp)(0/0sp)''')
            else:
                print(f'''+ {yr_stats.name} calms {other_stats.name} for {yr_stats.dmg}hp and {yr_stats.crit}sp (0/0hp)(0/0sp)''')
    
    #shock
    elif yr_stats.action == 401:
        print(f'% {yr_stats.name} shocks {other_stats.name} for {yr_stats.dmg}dmg {crit}({show_health})')
    #storm calmdown
    elif yr_stats.action == 402:
        if other_stats.health_type == 1:
            print(f'''+ {yr_stats.name} calms down and recovers {yr_stats.dmg}hp and {yr_stats.crit}sp ({yr_stats.cur_hp}/{yr_stats.max_hp}hp)({yr_stats.cur_sp}/{yr_stats.max_sp}sp)''')
        elif other_stats.health_type == 2:
            print(f'''+ {yr_stats.name} calms down and recovers {yr_stats.dmg}hp and {yr_stats.crit}sp ({yr_stats.cur_hp}/{yr_stats.max_hp}hp)(0/0sp)''')
        elif other_stats.health_type == 3:
            print(f'''+ {yr_stats.name} calms down and recovers {yr_stats.dmg}hp and {yr_stats.crit}sp (0/0hp)({yr_stats.cur_sp}/{yr_stats.max_sp}sp)''')
        else:
            print(f'''+ {yr_stats.name} calms down and recovers {yr_stats.dmg}hp and {yr_stats.crit}sp (0/0hp)(0/0sp)''')
    #Charge
    elif yr_stats.action == 403:
        if yr_stats.charge > yr_stats.max_charge:
            print(f'+ {yr_stats.name} over charges')
        else:
            print(f'+ {yr_stats.name} charges up')
    #Spray
    elif yr_stats.action == 501:
        if yr_stats.crit == 1:
            print(f'! {yr_stats.name} sprays the enemys and lowers their def and sdf!')
        else:
            print(f'! {other_stats.name} takes {yr_stats.dmg}dmg {crit}({show_health})')
    #Gun
    elif yr_stats.action == 502:
        print(f'! {yr_stats.name} shoots {other_stats.name} for {yr_stats.dmg}dmg ({show_health})')
    #Cook
    elif yr_stats.action == 601:
        rng_message = random.randint(1,3)
        #lk given
        if other_stats.id == 1 and rng_message == 1:
            print(f'+ {yr_stats.name} gives a potato to {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        #taco given
        elif other_stats.id == 2 and rng_message == 1:
            print(f'+ {yr_stats.name} cooks some chips for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        #green given
        elif other_stats.id == 3 and rng_message == 1:
            print(f'+ {yr_stats.name} cooks a bean for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        #storm given
        elif other_stats.id == 4 and rng_message == 1:
            print(f'+ {yr_stats.name} cooks some tea(foodflavor) for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        #hamy given
        elif other_stats.id == 5 and rng_message == 1:
            print(f'+ {yr_stats.name} cooks some tofu for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        #creation given
        elif other_stats.id == 6 and rng_message == 1:
            print(f'+ {yr_stats.name} cooks some breakfast gears for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        #willow given
        elif other_stats.id == 7 and rng_message == 1:
            print(f'+ {yr_stats.name} cooks some ice cubes for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        #fred given
        elif other_stats.id == 99 and rng_message == 1:
            print(f'+ {yr_stats.name} cooks some mushrooms for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        #error given
        elif other_stats.id == 100 and rng_message == 1:
            print(f'+ {yr_stats.name} cooks some [ERROR] for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
        else:
            rng_message = random.randint(1,9)
            if rng_message == 1:
                print(f'+ {yr_stats.name} cooks some dinosaur egg oatmeal for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            elif rng_message == 2:
                print(f'+ {yr_stats.name} cooks some pancakes for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            elif rng_message == 3:
                print(f'+ {yr_stats.name} cooks some garlicbread for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            elif rng_message == 4:
                print(f'+ {yr_stats.name} cooks some MEAT? for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            elif rng_message == 5:
                print(f'+ {yr_stats.name} cooks some cheese for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            elif rng_message == 6:
                print(f'+ {yr_stats.name} cooks some pet friendly chocolate for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            elif rng_message == 7:
                print(f'+ {yr_stats.name} cooks some tofu for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            elif rng_message == 8:
                print(f'+ {yr_stats.name} cooks some mango-toothpaste for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            elif rng_message == 9:
                print(f'+ {yr_stats.name} cooks some eggplant for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
            else:
                print(f'+ {yr_stats.name} cooks some food for {other_stats.name}, it heals {yr_stats.dmg}hp ({show_health})')
    #IcyWind
    elif yr_stats.action == 701:
        print(f'% {yr_stats.name} freezes {other_stats.name} for {yr_stats.dmg}dmg {crit}({show_health})')
    #RED HANDS
    elif yr_stats.action == 9901:
        print(f'! {yr_stats.name} ERASES {other_stats.name}, it dealt {yr_stats.dmg}dmg {crit}({show_health})')
    #SNOWGRAVE
    elif yr_stats.action == 9902:
        print(f'% {yr_stats.name} casts SNOWGRAVE on {other_stats.name}, it dealt {yr_stats.dmg}dmg {crit}({show_health})')
        
    #error mesages
    elif yr_stats.action == 696969:
        print('* nicenicenice')
    else:
        print('? Error message!')








