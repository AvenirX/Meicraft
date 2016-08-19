import skill
import random
from character import *


def get_skill(skill_name):
    return getattr(skill, 'skill_'+skill_name)


def battle(player, enemy):
    # Enter battle_process
    print('Enter battle_process')
    battle_result = None

    # Begin battle_process

    # Enter turns
    # Begin turns
    # init
    maxTurn = 10

    turn = 1
    attacker = player
    defender = enemy

    while turn <= maxTurn:
        # turn += 1
        print('\n#{t}'.format(t=turn))

        # Choose skill
        skill_name = random.choice(attacker.SKB)
        # print('[{a}] uses [{skn}]'.format(a=attacker.name, skn=skill.__name__))
        projectile1 = get_skill(skill_name)(attacker, defender)
        skill.billing(projectile1)
        attacker.report_status()
        defender.report_status()

        if player.HP <= 0:
            # Will die

            # Did die
            battle_result = 'LOSE'
            break

        elif enemy.HP <= 0:
            # Will die

            # Did die
            battle_result = 'WIN'
            break
        else:
            turn += 0.5
            attacker, defender = defender, attacker
            continue

    if not battle_result:
        battle_result = 'TIE'

    # Exit turns
    print('Exit turns, \t\t\t\t\t\t\t\t\t\t[{n}][{r}]'.format(n=player.name, r=battle_result))

    # Exit battle_process
    distribute_loot(player, enemy, battle_result)


def distribute_loot(player, enemy, battle_result):
    if battle_result == 'WIN':
        c_money = 1
        c_exp = 1
        loot_item_dict = enemy.loot['item_dict']
    elif battle_result == 'TIE':
        c_money = 0
        c_exp = 0.5
        loot_item_dict = {}
    elif battle_result == 'LOSE':
        c_money = 0
        c_exp = 0
        loot_item_dict = {}

    else:
        return

    player.add_money(enemy.loot['money'] * c_money)
    player.add_exp(enemy.loot['EXP'] * c_exp)
    for loot_item in loot_item_dict.keys():
        player.add_item(loot_item, loot_item_dict[loot_item])


player1 = Player('M', 'STR')
enemy1 = Boss('YXF', 'STR')

battle(player1, enemy1)

player1.report_wealth()
print(player1.level)
