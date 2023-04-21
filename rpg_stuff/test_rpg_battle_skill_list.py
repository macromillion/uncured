"""
this file contains skill stats and dmg calcs
"""
import test_rpg_battle_other_functions as func
import test_rpg_battle_messages_display as mes
import random


#--sp-costs--------------------------------------------
#general
cost_gain_basic_attack = 3
cost_gain_defending = 6
cost_basic_attack_pwr = 5
cost_gain_defending_pwr = 15
cost_miss = 3
cost_party_miss = 3
run_battle_cost = 4
#rage gain from being hit
gain_rage_hit = 1
pwr_exchange_rate = 5
max_num_of_membs_alive_to_hit_pl_including_pl = 2

#debuffs
debuff_spray = -0.2
debuff_burn = -0.06
max_burn_amount = 5

def resistance_calc(yr_stats,eny_stats, skill_stats, skilling):
    total = 1
    
    #-stat related resists
    if yr_stats.id == 1:
        total *= eny_stats.resist_lost_kid
    if yr_stats.id == 2:
        total *= eny_stats.resist_taco
    if yr_stats.id == 3:
        total *= eny_stats.resist_green
    if yr_stats.id == 4:
        total *= eny_stats.resist_storm
    if yr_stats.id == 5:
        total *= eny_stats.resist_hamy
    if yr_stats.id == 6:
        total *= eny_stats.resist_creation
    if yr_stats.id == 7:
        total *= eny_stats.resist_willow
    if yr_stats.id == 99:
        total *= eny_stats.resist_fred
    
    #weapon resists
    if yr_stats.weapon_type_hand - skilling >= 1 or skill_stats.type_hand >= 1:
        total *= eny_stats.resist_hand
    if yr_stats.weapon_type_cut - skilling >= 1 or skill_stats.type_cut  >= 1:
        total *= eny_stats.resist_cut
    if yr_stats.weapon_type_swipe - skilling >= 1 or skill_stats.type_swipe >= 1:
        total *= eny_stats.resist_swipe
    if yr_stats.weapon_type_poke - skilling >= 1 or skill_stats.type_poke >= 1:
        total *= eny_stats.resist_poke
    if yr_stats.weapon_type_slam - skilling >= 1 or skill_stats.type_slam >= 1:
        total *= eny_stats.resist_slam
    if yr_stats.weapon_type_whack - skilling >= 1 or skill_stats.type_whack >= 1:
        total *= eny_stats.resist_whack
    if yr_stats.weapon_type_projectile - skilling >= 1 or skill_stats.type_projectile >= 1:
        total *= eny_stats.resist_projectile
    
    #skill resists
    if skill_stats.type_phyical >= 1:
        total *= eny_stats.resist_phyical
    if skill_stats.type_magic >= 1:
        total *= eny_stats.resist_magic
    if skill_stats.type_spector >= 1:
        total *= eny_stats.resist_spector
    if skill_stats.type_fire >= 1:
        total *= eny_stats.resist_fire
    if skill_stats.type_electric >= 1:
        total *= eny_stats.resist_electric
    if skill_stats.type_ice >= 1:
        total *= eny_stats.resist_ice
    if skill_stats.type_plant  >= 1:
        total *= eny_stats.resist_plant
    if skill_stats.type_antiplant  >= 1:
        total *= eny_stats.resist_antiplant
    if skill_stats.type_shadow  >= 1:
        total *= eny_stats.resist_shadow
    if skill_stats.type_illusion >= 1:
        total *= eny_stats.resist_illusion
    if skill_stats.type_holy >= 1:
        total *= eny_stats.resist_holy
    if skill_stats.type_hydro >= 1:
        total *= eny_stats.resist_hydro
    if skill_stats.type_food >= 1:
        total *= eny_stats.resist_food
    
    return total

#calcs miss based on yr and eny spd
def miss_calc(yr_stats, eny_stats):
    if (eny_stats.cur_sp >= cost_miss and eny_stats.party_slot >= 0) or (eny_stats.cur_sp >= cost_party_miss and eny_stats.party_slot < 0):
        if random.randint(1,30) <= (2 + (eny_stats.speed*2 *eny_stats.speed_buff) - (yr_stats.speed *yr_stats.speed_buff)):
            yr_stats.miss = 0
        else:
            yr_stats.miss = 1
    else:
        yr_stats.miss = 1

#calcs crit based on yr and eny luk
def crit_calc(yr_stats, eny_stats):

    crit_numb = random.randint(1,100)
    if crit_numb <= (10 + (yr_stats.luck_buff * yr_stats.luck * 2) - (eny_stats.luck_buff * eny_stats.luck)) and eny_stats.crit_immune == 0:
        yr_stats.crit = 1
        yr_stats.crit_multi = 1.3 + (yr_stats.luck_buff * yr_stats.luck/10 *2) - (eny_stats.luck_buff * eny_stats.luck/10)
        if yr_stats.crit_multi < 1.1:
            yr_stats.crit_multi = 1.1
    else:
        yr_stats.crit = 0
        yr_stats.crit_multi = 1

#what all skills are based on
class SkillTemplate:
    name = ''
    id = 0
    stats = ''
    stats2 = ''
    check = ''
    cost = 0
    power = 0
    target = 0
    rage_add = 0
    
    type_phyical = 0
    type_hand  = 0
    type_cut   = 0
    type_swipe = 0
    type_poke  = 0
    type_slam  = 0
    type_whack = 0
    type_projectile = 0
    
    type_magic    = 0
    type_spector  = 0
    type_fire     = 0
    type_electric = 0
    type_ice      = 0
    type_plant    = 0
    type_antiplant = 0
    type_shadow   = 0
    type_illusion = 0
    type_holy     = 0
    type_hydro    = 0
    type_food     = 0


class Skill_BasicAttack(SkillTemplate):
    name = 'Basic Attack'
    id = 1
    stats = ''
    check = ''
    cost = 0
    power = 15
    target = 2
    rage_add = 1
    
    type_phyical = 1
    
def basic_attack(yr_stats, eny_stats, skill_stats):
    dmg = 0
    if yr_stats.health_type != 3 and eny_stats.health_type != 3:
        #crit calc
        crit_calc(yr_stats, eny_stats)
    
        if eny_stats.defence >= 1:
            dmg = int(((yr_stats.attack * (skill_stats.power + yr_stats.charge*2) + (yr_stats.rage*1)) * yr_stats.attack_ef * yr_stats.attack_buff) / (eny_stats.defence * eny_stats.defence_ef * eny_stats.defending * eny_stats.defence_buff) * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,0))
        elif eny_stats.defence == 0:
            dmg = int(((yr_stats.attack * (skill_stats.power + yr_stats.charge*2) + (yr_stats.rage*1)) * yr_stats.attack_ef * yr_stats.attack_buff) * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,0) / eny_stats.defence_ef * eny_stats.defence_buff)
        else:
            dmg = int(((yr_stats.attack * (skill_stats.power + yr_stats.charge*2) + (yr_stats.rage*1)) * yr_stats.attack_ef * yr_stats.attack_buff) * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,0) * abs(int(eny_stats.defence)) / eny_stats.defence_ef * eny_stats.defence_buff)
    
    if resistance_calc(yr_stats,eny_stats,skill_stats,0) <= 0:
        return dmg
    elif dmg <= 3 and yr_stats.crit == 1 and (yr_stats.charge >= yr_stats.max_charge and yr_stats.charge != 0):
        return 3
    elif dmg <= 2 and ((yr_stats.charge >= yr_stats.max_charge and yr_stats.charge != 0) or yr_stats.crit == 1):
        return 2
    elif dmg < 1:
        return 1
    else:
        return dmg

def magic_dmg_calc(yr_stats, eny_stats, skill_stats):
    dmg = 0
    if yr_stats.health_type != 3 and eny_stats.health_type != 3:
        #crit calc
        crit_calc(yr_stats, eny_stats)
        if eny_stats.spirit_defence >= 1:
            dmg = int(((yr_stats.magic * (skill_stats.power + yr_stats.charge*2) + (yr_stats.rage*1)) * yr_stats.magic_ef) * yr_stats.magic_buff *1.3 / (eny_stats.spirit_defence * eny_stats.spirit_defence_ef * eny_stats.defending * eny_stats.spirit_defence_buff) * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1))
        elif eny_stats.spirit_defence == 0:
            dmg = int(((yr_stats.magic * (skill_stats.power + yr_stats.charge*2) + (yr_stats.rage*1)) * yr_stats.magic_ef) * yr_stats.magic_buff *1.3 * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1) / eny_stats.spirit_defence_ef * eny_stats.spirit_defence_buff)
        else:
            dmg = int(((yr_stats.magic * (skill_stats.power + yr_stats.charge*2) + (yr_stats.rage*1)) * yr_stats.magic_ef) * yr_stats.magic_buff *1.3 * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1) * abs(int(eny_stats.spirit_defence)) / eny_stats.spirit_defence_ef * eny_stats.spirit_defence_buff)
    
    if resistance_calc(yr_stats,eny_stats,skill_stats,0) <= 0:
        return dmg
    elif dmg <= 4 and yr_stats.crit == 1 and (yr_stats.charge >= yr_stats.max_charge and yr_stats.charge != 0):
        return 4
    elif dmg <= 3 and ((yr_stats.charge >= yr_stats.max_charge and yr_stats.charge != 0) or yr_stats.crit == 1):
        return 3
    elif dmg < 2:
        return 2
    else:
        return dmg

#--LK-skills---------------------------------
class Skill_LKCheck(SkillTemplate):
    name = 'Check'
    id = 101
    stats = ''
    check = 'Check an enemy for info.'
    cost = 0
    power = 0
    target = 2
    rage_add = 0
    
def lkcheck(yr_stats, stats):

    if stats.checked <= 0:
        check = stats.check1
    else:
        check = stats.check2
    stats.checked += 1
    print(f'? {stats.name}: \n? {stats.attack}atk  {stats.magic}mag  {stats.luck}luk \n? {stats.defence}def  {stats.spirit_defence}sdf  {stats.speed}spd \n* {check}')

class Skill_LKHeal(SkillTemplate):
    name = 'Heal'
    id = 102
    stats = ''
    check = 'Basic healing.'
    cost = 4
    power = 3
    target = 3
    rage_add = -1
    
    type_magic = 1

def lkheal(yr_stats, eny_stats, skill_stats):
    heal = int(skill_stats.power * yr_stats.magic + 10 + (yr_stats.rage/5))
    if heal <= 0:
        return 1
    else:
        return heal

#--Taco-skils--------------------------------

class Skill_TacoMultiSwipe(SkillTemplate):
    name = 'Multi-Swipe'
    id = 201
    stats = ''
    check = 'Attack twice.'
    cost = 4
    power = 14
    target = 4
    rage_add = 1

    type_phyical = 1
    
#see basic attack

class Skill_TacoDistract(SkillTemplate):
    name = 'Distract'
    id = 202
    stats = ''
    check = 'Grabs all foes attention.'
    cost = 3
    power = 0
    target = 1
    rage_add = 1

class Skill_TacoCheer(SkillTemplate):
    name = 'Cheer'
    id = 203
    stats = ''
    check = 'Restore 6sp to a friend.'
    cost = 5
    power = 6
    target = 3
    rage_add = 0

#--green-skills----------------------------
    
class Skill_GreenHeal(SkillTemplate):
    name = 'Heal'
    id = 301
    stats = ''
    check = 'Restore a chunk of hp to a friend.'
    cost = 6
    power = 14
    target = 3
    rage_add = -1
    
    type_magic = 1
    type_holy = 1
    
def greenheal(yr_stats, eny_stats, skill_stats):
    heal = int(skill_stats.power * (1 + yr_stats.temp/100) + (yr_stats.magic*2) + (yr_stats.rage/5))
    
    if skill_stats.id == Skill_GreenCalm.id:
        heal += func.buff_removal(eny_stats, 1)
    if heal <= 0:
        return 1
    else:
        return heal

class Skill_GreenBurn(SkillTemplate):
    name = 'Burn'
    id = 302
    stats = ''
    check = "Deals Fire damage, lowers target's defenses."
    cost = 6
    power = 15
    rage_add = 2
    
    type_magic = 1
    type_fire = 1
    target = 2
    
def green_burn_calc(yr_stats, eny_stats, skill_stats):
    dmg = 0
    if yr_stats.health_type != 3 and eny_stats.health_type != 3:
        #crit calc
        crit_calc(yr_stats, eny_stats)
        if eny_stats.spirit_defence >= 1:
            dmg = int(((yr_stats.magic * (skill_stats.power) + (yr_stats.rage*1)) * yr_stats.magic_ef) * yr_stats.magic_buff *1.4 / (eny_stats.spirit_defence * eny_stats.spirit_defence_ef * eny_stats.defending * eny_stats.spirit_defence_buff) * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1) * (0.8 + yr_stats.temp/100))
        elif eny_stats.spirit_defence == 0:
            dmg = int(((yr_stats.magic * (skill_stats.power) + (yr_stats.rage*1)) * yr_stats.magic_ef) * yr_stats.magic_buff *1.4 * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1) / eny_stats.spirit_defence_ef * (0.8 + yr_stats.temp/100) * eny_stats.spirit_defence_buff)
        else:
            dmg = int(((yr_stats.magic * (skill_stats.power) + (yr_stats.rage*1)) * yr_stats.magic_ef) * yr_stats.magic_buff *1.4 * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1) * abs(int(eny_stats.spirit_defence)) / eny_stats.spirit_defence_ef * (0.8 + yr_stats.temp/100) * eny_stats.spirit_defence_buff)
    
    temp_min = 0
    for i in range(int(yr_stats.temp/60)):
        temp_min += 1
    
    if resistance_calc(yr_stats,eny_stats,skill_stats,0) <= 0:
        return dmg
    elif dmg <= 3 + temp_min and  yr_stats.crit == 1:
        return 3 + temp_min
    elif dmg < 2 + temp_min:
        return 2 + temp_min
    else:
        return dmg

def green_burn_debuff(yr_stats, eny_stats, skill_stats):
    if eny_stats.debuff_immune == 0:
        if eny_stats.burn_debuff_num < max_burn_amount:
            func.buff_calc(eny_stats, 'def', debuff_burn)
            func.buff_calc(eny_stats, 'spdef', debuff_burn)
            eny_stats.burn_debuff_num += 1
            hold = yr_stats.to_party
            yr_stats.to_party = 1
            mes.battle_messages(yr_stats, eny_stats)
            yr_stats.to_party = hold

class Skill_GreenCalm(SkillTemplate):
    name = 'Calm'
    id = 303
    stats = ''
    check = 'Restores some hp and sp to a friend, removes effects.'
    cost = 3
    power = 1
    target = 3
    rage_add = -2
    
    type_magic = 1
    type_holy = 1
    
def greencalmsp(yr_stats, eny_stats, skill_stats):
    sp = int(yr_stats.magic / 2)
    if sp < 0:
        return 0
    else:
        return sp

#--storm-skills---------------------------------

class Skill_StormShock(SkillTemplate):
    name = 'Shock'
    id = 401
    stats = ''
    check = "Deals Electric damage, adds 1 to charge."
    cost = 5
    power = 15
    target = 2
    rage_add = 2
    
    type_magic = 1
    type_electric = 1

class Skill_StormCalmDown(SkillTemplate):
    name = 'Calmdown'
    id = 402
    stats = ''
    check = "Restores self's hp and sp based on charge, removes effects."
    cost = 0
    power = 9
    target = 1
    rage_add = -2

def stormcalmdownhp(yr_stats, eny_stats, skill_stats):
    heal = int(skill_stats.power + skill_stats.power * yr_stats.charge + func.buff_removal(yr_stats, 1))
    if heal < 0:
        return 0
    else:
        return heal
    
def stormcalmdownsp(yr_stats, eny_stats, skill_stats):
    sp = int(yr_stats.charge + 3)
    if sp < 0:
        return 0
    else:
        return sp
    
class Skill_StormCharge(SkillTemplate):
    name = 'Charge'
    id = 403
    stats = ''
    check = "Maxes out charge."
    cost = 4
    power = 3
    target = 1
    rage_add = 0
    
    type_electric = 1

#--hamy-skills--------------------------------------------------
class Skill_HamySpray(SkillTemplate):
    name = 'PBS Spray'
    id = 501
    stats = ''
    check = "Lowers all enemy defence."
    cost = 1
    power = 1
    target = 1
    rage_add = 1
    
    type_phyical = 1
    type_projectile = 1
    type_antiplant = 1

def ham_attack_calc(yr_stats, eny_stats, skill_stats):
    dmg = 0
    if yr_stats.health_type != 3 and eny_stats.health_type != 3:
        #crit calc
        crit_calc(yr_stats, eny_stats)
    
        if eny_stats.defence >= 1:
            dmg = int((((skill_stats.power)) * yr_stats.attack_ef ) / (eny_stats.defence * eny_stats.defence_ef * eny_stats.defending * eny_stats.defence_buff) * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1))
        elif eny_stats.defence == 0:
            dmg = int((((skill_stats.power)) * yr_stats.attack_ef) * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1) / eny_stats.defence_ef * eny_stats.defence_buff)
        else:
            dmg = int((((skill_stats.power)) * yr_stats.attack_ef) * yr_stats.crit_multi * resistance_calc(yr_stats,eny_stats,skill_stats,1) * abs(int(eny_stats.defence)) / eny_stats.defence_ef * eny_stats.defence_buff)
    
    if resistance_calc(yr_stats,eny_stats,skill_stats,0) <= 0:
        return dmg
    elif dmg <= 3 and yr_stats.crit == 1 and (yr_stats.charge >= yr_stats.max_charge and yr_stats.charge != 0):
        return 3
    elif dmg <= 2 and ((yr_stats.charge >= yr_stats.max_charge and yr_stats.charge != 0) or yr_stats.crit == 1):
        return 2
    elif dmg < 1:
        return 1
    else:
        return dmg
    

class Skill_HamyGun(SkillTemplate):
    name = 'Ham Gun'
    id = 502
    stats = ''
    check = "Shoot an enemy."
    cost = 2
    power = 100
    target = 2
    rage_add = 2
    
    type_phyical = 1
    type_projectile = 1
    type_antiplant = 1
    
class Skill_HamyZap(SkillTemplate):
    name = 'Zap'
    id = 503
    stats = ''
    check = "Restore an allie's sp at cost of their hp."
    cost = 4
    power = 8
    target = 3
    rage_add = 0
    
    type_electric = 1
    
#--creation-skills----------------------------------------------
class Skill_CreationCook(SkillTemplate):
    name = 'Cook'
    id = 601
    stats = ''
    check = "Heal a friend with the power of food."
    cost = 4
    power = 30
    target = 3
    rage_add = -1
    
    type_food = 1
    
def creation_cook_heal(yr_stats, eny_stats, skill_stats):
    heal = int(skill_stats.power)
    return heal
    
class Skill_CreationStare(SkillTemplate):
    name = 'Stare'
    id = 602
    stats = ''
    check = "Lowers a target's stats."
    cost = 3
    power = 1
    target = 2
    rage_add = 0
    
    type_spector = 1
    
class Skill_CreationSleepMode(SkillTemplate):
    name = 'Sleep Mode'
    id = 603
    stats = ''
    check = "Restore power while asleep, can't act until awoken."
    cost = 0
    power = 30
    target = 1
    rage_add = 0
    
#--willow-skills------------------------------------------------
class Skill_WillowIcyWind(SkillTemplate):
    name = 'Icy Wind'
    id = 701
    stats = ''
    check = "Deals big ice damage."
    cost = 6
    power = 16
    target = 2
    rage_add = 3
    
    type_magic = 1
    type_ice = 1
    
class Skill_WillowSnowyBreeze(SkillTemplate):
    name = 'Snowy Breeze'
    id = 702
    stats = ''
    check = "Deals ice damage to all enemys."
    cost = 4
    power = 6
    target = 1
    rage_add = 2
    
    type_magic = 1
    type_ice = 1
    
class Skill_WillowFreeze(SkillTemplate):
    name = 'Freeze'
    id = 702
    stats = ''
    check = "Freeze an enemy."
    cost = 5
    power = 0
    target = 2
    rage_add = 0
    
    type_magic = 1
    type_ice = 1

#--other-skills-------------------------------------------------
    
class Skill_RedHands(SkillTemplate):
    name = 'RED HANDS'
    id = 9901
    stats = 'Deals big damage 4 times.'
    check = "ERASE the enemy."
    cost = 75
    power = 30
    target = 2
    rage_add = 1
    
class Skill_SnowGrave(SkillTemplate):
    name = 'SNOWGRAVE'
    id = 9902
    stats = 'Fatal.'
    check = "Fatal."
    cost = 200
    power = 400
    target = 2
    rage_add = 0
    
    type_magic = 1
    type_ice = 1
    
    #unfin
class Skill_Explosion(SkillTemplate):
    name = 'Explosion'
    id = 9903
    stats = 'why would you even do this.'
    check = "deal big damage to EVERYONE."
    cost = 0
    power = 200
    target = 1
    rage_add = 10
