"""
this file is where the skills are used
"""
import test_rpg_config as con
import test_rpg_config_translator as tran
import test_rpg_battle_stats_and_vars as var
import test_rpg_battle_messages_display as mes
import test_rpg_battle_other_functions as func
import test_rpg_battle_skill_list as lst
import random

#--skill-power--------------------

#the display/choosing for skills
def skill_choosing(stats):
    #sets the stats of each skill
    skill1 = tran.skill_conversion(stats.skill1)
    skill2 = tran.skill_conversion(stats.skill2)
    skill3 = tran.skill_conversion(stats.skill3)
    skill4 = tran.skill_conversion(stats.skill4)
    skill5 = tran.skill_conversion(stats.skill5)
    skip_skill = False
    #check if uses sp or pwr
    uses_sp =  not stats.health_type == 4
    if stats.health_type == 4:
        rate = lst.pwr_exchange_rate
    else:
        rate = 1
    
    #looks for the longest skill name (used for display)
    longest_name = len(skill1.name)
    if len(skill2.name) > longest_name:
        longest_name = len(skill2.name)
    if len(skill3.name) > longest_name:
        longest_name = len(skill3.name)
    if len(skill4.name) > longest_name:
        longest_name = len(skill4.name)
    if len(skill5.name) > longest_name:
        longest_name = len(skill5.name)
    
    #converts sp cost to pwr cost
    skill1_cost = skill1.cost * rate
    skill2_cost = skill2.cost * rate
    skill3_cost = skill3.cost * rate
    skill4_cost = skill4.cost * rate
    skill5_cost = skill5.cost * rate
    
    #shows what cost type
    if stats.health_type == 4:
        cost_type = 'pwr'
    elif stats.health_type == 2:
        cost_type = ''
    else:
        cost_type = 'sp'
    
    #choose skill
    if stats.skill1 != 0 or stats.skill2 != 0 or stats.skill3 != 0 or stats.skill4 != 0 or stats.skill5 != 0:
        skilling = True
        while skilling:
            print(f'What {f"Command" if stats.id == 1 else "Skill"}?  {func.side_text}')
            if stats.skill1 != 0:
                print(f'({con.option_1})|{mes.space_check(skill1.name, " ", longest_name)} - cost:{skill1_cost}{cost_type} - {skill1.check}')
            if stats.skill2 != 0:
                print(f'({con.option_2})|{mes.space_check(skill2.name, " ", longest_name)} - cost:{skill2_cost}{cost_type} - {skill2.check}')
            if stats.skill3 != 0:
                print(f'({con.option_3})|{mes.space_check(skill3.name, " ", longest_name)} - cost:{skill3_cost}{cost_type} - {skill3.check}')
            if stats.skill4 != 0:
                print(f'({con.option_4})|{mes.space_check(skill4.name, " ", longest_name)} - cost:{skill4_cost}{cost_type} - {skill4.check}')
            if stats.skill5 != 0:
                print(f'({con.option_5})|{mes.space_check(skill5.name, " ", longest_name)} - cost:{skill5_cost}{cost_type} - {skill5.check}')
            print(f'({con.option_back})|Back')
            
            #sets default
            choosen_skill = lst.SkillTemplate
            func.side_text = ''
            #the choice
            skill_choice = input()
            
            #sets action to the selected skill value
            if (skill_choice == con.option_1 and stats.skill1 != 0) or (skill_choice == con.option_2 and stats.skill2 != 0) or (skill_choice == con.option_3 and stats.skill3 != 0) or (skill_choice == con.option_4 and stats.skill4 != 0) or (skill_choice == con.option_5 and stats.skill5 != 0) or skill_choice == con.option_back:
                if stats.skill1 != 0 and skill_choice == con.option_1 and ((stats.cur_sp >= skill1_cost and uses_sp) or (stats.cur_pwr >= skill1_cost and stats.health_type == 4)):
                    stats.action = skill1.id
                    choosen_skill = skill1
                elif stats.skill2 != 0 and skill_choice == con.option_2 and ((stats.cur_sp >= skill2_cost and uses_sp) or (stats.cur_pwr >= skill2_cost and stats.health_type == 4)):
                    stats.action = skill2.id
                    choosen_skill = skill2
                elif stats.skill3 != 0 and skill_choice == con.option_3 and ((stats.cur_sp >= skill3_cost and uses_sp) or (stats.cur_pwr >= skill3_cost and stats.health_type == 4)):
                    stats.action = skill3.id
                    choosen_skill = skill3
                elif stats.skill4 != 0 and skill_choice == con.option_4 and ((stats.cur_sp >= skill4_cost and uses_sp) or (stats.cur_pwr >= skill4_cost and stats.health_type == 4)):
                    stats.action = skill4.id
                    choosen_skill = skill4
                elif stats.skill5 != 0 and skill_choice == con.option_5 and ((stats.cur_sp >= skill5_cost and uses_sp) or (stats.cur_pwr >= skill5_cost and stats.health_type == 4)):
                    stats.action = skill5.id
                    choosen_skill = skill5
                elif skill_choice == con.option_back:
                    stats.action = -69
                    skip_skill = True
                    skilling = False
                else:
                    func.side_text = f'(not enough sp)'
            else:
                func.side_text = f'(invalid command)'
                
            #-target-types--------
            if choosen_skill.target == 4: #enemy target x2
                print(f'To whom?')
                func.party_targeting(stats, 'enemy')
                stats.target2 = stats.target
                stats.target = 0
                if stats.target2 != 0:
                    print(f'And whom?')
                    func.party_targeting(stats, 'enemy')
                    if stats.target != 0:
                        skilling = False
                    else:
                        stats.target2 = 0
                        func.turn = 1
               
            elif choosen_skill.target == 3: #party target
                print(f'To whom?')
                func.party_targeting(stats, 'party')
                skilling = False
            elif choosen_skill.target == 2: #enemy target
                print(f'To whom?')
                func.party_targeting(stats, 'enemy')
                skilling = False
            elif choosen_skill.target == 1: #no target
                skilling = False
        
        if not skilling and not skip_skill and stats.action != 0:
            func.turn = 0
            if stats.action == -69:
                stats.action = 0
    else:
        func.side_text = f'(No skills)'
        
#--enemy-action-calc----------------------------------------

def enemy_choosing_action(stats):
        #lk action
    if stats.id == 1:
        stats.action = 1
        #taco action
    elif stats.id == 2:
        if stats.cur_sp >= lst.Skill_TacoMultiSwipe.cost:
            stats.action = lst.Skill_TacoMultiSwipe.id
        #greeen action
    elif stats.id == 3:
        if stats.cur_sp >= lst.Skill_GreenBurn.cost:
            stats.action = lst.Skill_GreenBurn.id
        else:
            stats.action = 2
        #storm action
    elif stats.id == 4:
        if stats.cur_hp <= stats.max_hp / 25:
            stats.action = lst.Skill_StormCalmDown.id
        elif stats.cur_sp >= lst.Skill_StormShock.cost:
            stats.action = lst.Skill_StormShock.id
        else:
            stats.action = 1
        #hamy action
    elif stats.id == 5:
        #bugged
        if stats.cur_sp >= lst.Skill_HamySpray.cost and not (var.pLStats.spray_debuff_turn > 0 or var.p1Stats.spray_debuff_turn > 0 or var.p2Stats.spray_debuff_turn > 0 or var.p3Stats.spray_debuff_turn > 0):
            stats.action = lst.Skill_HamySpray.id
        elif stats.cur_sp >= lst.Skill_HamyGun.cost and (var.pLStats.spray_debuff_turn > 0 or var.p1Stats.spray_debuff_turn > 0 or var.p2Stats.spray_debuff_turn > 0 or var.p3Stats.spray_debuff_turn > 0):
            stats.action = lst.Skill_HamyGun.id
        else:
            stats.action = 1
        #willow action
    elif stats.id == 7:
        if stats.cur_sp >= lst.Skill_WillowIcyWind.cost:
            stats.action = lst.Skill_WillowIcyWind.id
        else:
            stats.action = 2
        #SOMETHING
    elif stats.id == var.SomethingStats.id:
        print("  Liar")
    else:
        stats.action = 1

#--skill-interp----------------------------------------------

def skill_list(stats):
    if stats.party_slot > 0 and stats.to_party == 0:
        target_stats  = func.party_target_translator(func.party_target_correction(stats,stats.target))
        target_stats2 = func.party_target_translator(func.party_target_correction(stats,stats.target2))
    else:
        target_stats = func.enemy_target_translator(stats.target)
        target_stats2 = func.enemy_target_translator(stats.target2)
    
    #nothing
    if stats.action == -1:
        mes.battle_messages(stats, target_stats)
    #nothing with no message
    elif stats.action == 0:
        pass
    #basic attack
    elif stats.action == 1:
        stats.dmg = lst.basic_attack(stats, target_stats, lst.Skill_BasicAttack)
        lst.miss_calc(stats, target_stats)
        func.health_sub_calc(stats, target_stats)
        target_stats.damaged += 1 * stats.miss
        if stats.health_type == 4:
            func.pwr_add_calc(stats, lst.cost_basic_attack_pwr)
        else:
            func.sp_add_calc(stats, lst.cost_gain_basic_attack) 
        func.sp_cost_miss(stats, target_stats)
        mes.battle_messages(stats, target_stats)
        func.refuse_check(stats, target_stats)
        func.rage_add_calc(stats, lst.Skill_BasicAttack.rage_add)
        func.rage_add_calc(target_stats, lst.gain_rage_hit * stats.miss)
    #defend
    elif stats.action == 2:
        stats.defending = 1.5
        if stats.health_type == 4:
            func.pwr_add_calc(stats, lst.cost_gain_defending_pwr)
        else:
            func.sp_add_calc(stats, lst.cost_gain_defending)
        mes.battle_messages(stats, target_stats)
    #check
    elif stats.action == lst.Skill_LKCheck.id:
        func.sp_sub_calc(stats, lst.Skill_LKCheck.cost)
        lst.lkcheck(stats, target_stats)
    #lkheal
    elif stats.action == lst.Skill_LKHeal.id:
        func.sp_sub_calc(stats,lst.Skill_LKHeal.cost)
        stats.dmg = lst.lkheal(stats, target_stats, lst.Skill_LKHeal)
        func.hp_add_calc(target_stats, stats.dmg)
        mes.battle_messages(stats, target_stats)
        func.rage_add_calc(target_stats, lst.Skill_LKHeal.rage_add)
    #multi-swipe
    elif stats.action == lst.Skill_TacoMultiSwipe.id:
        func.sp_sub_calc(stats,lst.Skill_TacoMultiSwipe.cost)
        for i in range(2):
            stats.dmg = lst.basic_attack(stats, target_stats2, lst.Skill_TacoMultiSwipe)
            lst.miss_calc(stats, target_stats2)
            func.health_sub_calc(stats, target_stats2)
            target_stats.damaged += 1 * stats.miss
            func.sp_cost_miss(stats, target_stats2)
            mes.battle_messages(stats, target_stats2)
            func.refuse_check(stats, target_stats2)
            func.rage_add_calc(target_stats, lst.gain_rage_hit * stats.miss)
            target_stats = func.party_target_translator(func.party_target_correction(stats,stats.target))
            target_stats2 = target_stats
            func.rage_add_calc(stats, lst.Skill_TacoMultiSwipe.rage_add)
    #distract
    elif stats.action == lst.Skill_TacoDistract.id:
        func.sp_sub_calc(stats,lst.Skill_TacoDistract.cost)
        stats.targeted = 1
        stats.defending = 1.2
        mes.battle_messages(stats, target_stats)
        func.rage_add_all_enemy(lst.Skill_TacoDistract.rage_add)
    #cheer
    elif stats.action == lst.Skill_TacoCheer.id:
        func.sp_sub_calc(stats,lst.Skill_TacoCheer.cost)
        bonus = 1 if stats.id == target_stats.id else 0
        stats.cur_sp += lst.Skill_TacoCheer.cost if bonus > 0 else 0
        stats.dmg = lst.Skill_TacoCheer.power + bonus
        func.sp_add_calc(target_stats, stats.dmg)
        mes.battle_messages(stats, target_stats)
        func.rage_add_calc(target_stats, lst.Skill_TacoCheer.rage_add)
    #greenheal
    elif stats.action == lst.Skill_GreenHeal.id:
        func.sp_sub_calc(stats,lst.Skill_GreenHeal.cost)
        stats.dmg = lst.greenheal(stats, target_stats, lst.Skill_GreenHeal)
        func.hp_add_calc(target_stats, stats.dmg)
        mes.battle_messages(stats, target_stats)
        func.rage_add_calc(target_stats, lst.Skill_GreenHeal.rage_add)
    #burn
    elif stats.action == lst.Skill_GreenBurn.id:
        func.sp_sub_calc(stats,lst.Skill_GreenBurn.cost)
        stats.dmg = lst.green_burn_calc(stats, target_stats, lst.Skill_GreenBurn)
        #lst.miss_calc(stats, target_stats)
        func.health_sub_calc(stats, target_stats)
        target_stats.damaged += 1 * stats.miss
        func.sp_cost_miss(stats, target_stats)
        mes.battle_messages(stats, target_stats)
        lst.green_burn_debuff(stats, target_stats, lst.Skill_GreenBurn)
        func.refuse_check(stats, target_stats)
        func.rage_add_calc(stats, lst.Skill_GreenBurn.rage_add)
        func.rage_add_calc(target_stats, lst.gain_rage_hit * stats.miss)
    #greencalm
    elif stats.action == lst.Skill_GreenCalm.id:
        func.sp_sub_calc(stats,lst.Skill_GreenCalm.cost)
        stats.dmg = lst.greenheal(stats, target_stats, lst.Skill_GreenCalm)
        stats.crit = lst.greencalmsp(stats, target_stats, lst.Skill_GreenCalm)
        func.hp_add_calc(target_stats, stats.dmg)
        func.sp_add_calc(target_stats, stats.crit)
        mes.battle_messages(stats, target_stats)
        func.rage_add_calc(target_stats, lst.Skill_GreenCalm.rage_add)
        stats.crit = 0
    #shock
    elif stats.action == lst.Skill_StormShock.id:
        func.sp_sub_calc(stats,lst.Skill_StormShock.cost)
        stats.dmg = lst.magic_dmg_calc(stats, target_stats, lst.Skill_StormShock)
        func.charge_add_calc(stats, 1)
        lst.miss_calc(stats, target_stats)
        func.health_sub_calc(stats, target_stats)
        target_stats.damaged += 1 * stats.miss
        func.sp_cost_miss(stats, target_stats)
        mes.battle_messages(stats, target_stats)
        func.refuse_check(stats, target_stats)
        func.rage_add_calc(stats, lst.Skill_StormShock.rage_add)
        func.rage_add_calc(target_stats, lst.gain_rage_hit * stats.miss)
    #stormcalmdown
    elif stats.action == lst.Skill_StormCalmDown.id:
        func.sp_sub_calc(stats,lst.Skill_StormCalmDown.cost)
        stats.defending = 1.2
        stats.dmg = lst.stormcalmdownhp(stats, target_stats, lst.Skill_StormCalmDown)
        stats.crit = lst.stormcalmdownsp(stats, target_stats, lst.Skill_StormCalmDown)
        func.hp_add_calc(stats, stats.dmg)
        func.sp_add_calc(stats, stats.crit)
        stats.charge = 0
        mes.battle_messages(stats, target_stats)
        func.rage_add_calc(stats, lst.Skill_StormCalmDown.rage_add)
        stats.crit = 0
    #charge
    elif stats.action == lst.Skill_StormCharge.id:
        func.sp_sub_calc(stats,lst.Skill_StormCharge.cost)
        if stats.charge < stats.max_charge:
            stats.charge = stats.max_charge
        else:
            stats.charge += 1
        mes.battle_messages(stats, target_stats)
        func.rage_add_calc(stats, lst.Skill_StormCharge.rage_add)
    #spray
    elif stats.action == lst.Skill_HamySpray.id:
        func.sp_sub_calc(stats,lst.Skill_HamySpray.cost)
        stats.crit = 1
        mes.battle_messages(stats, target_stats)
        for estats in [var.pLStats, var.p1Stats, var.p2Stats, var.p3Stats, var.e1Stats, var.e2Stats, var.e3Stats, var.e4Stats]:
            if estats.exists == 1 and estats.alive == 1 and ((stats.party_slot >= 1 and estats.enemy_slot >= 1) or (stats.enemy_slot >= 1 and estats.party_slot >= 1)):
                total = 0
                estats.spray_debuff_turn = 1
                func.buff_calc(estats, 'def', lst.debuff_spray)
                func.buff_calc(estats, 'spdef', lst.debuff_spray)
                for i in range(8):
                    stats.dmg = lst.ham_attack_calc(stats, estats, lst.Skill_HamySpray)
                    #lst.miss_calc(stats, estats)
                    func.health_sub_calc(stats, estats)
                    estats.damaged += 1 * stats.miss
                    total += stats.dmg * stats.miss
                    if not func.health_check(estats) and estats.refuse > 0 and i != 9:
                        estats.refuse -= 1
                        estats.cur_hp = 1
                        estats.cur_pwr = 1
                stats.dmg = total
                stats.crit = 0
                mes.battle_messages(stats, estats)
                func.sp_cost_miss(stats, estats)
                func.refuse_check(stats, estats)
                func.rage_add_calc(estats, lst.gain_rage_hit * stats.miss * 3)
        func.rage_add_calc(stats, lst.Skill_HamySpray.rage_add)
    #gun
    elif stats.action == lst.Skill_HamyGun.id:
        func.sp_sub_calc(stats,lst.Skill_HamyGun.cost)
        stats.dmg = lst.ham_attack_calc(stats, target_stats, lst.Skill_HamyGun)
        lst.miss_calc(stats, target_stats)
        func.health_sub_calc(stats, target_stats)
        target_stats.damaged += 1 * stats.miss
        func.sp_cost_miss(stats, target_stats)
        mes.battle_messages(stats, target_stats)
        func.refuse_check(stats, target_stats)
        func.rage_add_calc(stats, lst.Skill_HamyGun.rage_add)
        func.rage_add_calc(target_stats, lst.gain_rage_hit * stats.miss)
    #creation cook
    elif stats.action == lst.Skill_CreationCook.id:
        func.sp_sub_calc(stats,lst.Skill_CreationCook.cost)
        stats.dmg = lst.creation_cook_heal(stats, target_stats, lst.Skill_CreationCook)
        func.hp_add_calc(target_stats, stats.dmg)
        mes.battle_messages(stats, target_stats)
        func.rage_add_calc(target_stats, lst.Skill_CreationCook.rage_add)
    #icywind
    elif stats.action == lst.Skill_WillowIcyWind.id:
        func.sp_sub_calc(stats,lst.Skill_WillowIcyWind.cost)
        stats.dmg = lst.magic_dmg_calc(stats, target_stats, lst.Skill_WillowIcyWind)
        #func.charge_add_calc(stats, 0.5)
        lst.miss_calc(stats, target_stats)
        func.health_sub_calc(stats, target_stats)
        target_stats.damaged += 1 * stats.miss
        func.sp_cost_miss(stats, target_stats)
        mes.battle_messages(stats, target_stats)
        func.refuse_check(stats, target_stats)
        func.rage_add_calc(stats, lst.Skill_WillowIcyWind.rage_add)
        func.rage_add_calc(target_stats, lst.gain_rage_hit * stats.miss)
    #RED HANDS
    elif stats.action == lst.Skill_RedHands.id:
        func.sp_sub_calc(stats,lst.Skill_RedHands.cost)
        target_stats.refuse += 1
        for i in range(4):
            target_stats.refuse -= 1
            stats.dmg = lst.basic_attack(stats, target_stats, lst.Skill_RedHands)
            lst.miss_calc(stats, target_stats)
            func.health_sub_calc(stats, target_stats)
            target_stats.damaged += 1 * stats.miss
            func.sp_cost_miss(stats, target_stats)
            mes.battle_messages(stats, target_stats)
            func.rage_add_calc(stats, lst.Skill_RedHands.rage_add)
            func.rage_add_calc(target_stats, lst.gain_rage_hit * stats.miss)
        func.refuse_check(stats, target_stats)
    #SNOWGRAVE
    elif stats.action == lst.Skill_SnowGrave.id:
        func.sp_sub_calc(stats,lst.Skill_SnowGrave.cost)
        target_stats.refuse += 1
        for i in range(3):
            target_stats.refuse -= 1
            stats.dmg = lst.magic_dmg_calc(stats, target_stats, lst.Skill_SnowGrave)
            #lst.miss_calc(stats, target_stats)
            func.health_sub_calc(stats, target_stats)
            target_stats.damaged += 1 * stats.miss
            func.sp_cost_miss(stats, target_stats)
            mes.battle_messages(stats, target_stats)
            func.rage_add_calc(stats, lst.Skill_SnowGrave.rage_add)
            func.rage_add_calc(target_stats, lst.gain_rage_hit * stats.miss)
        func.refuse_check(stats, target_stats)
    else:
        print(f'? {stats.name}, action:{stats.action}, target:{stats.target} ({target_stats.name}), target2:{stats.target2} ({target_stats2.name})')
    
        
        
        
        
        





