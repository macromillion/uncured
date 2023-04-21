"""
this file contains functions that translate number ids into actual stats
"""
import test_rpg_battle_stats_and_vars as var
import test_rpg_config as con
import test_rpg_battle_equip as eqp
import test_rpg_battle_skill_list as lst

#party/enemy conversion
def party_conversion(member):
    if member == var.LostKidStats.id:
        return var.LostKidStats
    elif member == var.TacoStats.id:
        return var.TacoStats
    elif member == var.GreenStats.id:
        return var.GreenStats
    elif member == var.StormStats.id:
        return var.StormStats
    elif member == var.HamyStats.id:
        return var.HamyStats
    elif member == var.CreationStats.id:
        return var.CreationStats
    elif member == var.WillowStats.id:
        return var.WillowStats
    elif member == var.SpaceManStats.id:
        return var.SpaceManStats
    elif member == var.PoopGuyStats.id:
        return var.PoopGuyStats
    elif member == var.FredStats.id:
        return var.FredStats
    elif member == var.ErrorStats.id:  
        return var.ErrorStats
    
    elif member == var.TestmanStats.id:
        return var.TestmanStats
    elif member == var.TestDummyStats.id:
        return var.TestDummyStats
    elif member == var.JohnToiletStats.id:
        return var.JohnToiletStats
    elif member == var.MoldsmalStats.id:
        return var.MoldsmalStats
    elif member == var.SomethingStats.id:
        return var.SomethingStats
    else:
        return var.StatTemplate
    """
    elif member == var..id:
        return var.
    """

#skill convert
def skill_conversion(skill):
    if skill == lst.Skill_BasicAttack.id:
        return lst.Skill_BasicAttack
    
    #lk skills
    elif skill == lst.Skill_LKCheck.id:
        return lst.Skill_LKCheck
    elif skill == lst.Skill_LKHeal.id:
        return lst.Skill_LKHeal
    
    #taco skills
    elif skill == lst.Skill_TacoMultiSwipe.id:
        return lst.Skill_TacoMultiSwipe
    elif skill == lst.Skill_TacoDistract.id:
        return lst.Skill_TacoDistract
    elif skill == lst.Skill_TacoCheer.id:
        return lst.Skill_TacoCheer
    
    #green skills
    elif skill == lst.Skill_GreenHeal.id:
        return lst.Skill_GreenHeal
    elif skill == lst.Skill_GreenBurn.id:
        return lst.Skill_GreenBurn
    elif skill == lst.Skill_GreenCalm.id:
        return lst.Skill_GreenCalm
    
    #storm skills
    elif skill == lst.Skill_StormShock.id:
        return lst.Skill_StormShock
    elif skill == lst.Skill_StormCalmDown.id:
        return lst.Skill_StormCalmDown
    elif skill == lst.Skill_StormCharge.id:
        return lst.Skill_StormCharge
    #hamy skills
    elif skill == lst.Skill_HamySpray.id:
        return lst.Skill_HamySpray
    elif skill == lst.Skill_HamyGun.id:
        return lst.Skill_HamyGun
    elif skill == lst.Skill_HamyZap.id:
        return lst.Skill_HamyZap
    #creation skills
    elif skill == lst.Skill_CreationCook.id:
        return lst.Skill_CreationCook
    elif skill == lst.Skill_CreationStare.id:
        return lst.Skill_CreationStare
    elif skill == lst.Skill_CreationSleepMode.id:
        return lst.Skill_CreationSleepMode
    #willow skills
    elif skill == lst.Skill_WillowIcyWind.id:
        return lst.Skill_WillowIcyWind
    elif skill == lst.Skill_WillowSnowyBreeze.id:
        return lst.Skill_WillowSnowyBreeze
    elif skill == lst.Skill_WillowFreeze.id:
        return lst.Skill_WillowFreeze
    #other skills
    elif skill == lst.Skill_RedHands.id: 
        return lst.Skill_RedHands
    elif skill == lst.Skill_SnowGrave.id:
        return lst.Skill_SnowGrave
    else:
        return lst.SkillTemplate
#--weapons----------------------------------
    #weapon converts
def weapon_conversion(stats):
    #generic equips
    if stats.weapon == eqp.Weapon_ToyKnife.id:#(1)
        return eqp.Weapon_ToyKnife
    elif stats.weapon == eqp.Weapon_AlterKnife.id: #(98)
        return eqp.Weapon_AlterKnife
    elif stats.weapon == eqp.Weapon_RealKnife.id: #(99)
        return eqp.Weapon_RealKnife
    #Lost Kid equips
    elif stats.weapon == eqp.Weapon_lkWornSickle.id: #(101)
        return eqp.Weapon_lkWornSickle
    #taco equips
    elif stats.weapon == eqp.Weapon_TacoStick.id: #(201)
        return eqp.Weapon_TacoStick
    #green equips
    #  none lol
    #storm equips
    elif stats.weapon == eqp.Weapon_StormSweatyBag.id: #(401)
        return eqp.Weapon_StormSweatyBag
    #hamy equips
    elif stats.weapon == eqp.Weapon_HamyHamer.id: #(501)
        return eqp.Weapon_HamyHamer
    #creation equips
    elif stats.weapon == eqp.Weapon_CreationPan.id: #(601)
        return eqp.Weapon_CreationPan
    #willow equips
    # none loll
    #fred equips
    elif stats.weapon == eqp.Weapon_FredKnife.id: #(9901)
        return eqp.Weapon_FredKnife
    elif stats.id == 3: #(0)
        return eqp.Weapon_NoWeaponGreen
    elif stats.id == 7: #(0)
        return eqp.Weapon_NoWeaponWillow
    else:
        return eqp.Weapon_NoWeapon
    
    #armor convert
def armor_conversion(stats):
    if stats.armor == eqp.Armor_EveryArmor.id:
        return eqp.Armor_EveryArmor
    elif stats.armor == eqp.Armor_GodArmor.id:
        return eqp.Armor_GodArmor
    elif stats.armor == eqp.Armor_AntiGodArmor.id:
        return eqp.Armor_AntiGodArmor
    else:
        return eqp.Armor_NoArmor

    #charm convert
def charm_conversion(stats):
    if stats.charm == eqp.Charm_TrueDreamBadge.id:
        return eqp.Charm_TrueDreamBadge
    elif stats.charm == eqp.Charm_PotatoBadge.id:
        return eqp.Charm_PotatoBadge
    elif stats.charm == eqp.Charm_PlotArmorBadge.id:
        return eqp.Charm_PlotArmorBadge
    elif stats.charm == eqp.Charm_FireOrb.id:
        return eqp.Charm_FireOrb
    else:
        return eqp.Charm_NoCharm 

    #adds stats to char based on weapon
def weapon_equip_calc(stats, weapon):
    if stats.id != 100:
        stats.weapon_name = weapon.name
        
        stats.weapon_type_hand  = weapon.type_hand
        stats.weapon_type_cut   = weapon.type_cut
        stats.weapon_type_swipe = weapon.type_swipe
        stats.weapon_type_poke  = weapon.type_poke
        stats.weapon_type_slam  = weapon.type_slam
        stats.weapon_type_whack = weapon.type_whack
        stats.weapon_type_projectile = weapon.type_projectile
        
        stats.attack += weapon.attack
        stats.magic  += weapon.magic
        
        stats.defence    += weapon.defence
        stats.spirit_defence += weapon.spirit_defence
        
        stats.cur_hp += weapon.cur_hp
        stats.max_hp += weapon.max_hp
        stats.cur_sp += weapon.cur_sp
        stats.max_sp += weapon.max_sp
        
        stats.luck  += weapon.luck
        stats.speed += weapon.speed

        equip_stat_fix(stats)

    #adds stats to char based on armor/charm
def armor_equip_calc(stats, armor, typ):
    if stats.id != 100:
        if typ == 'armor':
            stats.armor_name = armor.name
        elif typ == 'charm':
            stats.charm_name = armor.name
        
        stats.attack += armor.attack
        stats.magic  += armor.magic
        
        stats.defence    += armor.defence
        stats.spirit_defence += armor.spirit_defence
        
        stats.cur_hp += armor.cur_hp
        stats.max_hp += armor.max_hp
        stats.cur_sp += armor.cur_sp
        stats.max_sp += armor.max_sp
        
        stats.luck  += armor.luck
        stats.speed += armor.speed
        
        stats.resist_phyical -= armor.type_phyical
        stats.resist_hand    -= armor.type_hand
        stats.resist_cut     -= armor.type_cut
        stats.resist_swipe   -= armor.type_swipe
        stats.resist_poke    -= armor.type_poke
        stats.resist_slam    -= armor.type_slam
        stats.resist_whack   -= armor.type_whack
        stats.resist_projectile -= armor.type_projectile
        
        stats.resist_magic    -= armor.type_magic
        stats.resist_spector  -= armor.type_spector
        stats.resist_fire     -= armor.type_fire
        stats.resist_electric -= armor.type_electric
        stats.resist_ice      -= armor.type_ice
        stats.resist_plant    -= armor.type_plant
        stats.resist_antiplant -= armor.type_antiplant
        stats.resist_shadow   -= armor.type_shadow
        stats.resist_illusion -= armor.type_illusion
        stats.resist_holy     -= armor.type_holy
        stats.resist_hydro    -= armor.type_hydro
        stats.resist_food     -= armor.type_food

        equip_stat_fix(stats)

    #sets base for some stats
def equip_stat_fix(stats):
    if stats.exists == 1:
        if stats.cur_hp <= 0:
            stats.cur_hp = 1
        if stats.max_hp <= 0:
            stats.max_hp = 1
        if stats.cur_sp <= 0:
            stats.cur_sp = 0
        if stats.max_sp <= 0:
            stats.max_sp= 0


    

