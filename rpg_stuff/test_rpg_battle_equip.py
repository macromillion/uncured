#has all skills stats
import test_rpg_battle_skill_list as lst
"""
this file contains all weapon stats
"""
"""
--weapons----------------------------------------------------------------------------------------------

Lost Kid (1xx)
101 - Worn Sickle

Taco (2xx)
201 - Stick

Green (3xx)
(none)

Storm (4xx)
401 - Sweaty Bag

hamy (5xx)

creation (6xx)

willow (7xx)

fred (99xx)
"""

class WeaponTemplate:
    name = ''
    id = 0
    stats = ''
    check = ''
    
    #-adds-to-stats-------------
    attack = 0
    magic  = 0
    
    defence    = 0
    spirit_defence = 0
    
    cur_hp = 0
    max_hp = 0
    cur_sp = 0
    max_sp = 0
    
    luck  = 0
    speed = 0
    
    #-adds-typing-to-phyical-attacks-----------
    type_hand  = 0
    type_cut   = 0
    type_swipe = 0
    type_poke  = 0
    type_slam  = 0
    type_whack = 0
    type_projectile = 0
    
    #-unadded------
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
    
    #-who-can-equips-----------
    lk_equip    = 0
    taco_equip  = 0
    green_equip = 0
    storm_equip = 0
    
    hamy_equip     = 0
    creation_equip = 0
    willow_equip   = 0
    fred_equip     = 0

#--generic-equips------------------------------------------------
class Weapon_NoWeapon(WeaponTemplate):
    name = 'None'
    id = 0
    stats = ''
    check = ''
    
    type_hand  = 1
    lk_equip    = 1
    taco_equip  = 1
    storm_equip = 1
    
    hamy_equip     = 1
    creation_equip = 1
    fred_equip     = 1
    
class Weapon_NoWeaponGreen(WeaponTemplate):
    name = 'None'
    id = 0
    stats = ''
    check = ''
    
    type_poke = 1
    green_equip = 1
    
class Weapon_NoWeaponWillow(WeaponTemplate):
    name = 'None'
    id = 0
    stats = ''
    check = ''
    
    type_whack = 1
    willow_equip = 1
    
class Weapon_ToyKnife(WeaponTemplate):
    name = 'Abandoned Knife'
    id = 1
    stats = '+3atk'
    check = 'Back with a vengeance. (Not really)'
    
    attack = 3
    type_cut = 1
    lk_equip  = 1
    fred_equip = 1

class Weapon_AlterKnife(WeaponTemplate):
    name = 'ALTER Knife'
    id = 98
    stats = '+99mag'
    check = 'Here we were.'
    
    magic = 99
    type_cut = 1
    fred_equip = 1

class Weapon_RealKnife(WeaponTemplate):
    name = 'Real Knife'
    id = 99
    stats = '+99atk'
    check = 'Here we are!'
    
    attack = 99
    type_cut = 1
    fred_equip = 1

#--lost-kid-equips------------------------------------------------
class Weapon_lkWornSickle(WeaponTemplate):
    name = 'Worn Sickle'
    id = 101
    stats = ''
    check = 'A harvesting blade. Too dull to do any real damage.'
    
    attack = 0
    
    type_cut  = 1
    lk_equip  = 1
#--taco-equips------------------------------------------------
class Weapon_TacoStick(WeaponTemplate):
    name = 'Stick'
    id = 201
    stats = '+1atk'
    check = 'Fresh off the tree. Seen some use.'
    
    attack = 1
    
    type_swipe  = 1
    taco_equip  = 1
    
#--green-equips------------------------------------------------
    
    #has none lol
    
#--storm-equips------------------------------------------------
class Weapon_StormSweatyBag(WeaponTemplate):
    name = 'Sweaty Bag'
    id = 401
    stats = '+2atk'
    check = "Someone's gym bag. Stinky."
    
    attack = 2
    
    type_slam  = 1
    storm_equip  = 1
    
#--hamy-equips-------------------------------------------------
class Weapon_HamyHamer(WeaponTemplate):
    name = 'Hamyer'
    id = 501
    stats = '+2atk'
    check = "A sleged hammer with HAMY written on it."
    
    attack = 2
    
    type_whack  = 1
    hamy_equip  = 1
    
#--creation-equips------------------------------------------------
class Weapon_CreationPan(WeaponTemplate):
    name = 'Pan'
    id = 601
    stats = '+2atk, +1luk'
    check = 'Pan but with an "i".'
    
    attack = 2
    luck = 1
    
    type_slam  = 1
    creation_equip  = 1

#--willow-equips--------------------------------------------------
    
    #none lol
    
#--fred-equips----------------------------------------------------
class Weapon_FredKnife(WeaponTemplate):
    name = 'Knife'
    id = 9901
    stats = '+99999999atk/mag'
    check = "Because all indie rpgs need one."
    
    attack = 99999999
    magic  = 99999999
    
    type_cut  = 1
    fred_equip  = 1

"""
#--ARMORS--------------------------------------------------------------------


"""
class ArmorTemplate:
    name = ''
    id = 0
    stats = ''
    check = ''
    
    #-adds-stats-----------
    attack = 0
    magic  = 0
    
    defence    = 0
    spirit_defence = 0
    
    cur_hp = 0
    max_hp = 0
    cur_sp = 0
    max_sp = 0
    
    luck  = 0
    speed = 0

    #-adds-resists-----------   
    type_phyical = 0
    type_hand    = 0
    type_cut     = 0
    type_swipe   = 0
    type_poke    = 0
    type_slam    = 0
    type_whack   = 0
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
    
    #-who-can-equip------------
    lk_equip    = 1
    taco_equip  = 1
    green_equip = 1
    storm_equip = 1
    
    hamy_equip     = 1
    creation_equip = 1
    willow_equip   = 1
    fred_equip     = 1

class Armor_NoArmor(ArmorTemplate):
    name = 'None'
    id = 0
    stats = ''
    check = ''

class Armor_EveryArmor(ArmorTemplate):
    name = 'EveryArmor'
    id = 1
    stats = 'Increases ALL stats by 1'
    check = 'Contains a bit of everything...'
    
    attack = 1
    magic  = 1
    
    defence    = 1
    spirit_defence = 1
    
    cur_hp = 1
    max_hp = 1
    cur_sp = 1
    max_sp = 1
    
    luck  = 1
    speed = 1
    
    type_phyical = 0.1
    type_hand    = 0.1
    type_cut     = 0.1
    type_swipe   = 0.1
    type_poke    = 0.1
    type_slam    = 0.1
    type_whack   = 0.1
    type_projectile = 0.1
    
    type_magic    = 0.1
    type_spector  = 0.1
    type_fire     = 0.1
    type_electric = 0.1
    type_ice      = 0.1
    type_plant    = 0.1
    type_antiplant = 0.1
    type_shadow   = 0.1
    type_illusion = 0.1
    type_holy     = 0.1
    type_hydro    = 0.1
    type_food     = 0.1
    
    lk_equip    = 0
    taco_equip  = 0
    green_equip = 0
    storm_equip = 0
    
    hamy_equip     = 0
    creation_equip = 0
    willow_equip   = 0
    fred_equip     = 0

class Armor_Ribbon(ArmorTemplate):
    name = 'Ribbon'
    id = 2
    stats = '+1def'
    check = '''"If you're cuter, monsters won't hit you as hard..." -undertale.fandom.com/wiki/Faded_Ribbon'''
    
    defence    = 1
    spirit_defence = 0

class Armor_GodArmor(ArmorTemplate):
    name = 'God Armor'
    id = 3
    stats = 'Gain absurd def and spdef'
    check = 'simply become god.'
    
    defence    = 9999999999999999
    spirit_defence = 99999999999999999

class Armor_AntiGodArmor(ArmorTemplate):
    name = 'Anti-God Armor'
    id = 4
    stats = 'Gain NEO defence'
    check = 'simply become atheist.'
    
    defence    = -9999999999999999
    spirit_defence = -99999999999999999

"""
#--CHARMS--------------------------------------------------------------------

idea - elemetal hats - changes storms skills to that type
    - fire
    - ice
    - plant

"""
class CharmTemplate:
    name = ''
    id = 0
    stats = ''
    check = ''
    
    #-adds-to-stats--------
    attack = 0
    magic  = 0
    
    defence    = 0
    spirit_defence = 0
    
    cur_hp = 0
    max_hp = 0
    cur_sp = 0
    max_sp = 0
    
    
    luck  = 0
    speed = 0
    
    #-adds-resistences-----------
    type_phyical = 0
    type_hand    = 0
    type_cut     = 0
    type_swipe   = 0
    type_poke    = 0
    type_slam    = 0
    type_whack   = 0
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
    
    #-who-can-equip-----------
    lk_equip    = 1
    taco_equip  = 1
    green_equip = 1
    storm_equip = 1
    
    hamy_equip     = 1
    creation_equip = 1
    willow_equip   = 1
    fred_equip     = 1

class Charm_NoCharm(CharmTemplate):
    name = 'None'
    id = 0
    stats = ''
    check = ''

class Charm_TrueDreamBadge(CharmTemplate):
    name = 'TRUE Dream Badge'
    id = 2
    stats = 'gain dream-like abilitys'
    check = 'Cheater.'
    
    luck  = 9999999999999999
    speed = 9999999999999999
    
    lk_equip    = 1
    taco_equip  = 1
    green_equip = 1
    storm_equip = 1

class Charm_PotatoBadge(CharmTemplate):
    name = 'potato badge'
    id = 3
    stats = 'turns the wearer into a potato'
    check = 'dont.'
    
    attack = -9999999
    magic  = -9999999
    
    defence    = -999999
    spirit_defence = -999999
    
    cur_hp = -9999999
    max_hp = -9999999
    cur_sp = -9999999
    max_sp = -9999999
    
    luck  = -9999999
    speed = -9999999
    
    type_phyical = -9999999
    type_magic    = -9999999
    type_antiplant = -9999999
    
class Charm_PlotArmorBadge(CharmTemplate):
    name = 'Plot Armor Badge'
    id = 4
    stats = 'Gain Anime powers.'
    check = '''"You won't die..."'''
    #sets the refuse stat to big number

class Charm_FireOrb(CharmTemplate):
    name = 'Fire Orb'
    id = 5
    stats = 'Increases fire damage at the cost of healing (Green only)'
    check = 'Said to corrupt all to those who touch it.'
    
    magic  = 3
    type_fire = 1
    
    lk_equip    = 0
    taco_equip  = 0
    green_equip = 1
    storm_equip = 0
    
    hamy_equip     = 0
    creation_equip = 0
    willow_equip   = 0
    fred_equip     = 0

#--badge-conditions---------------------------------------
def charm_conditions(stats):
    if stats.exists == 1:
        if stats.charm == Charm_PotatoBadge.id:
            stats.name = 'potato'
            stats.check1 = 'a useless potato.'
            stats.check2 = 'still useless.'
        elif stats.charm == Charm_PlotArmorBadge.id:
            stats.refuse += 9999999999999999999999
        elif stats.charm == Charm_FireOrb.id:
            stats.temp *= 2
            lst.Skill_GreenHeal.power = 1
            lst.debuff_burn = -.1
            lst.max_burn_amount = 9999




