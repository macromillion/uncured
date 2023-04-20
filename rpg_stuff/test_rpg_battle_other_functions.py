'''
this file contains general functions
'''
import test_rpg_config as con
import test_rpg_battle_stats_and_vars as var
import test_rpg_battle_skills as skl
import test_rpg_battle_skill_list as lst
import test_rpg_battle_messages_display as mes
import random

#used for side mesages
side_text = ''

#DEBUG
def debug():
    print(f'--DEBUG----------------------------------------------')
    print(f'e1: {var.e1Stats.spray_debuff_turn}')
    print(f'e2: {var.e2Stats.spray_debuff_turn}')
    print(f'e3: {var.e3Stats.spray_debuff_turn}')
    print(f'e4: {var.e4Stats.spray_debuff_turn}')
    """
    print(f'e1: buffs:')
    print(f'atk x{var.e1Stats.attack_buff}')
    print(f'mag x{var.e1Stats.magic_buff}')
    print(f'def x{var.e1Stats.defence_buff}')
    print(f'spdef x{var.e1Stats.spirit_defence_buff}')
    print(f'luk x{var.e1Stats.luck_buff}')
    print(f'spd x{var.e1Stats.speed_buff}')
    print()
    print(f'def x{var.p1Stats.defence_buff}')
    print(f'def x{var.p2Stats.defence_buff}')
    """
    """
    print(f'pL rage: {var.pLStats.rage}')
    print(f'p1 rage: {var.p1Stats.rage}')
    print(f'p2 rage: {var.p2Stats.rage}')
    print(f'p3 rage: {var.p3Stats.rage}')
    print()
    print(f'e1 rage: {var.e1Stats.rage}')
    print(f'e2 rage: {var.e2Stats.rage}')
    print(f'e3 rage: {var.e3Stats.rage}')
    print(f'e4 rage: {var.e4Stats.rage}')
    """
    """
    print(f'pL did crit {var.pLStats.crit}')
    print(f'pL did by how much {var.pLStats.crit_multi}')
    print(f'pL dmg {var.pLStats.dmg}')
    print(f'pL miss {var.pLStats.miss}')
    print(f'pL defend {var.pLStats.defending}')
    print()
    print(f'p1 did crit {var.p1Stats.crit}')
    print(f'p1 did by how much {var.p1Stats.crit_multi}')
    print(f'p1 dmg {var.p1Stats.dmg}')
    print(f'p1 miss {var.p1Stats.miss}')
    print(f'p1 defend {var.p1Stats.defending}')
    print()
    print(f'p2 did crit {var.p2Stats.crit}')
    print(f'p2 did by how much {var.p2Stats.crit_multi}')
    print(f'p2 dmg {var.p2Stats.dmg}')
    print(f'p2 miss {var.p2Stats.miss}')
    print(f'p2 defend {var.p2Stats.defending}')
    print()
    print(f'p3 did crit {var.p3Stats.crit}')
    print(f'p3 did by how much {var.p3Stats.crit_multi}')
    print(f'p3 dmg {var.p3Stats.dmg}')
    print(f'p3 miss {var.p3Stats.miss}')
    print(f'p3 defend {var.p3Stats.defending}')
    print()
    """
    """
    print(var.LostKidStats())
    print(var.pLStats())
    print()
    print(f'pL weapon name: {var.pLStats.weapon_name}')
    print(f'type: h{var.pLStats.weapon_type_hand} c{var.pLStats.weapon_type_cut} sw{var.pLStats.weapon_type_swipe} p{var.pLStats.weapon_type_poke} sl{var.pLStats.weapon_type_slam}')
    print(f'pL armor name: {var.pLStats.armor_name}')
    print(f'p3 armor name: {var.pLStats.charm_name}')
    print()
    print(var.TacoStats())
    print(var.p1Stats())
    print()
    print(f'p1 weapon name: {var.p1Stats.weapon_name}')
    print(f'type: h{var.p1Stats.weapon_type_hand} c{var.p1Stats.weapon_type_cut} sw{var.p1Stats.weapon_type_swipe} p{var.p1Stats.weapon_type_poke} sl{var.p1Stats.weapon_type_slam}')
    print(f'p1 armor name: {var.p1Stats.armor_name}')
    print(f'p3 armor name: {var.p1Stats.charm_name}')
    print()
    print(var.GreenStats())
    print(var.p2Stats())
    print()
    print(f'p2 weapon name: {var.p2Stats.weapon_name}')
    print(f'type: h{var.p2Stats.weapon_type_hand} c{var.p2Stats.weapon_type_cut} sw{var.p2Stats.weapon_type_swipe} p{var.p2Stats.weapon_type_poke} sl{var.p2Stats.weapon_type_slam}')
    print(f'p2 armor name: {var.p2Stats.armor_name}')
    print(f'p3 armor name: {var.p2Stats.charm_name}')
    print()
    print(var.StormStats())
    print(var.p3Stats())
    print()
    print(f'p3 weapon name: {var.p3Stats.weapon_name}')
    print(f'type: h{var.p3Stats.weapon_type_hand} c{var.p3Stats.weapon_type_cut} sw{var.p3Stats.weapon_type_swipe} p{var.p3Stats.weapon_type_poke} sl{var.p3Stats.weapon_type_slam}')
    print(f'p3 armor name: {var.p3Stats.armor_name}')
    print(f'p3 armor name: {var.p3Stats.charm_name}')
    print()
    print(f'? {var.pLStats.name}, action:{var.pLStats.action}, target:{var.pLStats.target}, target2:{var.pLStats.target2}')
    print(f'? {var.p1Stats.name}, action:{var.p1Stats.action}, target:{var.p1Stats.target}, target2:{var.p1Stats.target2}')
    print(f'? {var.p2Stats.name}, action:{var.p2Stats.action}, target:{var.p2Stats.target}, target2:{var.p2Stats.target2}')
    print(f'? {var.p3Stats.name}, action:{var.p3Stats.action}, target:{var.p3Stats.target}, target2:{var.p3Stats.target2}')
    """
    print(f'-----------------------------------------------------')

#my friend told me to add this (ignore)
def shovel_rng():
    shovel = random.randint(1,500)
    if shovel == 50:
        print('shovel')
    else:
        print()
    
#checks if the char exists
def check_for_char(who, team):
    #on party side
    if team.lower() == 'party':
        if who == var.pLStats.id or who == var.p1Stats.id or who == var.p2Stats.id or who == var.p3Stats.id:
            return True
        else:
            return False
    #on enemy side
    elif team.lower() == 'enemy':
        if who == var.e1Stats.id or who == var.e2Stats.id or who == var.e3Stats.id or who == var.e4Stats.id:
            return True
        else:
            return False
    else:
        return "ha ha i will now crash your gam (you put in wrong team type nerd) (lolololllllo)"
    
#--reset-----------------------
#resets some general stats
def action_reset(stats):
    stats.action  = 0
    stats.target  = 0
    stats.target2 = 0
    stats.targeted = 0
    stats.to_party = 0
    stats.defending = 1
    stats.dmg  = 0
    stats.crit = 0
    stats.crit_multi = 1
    stats.miss = 1
    stats.damaged = 0
    

#--targeting----------------------------------------------
#chooses the type of targeting (only one is implemented)
def enemy_choosing_target(stats):
    if 1 == 2:
        stats.target = 1
    else:
        stats.target = basic_enemy_targeting()
    
    #used to grab agro in skills
def targeted_enemy_targeting():
    if   var.pLStats.targeted == 1 and var.pLStats.exists == 1 and var.pLStats.alive == 1:
        return 1
    elif var.p1Stats.targeted == 1 and var.p1Stats.exists == 1 and var.p1Stats.alive == 1:
        return 2
    elif var.p2Stats.targeted == 1 and var.p2Stats.exists == 1 and var.p2Stats.alive == 1:
        return 3
    elif var.p3Stats.targeted == 1 and var.p3Stats.exists == 1 and var.p3Stats.alive == 1:
        return 4
    else:
        return 0

    #normal targeting, cant hit pL if  at least 2 membs are up
def basic_enemy_targeting():
    #pL = 1
    #p1 = 2
    #p2 = 3
    #p3 = 4
    #check if anyone has agro
    if targeted_enemy_targeting() != 0:
        return targeted_enemy_targeting()
    #checks for amount of party alive
    total_alive = var.pLStats.alive + var.p1Stats.alive + var.p2Stats.alive + var.p3Stats.alive
    targeting = True
    #will keep cycling until a valid member is selected
    while targeting:
        num =  random.randint(1,4)
        
        if num == 1 and total_alive <= lst.max_num_of_membs_alive_to_hit_pl_including_pl and var.pLStats.exists == 1 and var.pLStats.alive == 1:
            return 1
        elif num == 2 and var.p1Stats.exists == 1 and var.p1Stats.alive == 1:
            return 2
        elif num == 3 and var.p2Stats.exists == 1 and var.p2Stats.alive == 1:
            return 3
        elif num == 4 and var.p3Stats.exists == 1 and var.p3Stats.alive == 1:
            return 4
        elif total_alive == 0:
            return 0
    
    
#how the party targets
def party_targeting(stats, team):
    global turn
    
    #setup
    command_targeting = 1
    while command_targeting == 1:
        #who we are selecting
        if team == 'enemy':
            mes.targets()
            stats.to_party = 0
        elif team == 'party':
            mes.targets_allies()
            stats.to_party = 1
            
        target_who = input()
            #enemy 1 / pL
        if target_who == con.option_1 and (team == 'enemy' or var.pLStats.exists):
            stats.target = 1
            command_targeting = 0
            turn = 0
            #enemy2 / p1
        elif target_who == con.option_2 and (team == 'enemy' or var.p1Stats.exists):
            stats.target = 2 
            command_targeting = 0
            turn = 0
            #enemy 3 / p2
        elif target_who == con.option_3 and (team == 'enemy' or var.p2Stats.exists):
            stats.target = 3    
            command_targeting = 0
            turn = 0
            #enemy 4 / p3
        elif target_who == con.option_4 and (team == 'enemy' or var.p3Stats.exists):
            stats.target = 4    
            command_targeting = 0
            turn = 0
        #back
        elif target_who == con.option_back:
            command_targeting = 0
            stats.action = 0
            stats.to_party = 0

#corrects target if it had been defeated
def party_target_correction(stats,target):
    for i in range(2):
        if target == 1 and var.e1Stats.exists == 0:
            target = 2
        if target == 2 and var.e2Stats.exists == 0:
            target = 3
        if target == 3 and var.e3Stats.exists == 0:
            target = 4
        if target == 4 and var.e4Stats.exists == 0:
            target = 1
    
    if var.e1Stats.exists == 0 and var.e2Stats.exists == 0 and var.e3Stats.exists == 0 and var.e4Stats.exists == 0:
        stats.action = 0
        target = 0
    return target

#translates target numbers into stats (for party)
def party_target_translator(target):
    if target == 1:
        return var.e1Stats
    elif target == 2:
        return var.e2Stats
    elif target == 3:
        return var.e3Stats
    elif target == 4:
        return var.e4Stats
    else:
        return var.NullStats

#translates target numbers into stats (for enemys)
def enemy_target_translator(target):
    if target == 1:
        return var.pLStats
    elif target == 2:
        return var.p1Stats
    elif target == 3:
        return var.p2Stats
    elif target == 4:
        return var.p3Stats
    else:
        return var.NullStats

#--buffs-------------------------------------------------
#adds/substracts buffs, wont let a buf go below 0
def buff_calc(stats, typpe, amount):
    if stats.debuff_immune == 0:
        if typpe == 'atk':
            stats.attack_buff += amount
            if stats.attack_buff < 0:
                stats.attack_buff = 0.0000001
        elif typpe == 'mag':
            stats.magic_buff += amount
            if stats.magic_buff < 0:
                stats.magic_buff = 0.0000001
        elif typpe == 'def':
            stats.defence_buff += amount
            if stats.defence_buff < 0:
                stats.defence_buff = 0.0000001
        elif typpe == 'spdef' or typpe == 'sdf':
            stats.spirit_defence_buff += amount
            if stats.spirit_defence_buff < 0:
                stats.spirit_defence_buff = 0.0000001
        elif typpe == 'luk':
            stats.luck_buff += amount
            if stats.luck_buff < 0:
                stats.luck_buff = 0.0000001
        elif typpe == 'spd':
            stats.speed_buff += amount
            if stats.speed_buff < 0:
                stats.speed_buff = 0.0000001
        else:
            print('* YOU PUT IN THE WRONG BUFF TYPE NERD.')

#end of turn removes unactive buffs then re-adds still active buffs
def buff_check(stats):
    stats.attack_buff = 1
    stats.magic_buff = 1
    stats.defence_buff = 1
    stats.spirit_defence_buff = 1
    stats.luck_buff = 1
    stats.speed_buff = 1
    if stats.debuff_immune == 0:
        #green def/sdf debuff
        for i in range(stats.burn_debuff_num):
            buff_calc(stats, 'def', lst.debuff_burn)
            buff_calc(stats, 'spdef', lst.debuff_burn)
        #hamy def/sdf debuff
        if stats.spray_debuff_turn >= 1:
            stats.spray_debuff_turn -= 1
            buff_calc(stats, 'def', lst.debuff_spray)
            buff_calc(stats, 'spdef', lst.debuff_spray)

#removes buffs used in some skills, can also be used for healing
def buff_removal(stats, give_return):
    heal = 0
    for buff in [stats.attack_buff, stats.magic_buff, stats.defence_buff, stats.spirit_defence_buff, stats.luck_buff, stats.speed_buff]:
        heal += int(abs(buff - 1) * 10)
    
    if stats.burn_debuff_num >= 1:
        stats.burn_debuff_num -= 1
    stats.spray_debuff_turn = 0

    buff_check(stats)
    if give_return == 1:
        return heal

#--hp-stuff------------------------------------------------
#checks if a health type is above 0
def health_check(stats):
    if (stats.cur_hp > 0 and (stats.health_type == 1 or stats.health_type == 2)) or (stats.cur_sp >= 0 and stats.health_type == 3) or (stats.cur_pwr > 0 and stats.health_type == 4):
        return True
    else:
        return False
    
    #subs health for each health type
def health_sub_calc(stats, target_stats):
    if stats.health_type == 3:
        stats.miss = 0
    if target_stats.health_type == 1 or target_stats.health_type == 2:
        target_stats.cur_hp -= stats.dmg * stats.miss
    elif target_stats.health_type == 3:
        stats.miss = 0
    elif target_stats.health_type == 4:
        if target_stats.cur_pwr - stats.dmg * stats.miss >= 0:
            target_stats.cur_pwr -= stats.dmg * stats.miss
        else:
            target_stats.cur_pwr = 0

    #adds pwr
def pwr_add_calc(stats, amount):
    if stats.cur_pwr + amount <= stats.max_pwr:
            stats.cur_pwr += amount
    elif stats.cur_pwr > stats.max_pwr:
        pass
    else:
        stats.cur_pwr = stats.max_pwr
    
    #subs pwr
def pwr_sub_calc(stats, amount):
    if stats.cur_pwr - amount >= 0:
            stats.cur_pwr -= amount
    else:
        stats.cur_pwr = 0

    #adds hp
def hp_add_calc(stats, hp_amount):
    if stats.health_type == 1 or stats.health_type == 2:
        if stats.cur_hp + hp_amount <= stats.max_hp:
            stats.cur_hp += hp_amount
        elif stats.cur_hp > stats.max_hp:
            pass
        else:
            stats.cur_hp = stats.max_hp

    #checks for a refuse
def refuse_check(yr_stats, eny_stats):
    if not health_check(eny_stats):
        if eny_stats.refuse > 0:
            eny_stats.cur_hp = 1
            eny_stats.cur_pwr = 1
            eny_stats.refuse -= 1
            mes.downed_refuse_messages(2, yr_stats, eny_stats)
        else:
            down_check_full()
            #mes.downed_refuse_messages(1, yr_stats, eny_stats)

    #full heals the party
def party_full_heal():
    var.pLStats.cur_hp = var.pLStats.max_hp
    var.pLStats.cur_sp = var.pLStats.max_sp
    var.pLStats.cur_pwr = var.pLStats.max_pwr
    
    var.p1Stats.cur_hp = var.p1Stats.max_hp
    var.p1Stats.cur_sp = var.p1Stats.max_sp
    var.p1Stats.cur_pwr = var.p1Stats.max_pwr
    
    var.p2Stats.cur_hp = var.p2Stats.max_hp
    var.p2Stats.cur_sp = var.p2Stats.max_sp
    var.p2Stats.cur_pwr = var.p2Stats.max_pwr
    
    var.p3Stats.cur_hp = var.p3Stats.max_hp
    var.p3Stats.cur_sp = var.p3Stats.max_sp
    var.p3Stats.cur_pwr = var.p3Stats.max_pwr
    
    end_battle_hp_sp(var.pLStats)
    end_battle_hp_sp(var.p1Stats)
    end_battle_hp_sp(var.p2Stats)
    end_battle_hp_sp(var.p3Stats)
    
 #full heals the enemys
def enemy_full_heal():
    var.e1Stats.cur_hp = var.e1Stats.max_hp
    var.e1Stats.cur_sp = var.e1Stats.max_sp
    var.e1Stats.cur_pwr = var.e1Stats.max_pwr
    
    var.e2Stats.cur_hp = var.e2Stats.max_hp
    var.e2Stats.cur_sp = var.e2Stats.max_sp
    var.e2Stats.cur_pwr = var.e2Stats.max_pwr
    
    var.e3Stats.cur_hp = var.e3Stats.max_hp
    var.e3Stats.cur_sp = var.e3Stats.max_sp
    var.e3Stats.cur_pwr = var.e3Stats.max_pwr
    
    var.e4Stats.cur_hp = var.e4Stats.max_hp
    var.e4Stats.cur_sp = var.e4Stats.max_sp
    var.e4Stats.cur_pwr = var.e4Stats.max_pwr
    
    end_battle_hp_sp(var.e1Stats)
    end_battle_hp_sp(var.e2Stats)
    end_battle_hp_sp(var.e3Stats)
    end_battle_hp_sp(var.e4Stats)

#adds 1 to hp if battle ends and is below 0
def end_battle_hp_sp(stats):
    if stats.cur_hp <= 0:
        stats.cur_hp = 1
    if stats.cur_sp <= 0:
        stats.cur_sp = 0
    if stats.cur_pwr <= 0:
        stats.cur_pwr = 1
    
    if stats.id == var.LostKidStats.id:
        con.lk_cur_hp = stats.cur_hp
        con.lk_cur_sp = stats.cur_sp
    
    elif stats.id == var.TacoStats.id:
        con.taco_cur_hp = stats.cur_hp
        con.taco_cur_sp = stats.cur_sp
    
    elif stats.id == var.GreenStats.id:
        con.green_cur_hp = stats.cur_hp
        con.green_cur_sp = stats.cur_sp
    
    elif stats.id == var.StormStats.id:
        con.storm_cur_hp = stats.cur_hp
        con.storm_cur_sp = stats.cur_sp
        
    if stats.id == var.HamyStats.id:
        con.hamy_cur_hp = stats.cur_hp
        con.hamy_cur_sp = stats.cur_sp
    
    elif stats.id == var.CreationStats.id:
        con.creation_cur_pwr = stats.cur_pwr
    
    elif stats.id == var.WillowStats.id:
        con.willow_cur_hp = stats.cur_hp
        con.willow_cur_sp = stats.cur_sp
    
    elif stats.id == var.FredStats.id:
        con.fred_cur_hp = stats.cur_hp
        
    elif stats.id == var.ErrorStats.id:
        con.error_cur_sp = stats.cur_sp

#--sp-stuff---------------------------------------------------------------------

#adds sp
def sp_add_calc(stats, sp_amount):
    if stats.cur_sp + sp_amount <= stats.max_sp:
        stats.cur_sp += sp_amount
    elif stats.cur_sp > stats.max_sp:
        pass
    else:
        stats.cur_sp = stats.max_sp
 
#subs sp if miss
def sp_cost_miss(yr_stats, eny_stats):
    if yr_stats.miss == 0:
        if eny_stats.party_slot <= 0:
            sp_sub_calc(eny_stats, lst.cost_miss)
        else:
            sp_sub_calc(eny_stats, lst.cost_party_miss)

#subs sp
def sp_sub_calc(stats, amount):
    if stats.health_type == 4:
        pwr_sub_calc(stats, amount * lst.pwr_exchange_rate)
    else:
        if stats.cur_sp - amount >= 0:
            stats.cur_sp -= amount
        else:
            stats.cur_sp = 0

#--rage-suff--------------------------------------------------------------

#-RAGE IS UNUSED-

#adds rage
def rage_add_calc(stats, amount):
    if stats.miss == 0:
        miss = 2
    else:
        miss = 1
        
    rage_add = amount * stats.rage_multi * miss
    
    if stats.rage + rage_add <= stats.max_rage:
        stats.rage += rage_add
    elif stats.rage > stats.max_rage:
        pass
    else:
        stats.rage = stats.max_rage

#adds rage to party
def rage_add_all_party(amount):
    if var.pLStats.exists == 1 and var.pLStats.alive == 1:
        hold = var.pLStats.miss 
        var.pLStats.miss = 1
        rage_add_calc(var.pLStats, amount)
        var.pLStats.miss = hold
    if var.p1Stats.exists == 1 and var.p1Stats.alive == 1:
        hold = var.p1Stats.miss 
        var.p1Stats.miss = 1
        rage_add_calc(var.p1Stats, amount)
        var.p1Stats.miss = hold
    if var.p2Stats.exists == 1 and var.p2Stats.alive == 1:
        hold = var.p2Stats.miss 
        var.p2Stats.miss = 1
        rage_add_calc(var.p2Stats, amount)
        var.p2Stats.miss = hold
    if var.p3Stats.exists == 1 and var.p3Stats.alive == 1:
        hold = var.p3Stats.miss 
        var.p3Stats.miss = 1
        rage_add_calc(var.p3Stats, amount)
        var.p3Stats.miss = hold

#adds rage to all enemys
def rage_add_all_enemy(amount):
    if var.e1Stats.exists == 1:
        hold = var.e1Stats.miss 
        var.e1Stats.miss = 1
        rage_add_calc(var.e1Stats, amount)
        var.e1Stats.miss = hold
    if var.e2Stats.exists == 1:
        hold = var.e2Stats.miss 
        var.e2Stats.miss = 1
        rage_add_calc(var.e2Stats, amount)
        var.e2Stats.miss = hold
    if var.e3Stats.exists == 1:
        hold = var.e3Stats.miss 
        var.e3Stats.miss = 1
        rage_add_calc(var.e3Stats, amount)
        var.e3Stats.miss = hold
    if var.e4Stats.exists == 1:
        hold = var.e4Stats.miss 
        var.e4Stats.miss = 1
        rage_add_calc(var.e4Stats, amount)
        var.e4Stats.miss = hold
        

#--charge-stuff--------------------------------------------------------------
#adds chrg
def charge_add_calc(stats, amount):
    if stats.charge + amount <= stats.max_charge:
        stats.charge += amount
    elif stats.charge > stats.max_charge:
        pass
    else:
        stats.charge = stats.max_charge
    
#--downed-stuff--------------------------------------------------
#check if enyone is downed
def down_check_full():
    party_down_calc(var.pLStats)
    party_down_calc(var.p1Stats)
    party_down_calc(var.p2Stats)
    party_down_calc(var.p3Stats)
    
    enemy_down_calc(var.e1Stats)
    enemy_down_calc(var.e2Stats)
    enemy_down_calc(var.e3Stats)
    enemy_down_calc(var.e4Stats)

#if pL is down end game/ if no pL and all pMs are down
def pl_down_calc():
    if (var.pLStats.exists == 1 and var.pLStats.alive == 0) or var.pLStats.exists == 0 and (var.p1Stats.alive == 0 or var.p1Stats.exists == 0) and (var.p2Stats.alive == 0 or var.p2Stats.exists == 0) and (var.p3Stats.alive == 0 or var.p3Stats.exists == 0):
        print()
        var.currently_battling = 0
        print(f'You lost...')
        input()

#check if all enemys are down, gives win
def all_enemy_down_calc():
    total_alive = var.e1Stats.alive + var.e2Stats.alive + var.e3Stats.alive + var.e4Stats.alive
    if total_alive == 0:
        print()
        var.currently_battling = 0
        print(f'YOU WON!')
        input()

#punishes pM if gone down
def party_down_calc(stats):
    if not health_check(stats) and stats.damaged >= 1:
        if stats.alive > 0:
            buff_removal(stats, 0)
            mes.downed_refuse_messages(1, var.NullStats, stats)
            stats.alive = 0
            stats.cur_hp -= 10
            rage_add_all_party(8)

#makes enemys stop existing if they are downed
def enemy_down_calc(stats):
    if not health_check(stats) and stats.damaged >= 1:
        stats.exists = 0
        if stats.alive > 0:
            buff_removal(stats, 0)
            mes.downed_refuse_messages(1, var.NullStats, stats)
            stats.alive = 0
            rage_add_all_enemy(8)

#check if pM has positive hp
def upped_check(stats):
    if stats.alive == 0 and stats.damaged == 0 and stats.exists == 1:
        if stats.id == 3 and stats.cur_hp <= 0:
            hp_add_calc(stats, 8)
        elif stats.cur_hp <= 0:
            hp_add_calc(stats, 5)
        if stats.cur_hp > 0:
            rage_add_all_party(-5)
            stats.alive = 1
        if stats.id == 4 or stats.id == 1:
            stats.refuse = 1

#--turn-stuff--------------------------------------

def party_turn(stats):
    global turn
    global side_text
    global first_action
    
    #start!
    turn = 1
    while turn == 1:
        if not first_action:
            mes.clear_screen()
            mes.display_hp_and_sp()
        else:
            first_action = False
        
        mes.party_actions(stats, side_text)
        action_command = input()
        side_text = ''
        
        #fight
        if action_command == con.option_1:
            stats.action = 1
            print(f'Fight who?')
            party_targeting(stats, 'enemy')
            
        #command (leader only) unfin
        elif action_command == con.option_2 and stats.id == 1:
            skl.skill_choosing(stats)
        
        #skill (partymembs)
        elif action_command == con.option_2 and stats.id != 1:
            skl.skill_choosing(stats)
        
        #defend
        elif action_command == con.option_3:
            stats.action = 2
            turn = 0
        
        #run (leader only)
        elif action_command == con.option_4 and stats.party_slot == 1:
            stats.action = 0
            total = 0
            not_enough_sp = 0
            for pstats in [var.pLStats, var.p1Stats, var.p2Stats, var.p3Stats]:
                if pstats.exists == 0:
                    total += 1
                else:
                    if (pstats.health_type == 1 or pstats.health_type == 3) and pstats.alive == 1:
                        if pstats.cur_sp >= lst.run_battle_cost:
                            total += 1
                        else:
                            not_enough_sp += 1
                    elif pstats.health_type == 2 and pstats.alive == 1:
                        total += 1
                    elif pstats.health_type == 4 and pstats.alive == 1:
                        if pstats.cur_pwr >= lst.run_battle_cost * lst.pwr_exchange_rate:
                            total += 1
                        else:
                            not_enough_sp += 1
            if total >= 4:
                print()
                var.running = 1
                var.currently_battling = 0
                turn = 0
                sp_sub_calc(var.pLStats, lst.run_battle_cost)
                sp_sub_calc(var.p1Stats, lst.run_battle_cost)
                sp_sub_calc(var.p2Stats, lst.run_battle_cost)
                sp_sub_calc(var.p3Stats, lst.run_battle_cost)
                print(f'The party ran!')
                input()
            elif not_enough_sp >= 1:
                side_text = f'(not enough sp)'
            else:
                side_text = f"(you can't leave a friend behind!)"
        
        #previous member
        elif action_command == con.option_back:
            # 3 -> 2
            if var.current_member_turn == 4 and var.p2Stats.alive == 1:
                var.current_member_turn = 2
                action_reset(stats)
                action_reset(var.p2Stats)
                turn = 0
            # 3 -> 1
            elif var.current_member_turn == 4 and var.p1Stats.alive == 1:
                var.current_member_turn = 1
                action_reset(stats)
                action_reset(var.p1Stats)
                turn = 0
            # 3 -> L
            elif var.current_member_turn == 4 and var.pLStats.alive == 1:
                var.current_member_turn = 0
                action_reset(stats)
                action_reset(var.pLStats)
                turn = 0
            # 2 -> 1
            elif var.current_member_turn == 3 and var.p1Stats.alive == 1:
                var.current_member_turn = 1
                action_reset(stats)
                action_reset(var.p1Stats)
                turn = 0
            # 2 -> L
            elif var.current_member_turn == 3 and var.pLStats.alive == 1:
                var.current_member_turn = 0
                action_reset(stats)
                action_reset(var.pLStats)
                turn = 0
            # 1 -> L
            elif var.current_member_turn == 2 and var.pLStats.alive == 1:
                var.current_member_turn = 0
                action_reset(stats)
                action_reset(var.pLStats)
                turn = 0
            else:
                side_text = f'(There was no one behind {stats.name})'
            
        #nothing
        elif action_command == con.option_nothing:
            stats.action = -1
            turn = 0
        
        #error
        else:
            side_text = '(invalid command)'



