"""
this is the main battle loop file
"""
#imports needed other files
#for stats
import test_rpg_battle_stats_and_vars as var
#for functions
import test_rpg_battle_other_functions as func
#for display stuff
import test_rpg_battle_messages_display as mes
#for skills
import test_rpg_battle_skills as skl
#config stuff
import test_rpg_config as con
#rando
import random

#--debug-(ignore)-----------
#func.rage_add_all_party(50)
var.battle_cycle = 0
#---------------------------

def battle_start(e1, e2, e3, e4):
    #sets enemys
    con.enemy1 = e1
    con.enemy2 = e2
    con.enemy3 = e3
    con.enemy4 = e4
    
    #--MAIN-GAMEPLAY-LOOP----------------------------
    var.stats_define()
    first_turn = True
    var.turn_number = 0
    var.turn_number_message = 0
    var.running = 0
    var.currently_battling = 1
    #full heals enemys
    func.enemy_full_heal()
    while var.currently_battling == 1:
        #sets some basic vars
        our_turn = True
        func.first_action = True
        var.current_member_turn = 0
        var.turn_number += 1
        var.turn_number_message += 1
        
        #party hp sp showing and clears screen if turn 1
        if var.turn_number == 1:
            mes.clear_screen()
        
        mes.display_hp_and_sp()

        #--party turn---------------------------------
        #party choosing actions
        while our_turn:
            var.current_member_turn += 1
            #party leader's turn
            if var.pLStats.exists == 1 and func.health_check(var.pLStats) and var.current_member_turn == 1:
                func.party_turn(var.pLStats)
            
            #party1's turn
            if var.p1Stats.exists == 1 and func.health_check(var.p1Stats) and var.current_member_turn == 2:
                func.party_turn(var.p1Stats)
            
            #party2's turn
            if var.p2Stats.exists == 1 and func.health_check(var.p2Stats) and var.current_member_turn == 3:
                func.party_turn(var.p2Stats)
                  
            #party3's turn
            if var.p3Stats.exists == 1 and func.health_check(var.p3Stats) and var.current_member_turn == 4:
                func.party_turn(var.p3Stats)
            
            #if everyone had turn
            if var.current_member_turn == 5 or var.running == 1:
                our_turn = False
        
        if var.running != 1:
            #clear screen
            mes.clear_screen()
            
            #has the party does their actions + display a message
            print(f'--PARTY-TURN------------------------------------')
            skl.skill_list(var.pLStats)
            skl.skill_list(var.p1Stats)
            skl.skill_list(var.p2Stats)
            skl.skill_list(var.p3Stats)
            
            #check if anyone has gone down
            func.down_check_full()
            
            #enemy turn code
            print(f'--ENEMY-TURN------------------------------------')
            #enemy1 turn
            if var.e1Stats.exists:
                skl.enemy_choosing_action(var.e1Stats)
                func.enemy_choosing_target(var.e1Stats)
                skl.skill_list(var.e1Stats)
            #enemy2 turn
            if var.e2Stats.exists:
                skl.enemy_choosing_action(var.e2Stats)
                func.enemy_choosing_target(var.e2Stats)
                skl.skill_list(var.e2Stats)
            #enemy3 turn
            if var.e3Stats.exists:
                skl.enemy_choosing_action(var.e3Stats)
                func.enemy_choosing_target(var.e3Stats)
                skl.skill_list(var.e3Stats)
            #enemy4 turn
            if var.e4Stats.exists:
                skl.enemy_choosing_action(var.e4Stats)
                func.enemy_choosing_target(var.e4Stats)
                skl.skill_list(var.e4Stats)
            print(f'------------------------------------------------')
            
            #--down-check------------------------------
            func.down_check_full()
            func.all_enemy_down_calc()
            func.pl_down_calc()
            
            #-upped-check------------------------------
            func.upped_check(var.pLStats)
            func.upped_check(var.p1Stats)
            func.upped_check(var.p2Stats)
            func.upped_check(var.p3Stats)
        
        #func.debug()
        #move enemy reset up
        #--resets---------------------------
        for stats in [var.pLStats, var.p1Stats, var.p2Stats, var.p3Stats, var.e1Stats, var.e2Stats, var.e3Stats, var.e4Stats]:
            func.action_reset(stats)
            func.buff_check(stats)
        
        func.rage_add_all_party(1)
        func.rage_add_all_enemy(1)
        
        #func.debug()
    
    #saves the hp at the end of battle
    func.end_battle_hp_sp(var.pLStats)
    func.end_battle_hp_sp(var.p1Stats)
    func.end_battle_hp_sp(var.p2Stats)
    func.end_battle_hp_sp(var.p3Stats)
    
    func.end_battle_hp_sp(var.e1Stats)
    func.end_battle_hp_sp(var.e2Stats)
    func.end_battle_hp_sp(var.e3Stats)
    func.end_battle_hp_sp(var.e4Stats)

#battle!
battle_start(104, 104, 104, 0)
for i in range(99):
    var.battle_cycle += 1
    rng = random.randint(1,7)
    if rng == 1:
        battle_start(104, 104, 104, 0)
    elif rng == 2:
        battle_start(101, 0, 0, 0)
    elif rng == 3:
        battle_start(5, 6, 0, 0)
    elif rng == 4:
        battle_start(99, 0, 0, 0)
    elif rng == 5:
        battle_start(134, 0, 0, 0)
    elif rng == 6:
        battle_start(101, 101, 101, 0)
    elif rng == 7:
        battle_start(7, 7, 7, 0)
    else:
        battle_start(0,0,0,0)





