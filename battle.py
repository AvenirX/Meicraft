import random
import time
from character import *


def battle(fighters, max_turn=10):
    """
    Battle process start->loot

    :param max_turn: int turns for 1 battle, default 10
    :param fighters: list of fighter
    :return: None
    """

    # Enter battle_process
    print('Enter battle_process')

    # Begin battle_process
    # Init skills (for n)
    for fighter in fighters:
        fighter.init_skills()
        fighter.report_status()

    # Turns begin
    turn = 1
    # Init turns
    # fighters_this_turn = list(fighters)
    fighters_remain = len(fighters)

    while turn <= max_turn and fighters_remain >= 2:
        # Enter Turn #turn
        print('\n#{t}'.format(t=turn))

        # Begin Turn #turn
        # Init turn
        # Construct fighters participate in this turn
        # & Init fighter turn paras
        fighters_this_turn = []
        for fighter in fighters:
            fighter.init_turn()
            if fighter.is_alive():
                fighters_this_turn.append(fighter)

        # Choose skill
        for fighter in fighters_this_turn:
            # NPC choose skill
            if fighter.is_npc:
                npc = fighter
                target = ''
                target_list = list(set(fighters_this_turn) - {npc})
                key = random.choice(npc.get_available_skills())
                skill = npc.BATTLESKILLBOOK[key]

                # If it's an A skill, choose its target
                if skill.phase_type == 'A':
                    target = random.choice(target_list)

            # Player input skill
            else:
                player = fighter
                target_list = list(set(fighters_this_turn) - {player})
                target = ''  # dummy?
                target_name = ''  # dummy?
                key = ''  # dummy?
                while True:
                    input_raw = input('BoLoBoLo...{s}:'
                                      .format(s=str(player.get_available_skills())))
                    input_args = input_raw.strip().split()

                    key = input_args[0].upper()
                    target_name = input_args[1] if len(input_args) > 1 else ''
                    if key in player.get_available_skills():
                        break
                skill = player.BATTLESKILLBOOK[key]

                # If it's an A skill, choose its target
                if skill.phase_type == 'A':
                    # Auto choose target when only 1 enemy
                    if len(target_list) == 1:
                        target = target_list[0]
                    else:
                        while True:
                            for target_fighter in target_list:
                                if target_fighter.name == target_name:
                                    target = target_fighter
                            if target:
                                break
                            target_name = input('target...')

            # Cast skill = record move, create proj, deliver proj
            skill.cast(target)

        # Billing
        for fighter in fighters:
            # Start billing by order
            for category in ['potion', 'arrow']:
                for tag in ['fill', 'drain', 'heal', 'damage']:
                    prjs = fighter.incoming_projectiles[category][tag]
                    if prjs:
                        for prj in prjs:
                            prj.billing()
            # All billed
            # Check death
            if fighter.HP <= 0:
                # fighter will die

                # fighter did die
                # go_die = set alive false, record turn, leave death message
                fighter.go_die(turn)
                fighters_remain -= 1

        # Output turn info
        # Moves
        for fighter in fighters:
            print('{hp}hp {mp}mp\t[{f}]|\t{m}'
                  .format(hp=fighter.HP, mp=fighter.MP,
                          f=fighter.name, m=str(fighter.last_move)))
            time.sleep(0.2)
        # Deaths
        for fighter in fighters_this_turn:
            if not fighter.is_alive():
                print('{f} 卒'.format(f=fighter.name))

        turn += 1
        continue

    # Exit turns
    print('\nExit turns')

    # Exit battle_process
    # Battle result
    score_board = sorted(fighters, key=lambda f: (f.died_turn, f.HP), reverse=True)
    for index, fighter in enumerate(score_board):
        if fighter.is_alive():
            status = '存活({hp}HP)'.format(hp=fighter.HP)
        else:
            killers = []
            for pj in fighter.killers:
                killer = '{owner}的{skill}'. \
                    format(owner=pj.owner.name, skill=pj.skill.alias)
                killers.append(killer)
            killers_msg = '&'.join(killers)

            status = '卒(Turn{t}, {hp}HP, 被{killer}所杀)' \
                .format(t=fighter.died_turn, hp=fighter.HP,
                        killer=killers_msg)
        print('#{i} {f} -- {s}'.format(i=index, f=fighter.name, s=status))

        # distribute_loot(player, enemy, battle_result)


# def distribute_loot(player, enemy, battle_result):
#     """
#     Distribute enemy loot to player according to battle result
#     :param player: obj
#     :param enemy: obj
#     :param battle_result: string 'WIN'/'LOSE'/'TIE'
#     :return: None
#     """
#     if battle_result == 'WIN':
#         c_money = 1
#         c_exp = 1
#         loot_item_dict = enemy.loot['item_dict']
#     elif battle_result == 'TIE':
#         c_money = 0
#         c_exp = 0.5
#         loot_item_dict = {}
#     elif battle_result == 'LOSE':
#         c_money = 0
#         c_exp = 0
#         loot_item_dict = {}
#
#     else:
#         return
#
#     player.add_money(enemy.loot['money'] * c_money)
#     player.add_exp(enemy.loot['EXP'] * c_exp)
#     for loot_item in loot_item_dict.keys():
#         player.get_item(loot_item, loot_item_dict[loot_item])


if __name__ == "__main__":
    zcx = Fighter('zcx')
    i = Fighter('i', is_npc=True)
    j = Fighter('j', is_npc=True)
    k = Fighter('k', is_npc=True)

    battle([zcx, i, j, k])

    # player1.report_wealth()
    # print(player1.level)
