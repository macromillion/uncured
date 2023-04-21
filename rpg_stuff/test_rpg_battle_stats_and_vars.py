"""
This file contains most variables
It has party stats & enemy stats
also equips are added here
also also name change stuff happens here
"""
#basicly the SAVE file
import test_rpg_config as con
#translates numbers to a class
import test_rpg_config_translator as tran
#equip suff
import test_rpg_battle_equip as eqp

def stats_define():
    global StatTemplate
    #basic template for all chars
    class StatTemplate:

        #your_name
        name = ''
        #used to make things look nicer
        display_name = name
        #id
        id = 0
        #if exists
        exists = 0
        #used for message pronouns
        gender = 0
        #gender:
        #0 - they
        #1 - he
        #2 - she
        #3 - it
        #type of hp
        health_type = 1
        #hp type:
        #1 - hp / sp
        #2 - hp
        #3 - sp
        #4 - pwr
        
        #--equips-----------
        weapon = 0
        armor  = 0
        charm  = 0
        
        weapon_name = ''
        armor_name  = ''
        charm_name  = ''
        
        #the type the weapon is (used for resist)
        weapon_type_hand  = 0
        weapon_type_cut   = 0
        weapon_type_swipe = 0
        weapon_type_poke  = 0
        weapon_type_slam  = 0
        weapon_type_whack = 0
        weapon_type_projectile = 0
        
        #--battle-vars-----------
        alive      = 0
        party_slot = 0
        enemy_slot = 0
        action     = 0
        target     = 0
        target2    = 0
        #if skill is directed at party set 1
        to_party   = 0
        targeted   = 0
        defending  = 1
        dmg        = 0
        #if criting
        crit       = 0
        #how much more dmg a crit will do
        crit_multi = 1
        miss       = 1
        damaged    = 0
        rage       = 0
        #rage gain multipyer
        rage_multi = 0 # was 1
        max_rage   = 0 # was 50
        
        #char gimics
        charge     = 0
        max_charge = 0
        #how many times they can live at 1hp
        refuse     = 0
        temp       = 0
        
        #-buffs/debuffs--------------
        attack_buff = 1
        magic_buff = 1
        defence_buff = 1
        spirit_defence_buff = 1
        luck_buff = 1
        speed_buff = 1
        
        #used to count times debuffed by green burn
        burn_debuff_num = 0
        #turns left of ham spray
        spray_debuff_turn = 0
        
        debuff_immune = 0
        crit_immune   = 0
        
        #-stats---------------
        attack = 0
        magic  = 0
        
        #used for plot shenanigans
        attack_ef = 1
        magic_ef  = 1

        defence = 0
        #(magic defence)
        spirit_defence = 0
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 0
        speed = 0

        cur_hp = 0
        max_hp = 0
        cur_sp = 0
        max_sp = 0
        
        #other hp type
        cur_pwr = 0
        max_pwr = 0
        
        skill1 = 0
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0
        
        #if was checked
        checked = 0
        check1 = ''
        check2 = check1
        
        #--resists-----------------
        resist_phyical = 1
        resist_hand    = 1
        resist_cut     = 1
        resist_swipe   = 1
        resist_poke    = 1
        resist_slam    = 1
        resist_whack   = 1
        resist_projectile = 1
        
        resist_magic    = 1
        resist_spector  = 1
        resist_fire     = 1
        resist_electric = 1
        resist_ice      = 1
        resist_plant    = 1
        resist_antiplant = 1
        resist_shadow   = 1
        resist_illusion = 1
        resist_holy     = 1
        resist_hydro    = 1
        resist_food     = 1
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

        def __repr__(self):
            return f'? {self.name} {self.cur_hp}/{self.max_hp}hp {self.cur_sp}/{self.max_sp}sp: \n? {self.attack}atk {self.magic}mag {self.luck}luk \n? {self.defence}def {self.spirit_defence}spdef {self.speed}spd \n* {self.check1}'

    global LostKidStats
    class LostKidStats(StatTemplate):
        name = con.player_name
        id = 1
        exists = 1
        gender = 0
        alive = 1
        refuse = 1
        crit_immune = 1

        weapon = con.lk_equip_weapon
        armor  = con.lk_equip_armor
        charm  = con.lk_equip_charm

        attack = 5
        magic  = 5
        
        attack_ef = 1
        magic_ef  = 1

        defence = 5
        spirit_defence = 5
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 5
        speed = 5

        cur_hp = con.lk_cur_hp
        max_hp = 40
        cur_sp = con.lk_cur_sp
        max_sp = 10
        
        skill1 = 101
        skill2 = 102
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = 'what'
        
        resist_phyical = 0.9
        resist_magic   = 0.9
        
        resist_lost_kid = 1
        resist_taco     = 0.6
        resist_green    = 0.1
        resist_storm    = 0.7
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global TacoStats
    class TacoStats(StatTemplate):
        name = 'Taco'
        id = 2
        exists = 1
        gender = 1
        alive = 1
        
        weapon = con.taco_equip_weapon
        armor  = con.taco_equip_armor
        charm  = con.taco_equip_charm

        attack = 3
        magic  = 1
        
        attack_ef = 1
        magic_ef  = 1

        defence = 6
        spirit_defence = 4
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 3
        speed = 6

        cur_hp = con.taco_cur_hp
        max_hp = 55
        cur_sp = con.taco_cur_sp
        max_sp = 25
        
        skill1 = 201
        skill2 = 202
        skill3 = 203
        skill4 = 0
        skill5 = 0

        check1 = 'A cat-raccon thing. His real name is actually "Stampy".'
        
        resist_spector  = 1.2
        resist_illusion = 0.7
        
        resist_lost_kid = 0.5
        resist_taco     = 1
        resist_green    = 0.01
        resist_storm    = 0.9
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global GreenStats
    class GreenStats(StatTemplate):
        name = 'Green'
        id = 3
        exists = 1
        gender = 1
        alive = 1
        temp = 40
        rage_multi = 0 # was 1.5
        
        weapon = con.green_equip_weapon
        armor  = con.green_equip_armor
        charm  = con.green_equip_charm

        attack = 3
        magic  = 6
        
        attack_ef = 1
        magic_ef  = 1

        defence = 5
        spirit_defence = 6
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 6
        speed = 3

        cur_hp = con.green_cur_hp
        max_hp = 50
        cur_sp = con.green_cur_sp
        max_sp = 20
        
        skill1 = 301
        skill2 = 302
        skill3 = 303
        skill4 = 0
        skill5 = 0

        check1 = '''A green dragon with a scarf. Is aware of how silly his name is.'''
        
        resist_fire     = 0.6
        resist_ice      = 1.4
        resist_holy     = 0.7
        
        resist_lost_kid = 0.5
        resist_taco     = 0.3
        resist_green    = 1
        resist_storm    = 0.3
        
        resist_hamy     = 1
        resist_creation = .9
        resist_willow   = 1
        resist_fred     = 1

    global StormStats
    class StormStats(StatTemplate):
        name = 'Storm'
        id = 4
        exists = 1
        gender = 2
        alive = 1
        refuse = 1
        max_charge = 3
        
        weapon = con.storm_equip_weapon
        armor  = con.storm_equip_armor
        charm  = con.storm_equip_charm

        attack = 4
        magic  = 7
        
        attack_ef = 1
        magic_ef  = 1

        defence = 4
        spirit_defence = 4
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 4
        speed = 4

        cur_hp = con.storm_cur_hp
        max_hp = 45
        cur_sp = con.storm_cur_sp
        max_sp = 15
        
        skill1 = 401
        skill2 = 402
        skill3 = 403
        skill4 = 0
        skill5 = 0

        check1 = 'A cloaked cat person. Shes still looking for someone.'
        
        resist_electric = 0.5
        resist_hydro    = 0.9
        
        resist_lost_kid = 0.5
        resist_taco     = 0.7
        resist_green    = 0.01
        resist_storm    = 1.2
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global HamyStats
    class HamyStats(StatTemplate):

        name = 'Hamy'
        display_name = name
        id = 5
        exists = 1
        gender = 0
        alive = 1
        
        weapon = con.hamy_equip_weapon
        armor  = con.hamy_equip_armor
        charm  = con.hamy_equip_charm

        attack = 3
        magic  = 0
        
        attack_ef = 1
        magic_ef  = 1

        defence = 4
        spirit_defence = 4
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 8
        speed = 4

        cur_hp = con.hamy_cur_hp
        max_hp = 40
        cur_sp = con.hamy_cur_sp
        max_sp = 5
        
        skill1 = 501
        skill2 = 502
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = 'An idiot-genius hamburger. Lives in BS.'
        
        resist_spector  = .1
        resist_fire     = .1
        resist_electric = 0
        resist_ice      = .1
        resist_plant    = .1
        resist_antiplant = .1
        resist_shadow   = .1
        resist_illusion = .1
        resist_holy     = .1
        resist_hydro    = .1
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1.1
        
        resist_hamy     = 1
        resist_creation = .9
        resist_willow   = .8
        resist_fred     = 1
        
    global CreationStats
    class CreationStats(StatTemplate):

        name = 'Creation'
        display_name = name
        id = 6
        exists = 1
        gender = 3
        alive = 1
        health_type = 4
        
        weapon = con.creation_equip_weapon
        armor  = con.creation_equip_armor
        charm  = con.creation_equip_charm

        attack = 6
        magic  = 0
        
        attack_ef = 1
        magic_ef  = 1

        defence = 6
        spirit_defence = 6
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 1
        speed = -1

        cur_hp = 0
        max_hp = 0
        cur_sp = 0
        max_sp = 0
        
        cur_pwr = con.creation_cur_pwr
        max_pwr = 100
        
        skill1 = 601
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = '''A giant robot. Hamy's loyal slave.'''
        
        resist_phyical = .9
        
        resist_electric = -1
        resist_hydro    = 1.1
        
        resist_lost_kid = 1
        resist_taco     = 1.1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = .01
        resist_creation = 1
        resist_willow   = .5
        resist_fred     = 1

    global WillowStats
    class WillowStats(StatTemplate):

        name = 'Willow'
        display_name = name
        id = 7
        exists = 1
        gender = 2
        alive = 1
        max_charge = 3
        
        weapon = con.willow_equip_weapon
        armor  = con.willow_equip_armor
        charm  = con.willow_equip_charm

        attack = 4
        magic  = 9
        
        attack_ef = 1
        magic_ef  = 1

        defence = 3
        spirit_defence = 3
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 1
        speed = 9

        cur_hp = con.willow_cur_hp
        max_hp = 50
        cur_sp = con.willow_cur_sp
        max_sp = 25
        
        skill1 = 701
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = '''A white dragon with slighty blue eyes. Green's sister.'''
        
        resist_fire     = 1.4
        resist_ice      = .1
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = .1
        resist_storm    = 1
        
        resist_hamy     = .7
        resist_creation = 1
        resist_willow   = .1
        resist_fred     = .5


    global SpaceManStats
    class SpaceManStats(StatTemplate):
        name = 'spacemanman'
        id = 68
        exists = 1
        gender = 0
        alive = 1
        crit_immune = 0

        weapon = 0
        armor  = 0
        charm  = 0

        attack = 5
        magic  = 5
        
        attack_ef = 1
        magic_ef  = 1

        defence = 5
        spirit_defence = 5
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 5
        speed = 5

        cur_hp = 60
        max_hp = 60
        cur_sp = 10
        max_sp = 10
        
        skill1 = 101
        skill2 = 601
        skill3 = 9902
        skill4 = 0
        skill5 = 0

        check1 = 'the spaceman man'
    
    global PoopGuyStats
    class PoopGuyStats(StatTemplate):

        name = 'Poop Guy'
        display_name = name
        id = 69
        exists = 1
        health_type = 2
        gender = 0
        alive = 1
        
        weapon = 0
        armor  = 0
        charm  = 0

        attack = 3
        magic  = 0
        
        attack_ef = 1
        magic_ef  = 1

        defence = 13
        spirit_defence = 4
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 5
        speed = 6

        cur_hp = 200
        max_hp = 200
        cur_sp = 0
        max_sp = 0
        
        skill1 = 0
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = 'Used in a different game. (ignore)'
        
        resist_phyical = 1
        resist_magic    = 1
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global FredStats
    class FredStats(StatTemplate):

        name = 'Fred'
        display_name = name
        id = 99
        exists = 1
        health_type = 2
        gender = 0
        alive = 1
        rage_multi = 0 #was 0
        debuff_immune = 1
        crit_immune = 1
        
        weapon = con.fred_equip_weapon
        armor  = con.fred_equip_armor
        charm  = con.fred_equip_charm

        attack = 99
        magic  = 99
        
        attack_ef = .005
        magic_ef  = .005

        defence = 99
        spirit_defence = 99
        
        defence_ef        = .1
        spirit_defence_ef = .1

        luck  = 99
        speed = 99

        cur_hp = con.fred_cur_hp
        max_hp = 99
        cur_sp = 0
        max_sp = 0
        
        skill1 = 0
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = 'Fred.'
        
        resist_phyical = 1
        resist_magic    = 1
        resist_antiplant = 0
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global ErrorStats
    class ErrorStats(StatTemplate):
        name = '[ERROR]'
        id = 100
        exists = 1
        health_type = 3
        gender = 69
        alive = 1
        rage_multi = 0 #was 2
        debuff_immune = 1
        crit_immune = 1

        attack = 'all the '
        magic  = "good amount of "
        
        attack_ef = 1
        magic_ef  = 1

        defence = 'useless '
        spirit_defence = 'more useless '
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 'very '
        speed = 13

        cur_hp = 0
        max_hp = 0
        cur_sp = con.error_cur_sp
        max_sp = 20
        
        skill1 = 0
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = "[What? Never seen an ERROR before?]"
        check2 = "[Whaddya lookin' for?]"
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 99

    global TestmanStats
    class TestmanStats(StatTemplate):
        name = 'Testman'
        id = 101
        exists = 1
        gender = 1
        alive = 1

        attack = 5
        magic  = 5
        
        attack_ef = 1
        magic_ef  = 1

        defence = 5
        spirit_defence = 5
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 5
        speed = 5

        cur_hp = 100
        max_hp = 100
        cur_sp = 20
        max_sp = 20
        
        skill1 = 0
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = 'A humble test enemy.'
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global TestDummyStats
    class TestDummyStats(StatTemplate):
        name = 'TestDummy'
        id = 102
        exists = 1
        gender = 0
        alive = 1

        attack = 0
        magic  = 0
        
        attack_ef = 1
        magic_ef  = 1

        defence = 5
        spirit_defence = 5
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 0
        speed = -14

        cur_hp = 999999999999999999999999999999999999999999999999999999
        max_hp = 999999999999999999999999999999999999999999999999999999
        cur_sp = 0
        max_sp = 0
        
        skill1 = 0
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = 'Capable of taking hits.'
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global JohnToiletStats
    class JohnToiletStats(StatTemplate):

        name = 'John Toilet'
        display_name = name
        id = 103
        exists = 1
        health_type = 2
        gender = 0
        alive = 1

        attack = 7
        magic  = 0
        
        attack_ef = 1
        magic_ef  = 1

        defence = 50
        spirit_defence = 10
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 2
        speed = 1

        cur_hp = 3000
        max_hp = 3000
        cur_sp = 0
        max_sp = 0
        
        skill1 = 0
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = "Walmart's janitor."
        
        resist_phyical = 1
        resist_magic    = 1
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global MoldsmalStats
    class MoldsmalStats(StatTemplate):

        name = 'Moldsmal'
        display_name = name
        id = 104
        exists = 1
        health_type = 2
        gender = 0
        alive = 1

        attack = 4
        magic  = 0
        
        attack_ef = 1
        magic_ef  = 1

        defence = 0
        spirit_defence = 0
        
        defence_ef        = 2
        spirit_defence_ef = 2

        luck  = 3
        speed = 0

        cur_hp = 50
        max_hp = 50
        cur_sp = 0
        max_sp = 0
        
        skill1 = 0
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = "Stereotypical: Curvaceously attractive, but no brains..."
        
        resist_phyical = 1
        resist_magic    = 1
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    global SomethingStats
    class SomethingStats(StatTemplate):

        name = 'SOMETHING'
        display_name = name
        id = 134
        exists = 1
        health_type = 0
        gender = 3
        alive = 1

        attack = 1
        magic  = 3
        
        attack_ef = 1
        magic_ef  = 1

        defence = 1
        spirit_defence = 3
        
        defence_ef        = 1
        spirit_defence_ef = 1

        luck  = 4
        speed = 4

        cur_hp = 134
        max_hp = 134
        cur_sp = 134
        max_sp = 134
        
        skill1 = 134
        skill2 = 0
        skill3 = 0
        skill4 = 0
        skill5 = 0

        check1 = "I'm sorry."
        check2 = f"{con.player_name}..."
        
        resist_phyical = 1
        resist_magic    = 1
        
        resist_lost_kid = 1
        resist_taco     = 1
        resist_green    = 1
        resist_storm    = 1
        
        resist_hamy     = 1
        resist_creation = 1
        resist_willow   = 1
        resist_fred     = 1

    #--party-------------------------------------------------------
    #pL = Party Leader
    #p1 = Party member 1
    #p2 = Party member 2
    #p3 = Party member 3

    #defines party
    global pLStats
    class pLStats(tran.party_conversion(con.party_leader)):
        party_slot = 1
        refuse = 1
        crit_immune = 1
    
    global p1Stats
    class p1Stats(tran.party_conversion(con.party_memb1)):
        party_slot = 2
    
    global p2Stats
    class p2Stats(tran.party_conversion(con.party_memb2)):
        party_slot = 3
    
    global p3Stats
    class p3Stats(tran.party_conversion(con.party_memb3)):
        party_slot = 4

    #--enemy-----------------------------------------------------
    #e1 = enemy 1
    #e2 = enemy 2
    #e3 = enemy 3
    #e4 = enemy 4

    #defines enemys
    global e1Stats
    class e1Stats(tran.party_conversion(con.enemy1)):
        enemy_slot = 1
        
    global e2Stats
    class e2Stats(tran.party_conversion(con.enemy2)):
        enemy_slot = 2
        
    global e3Stats
    class e3Stats(tran.party_conversion(con.enemy3)):
        enemy_slot = 3
        
    global e4Stats
    class e4Stats(tran.party_conversion(con.enemy4)):
        enemy_slot = 4
    #used as a fail safe
    global NullStats
    class NullStats(StatTemplate):
        enemy_slot = 0
    #--equips------------------------------------------------

    #-weapons----------
    #pL
    tran.weapon_equip_calc(pLStats, tran.weapon_conversion(pLStats))
    #p1
    tran.weapon_equip_calc(p1Stats, tran.weapon_conversion(p1Stats))
    #p2
    tran.weapon_equip_calc(p2Stats, tran.weapon_conversion(p2Stats))
    #p3
    tran.weapon_equip_calc(p3Stats, tran.weapon_conversion(p3Stats))

    #e1
    tran.weapon_equip_calc(e1Stats, tran.weapon_conversion(e1Stats))
    #e2
    tran.weapon_equip_calc(e2Stats, tran.weapon_conversion(e2Stats))
    #e3
    tran.weapon_equip_calc(e3Stats, tran.weapon_conversion(e3Stats))
    #e4
    tran.weapon_equip_calc(e4Stats, tran.weapon_conversion(e4Stats))

    #-armor-----------
    #pL
    tran.armor_equip_calc(pLStats, tran.armor_conversion(pLStats), 'armor')
    #p1
    tran.armor_equip_calc(p1Stats, tran.armor_conversion(p1Stats), 'armor')
    #p2
    tran.armor_equip_calc(p2Stats, tran.armor_conversion(p2Stats), 'armor')
    #p3
    tran.armor_equip_calc(p3Stats, tran.armor_conversion(p3Stats), 'armor')

    #e1
    tran.armor_equip_calc(e1Stats, tran.armor_conversion(e1Stats), 'armor')
    #e2
    tran.armor_equip_calc(e2Stats, tran.armor_conversion(e2Stats), 'armor')
    #e3
    tran.armor_equip_calc(e3Stats, tran.armor_conversion(e3Stats), 'armor')
    #e4
    tran.armor_equip_calc(e4Stats, tran.armor_conversion(e4Stats), 'armor')

    #-charm-----------
    #pL
    tran.armor_equip_calc(pLStats, tran.charm_conversion(pLStats), 'charm')
    #p1
    tran.armor_equip_calc(p1Stats, tran.charm_conversion(p1Stats), 'charm')
    #p2
    tran.armor_equip_calc(p2Stats, tran.charm_conversion(p2Stats), 'charm')
    #p3
    tran.armor_equip_calc(p3Stats, tran.charm_conversion(p3Stats), 'charm')

    #e1
    tran.armor_equip_calc(e1Stats, tran.charm_conversion(e1Stats), 'charm')
    #e2
    tran.armor_equip_calc(e2Stats, tran.charm_conversion(e2Stats), 'charm')
    #e3
    tran.armor_equip_calc(e3Stats, tran.charm_conversion(e3Stats), 'charm')
    #e4
    tran.armor_equip_calc(e4Stats, tran.charm_conversion(e4Stats), 'charm')

    #charm conditons
    eqp.charm_conditions(pLStats)
    eqp.charm_conditions(p1Stats)
    eqp.charm_conditions(p2Stats)
    eqp.charm_conditions(p3Stats)

    eqp.charm_conditions(e1Stats)
    eqp.charm_conditions(e2Stats)
    eqp.charm_conditions(e3Stats)
    eqp.charm_conditions(e4Stats)

    #--name a-b-c-d--system-----------------------------------------------------------
    #will add an 'A', 'B', 'C', or 'D' if enemy is same
    def name_enemy_letter_system(stats):
        num = 0
        if stats == e1Stats and e1Stats.exists == 1: 
            if stats.id == e2Stats.id and e2Stats.exists == 1:
                num += 1
            if stats.id == e3Stats.id and e3Stats.exists == 1:
                num += 1
            if stats.id == e4Stats.id and e4Stats.exists == 1:
                num += 1
                
        if stats == e2Stats and e2Stats.exists == 1: 
            if stats.id == e1Stats.id and e1Stats.exists == 1:
                num += 1
            if stats.id == e3Stats.id and e3Stats.exists == 1:
                num += 1
            if stats.id == e4Stats.id and e4Stats.exists == 1:
                num += 1
                
        if stats == e3Stats and e3Stats.exists == 1: 
            if stats.id == e1Stats.id and e1Stats.exists == 1:
                num += 1
            if stats.id == e2Stats.id and e2Stats.exists == 1:
                num += 1
            if stats.id == e4Stats.id and e4Stats.exists == 1:
                num += 1
                
        if stats == e4Stats and e4Stats.exists == 1: 
            if stats.id == e1Stats.id and e1Stats.exists == 1:
                num += 1
            if stats.id == e2Stats.id and e2Stats.exists == 1:
                num += 1
            if stats.id == e3Stats.id and e3Stats.exists == 1:
                num += 1
                
        if num > 0 and stats.exists == 1:
            if stats.enemy_slot == 1:
                stats.name += ' A'
            if stats.enemy_slot == 2:
                stats.name += ' B'
            if stats.enemy_slot == 3:
                stats.name += ' C'
            if stats.enemy_slot == 4:
                stats.name += ' D'

    #gives the letters
    name_enemy_letter_system(e4Stats)
    name_enemy_letter_system(e3Stats)
    name_enemy_letter_system(e2Stats)
    name_enemy_letter_system(e1Stats)

    #--party-display-name--------------------------------------------------------------
    #creates a space in names so it looks nicer
    #ex
    """
    BEFORE
    lost kid 40/40hp 10/10sp
    taco 55/55hp 25/25sp
    green 50/50sp 20/20sp

    AFTER
    lost kid 40/40hp 10/10sp
    taco     55/55hp 25/25sp
    green    50/50sp 20/20sp
    """
    #checks for longest name in party
    if len(pLStats.name) >= len(p1Stats.name) and len(pLStats.name) >= len(p2Stats.name) and len(pLStats.name) >= len(p3Stats.name):
        longest_party_name = len(pLStats.name)
        
    elif len(p1Stats.name) >= len(pLStats.name) and len(p1Stats.name) >= len(p2Stats.name) and len(p1Stats.name) >= len(p3Stats.name):
        longest_party_name = len(p1Stats.name)
        
    elif len(p2Stats.name) >= len(pLStats.name) and len(p2Stats.name) >= len(p1Stats.name) and len(p2Stats.name) >= len(p3Stats.name):
        longest_party_name = len(p2Stats.name)
        
    elif len(p3Stats.name) >= len(pLStats.name) and len(p3Stats.name) >= len(p1Stats.name) and len(p3Stats.name) >= len(p2Stats.name):
        longest_party_name = len(p3Stats.name)
        
    else:
        longest_party_name = 0

    #establishes party display names
    pLStats.display_name = pLStats.name
    p1Stats.display_name = p1Stats.name
    p2Stats.display_name = p2Stats.name
    p3Stats.display_name = p3Stats.name

    #adds a space for the difference in name length from longest name (party)
    for space in range(longest_party_name - len(pLStats.name)):
        pLStats.display_name += ' '
    for space in range(longest_party_name - len(p1Stats.name)):
        p1Stats.display_name += ' '
    for space in range(longest_party_name - len(p2Stats.name)):
        p2Stats.display_name += ' '
    for space in range(longest_party_name - len(p3Stats.name)):
        p3Stats.display_name += ' '
        
    #--enemy-display-name--------------------------------------------------------------
    #same for enemys

    #checks for longest name
    if len(e1Stats.name) >= len(e2Stats.name) and len(e1Stats.name) >= len(e3Stats.name) and len(e1Stats.name) >= len(e4Stats.name):
        longest_party_name = len(e1Stats.name)
        
    elif len(e2Stats.name) >= len(e1Stats.name) and len(e2Stats.name) >= len(e3Stats.name) and len(e2Stats.name) >= len(e4Stats.name):
        longest_party_name = len(e2Stats.name)
        
    elif len(e3Stats.name) >= len(e1Stats.name) and len(e3Stats.name) >= len(e2Stats.name) and len(e3Stats.name) >= len(e4Stats.name):
        longest_party_name = len(e3Stats.name)
        
    elif len(e4Stats.name) >= len(e1Stats.name) and len(e4Stats.name) >= len(e2Stats.name) and len(e4Stats.name) >= len(e3Stats.name):
        longest_party_name = len(e4Stats.name)
        
    else:
        longest_party_name = 0

    #establishes enemy display names
    e1Stats.display_name = e1Stats.name
    e2Stats.display_name = e2Stats.name
    e3Stats.display_name = e3Stats.name
    e4Stats.display_name = e4Stats.name

    #adds a space for the difference in name length from longest name (enemy)
    for space in range(longest_party_name - len(e1Stats.name)):
        e1Stats.display_name += ' '
    for space in range(longest_party_name - len(e2Stats.name)):
        e2Stats.display_name += ' '
    for space in range(longest_party_name - len(e3Stats.name)):
        e3Stats.display_name += ' '
    for space in range(longest_party_name - len(e4Stats.name)):
        e4Stats.display_name += ' '












