# toImpr remove import?
from Skill import the_skill


class Hero:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

        self.level = 1
        self.EXP = 0

        self.__HP = 5
        # self.__STR = 2
        # self.__AGI = 1
        # self.__INT = 1
        self.__STA = 1

        self.HP = 0
        # self.STR = 0
        # self.AGI = 0
        # self.INT = 0
        self.STA = 0

        self.SKILLBOOK = ['attack', 'prep', 'defend']

        self.money = 0
        self.equipments = {
            # 'weapon': None,
            # 'armour': None,
            # 'jewelry': None
        }

        self.inventory = []
        self.loot = self.inventory

        self.reset_status()

        self.alive = True

    def __repr__(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

    def reset_status(self):
        # self.STR = self.__STR
        # self.AGI = self.__AGI
        # self.INT = self.__INT
        self.STA = self.__STA

        self.HP = self.__HP + self.STA * 1

    def is_alive(self):
        return True if self.alive else False

    def increase_hp(self, amount):
        self.HP += amount

    def add_exp(self, amount):
        self.EXP += amount
        print('{p} gets {e} EXP'.format(p=self.name, e=amount))
        # self.level_up()
    #
    # def level_up(self):
    #     while self.EXP > level_exp[self.level]:
    #         self.EXP -= level_exp[self.level]
    #         self.level += 1
    #
    #         self.__HP += 1
    #         self.__STR += 2
    #         self.__AGI += 1
    #         self.__INT += 1
    #         self.__STA += 1
    #
    #         self.reset_status()
    #         print('\t\t\t\t\t\t\t\t\t\tHERO [{p}] LEVEL UP!'.format(p=self.name))
    #     return

    # def acquire_item(self, item_id):
    #     item = the_item(item_id)()
    #     self.put_in_item(item)

    def put_in_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def take_out_item(self, item):
        self.inventory.remove(item)

    def equip_item(self, item):
        if item in self.inventory and item.equipment:
            self.take_out_item(item)
            self.equipments[item.category] = item

    def unequip_item(self, item):
        if self.equipments[item.category]:
            self.equipments[item.category] = None
            self.put_in_item(item)

    # def increase_level(self, n):
    #     self.level += n
    #     print('{p} level is increased by {n}'.format(p=self.name, n=n))

    # toImpr new report according to new inventory
    # def report_wealth(self):
    #     print('{p} has {e} EXP, {m} money'.format(
    #         p=self.name,
    #         e=self.EXP,
    #         m=self.money
    #     ))
    #
    #     print('Bag:\n-----------')
    #     if self.inventory:
    #         for item in self.inventory:
    #             print('{i} x {n}'.format(i=item, n=self.inventory[item]))
    #     else:
    #         print('Empty')
    #     print('-----------')

    def add_money(self, amount):
        self.money += amount
        print('{p} gets {m} money'.format(p=self.name, m=amount))

#
# level_exp = {
#     1: 20,
#     2: 40,
#     3: 80,
#     4: 160
# }


class Fighter(Hero):
    def __init__(self, name, type_='STR', is_npc=False):
        super(Fighter, self).__init__(name, type_)
        self.PHASE = ''
        self.MP = 0
        self.BATTLESKILLBOOK = {}

        self.is_npc = is_npc
        self.died_turn = 9999
        self.lethal_projectiles = []
        self.score = 0
        self.kills = 0
        self.survive_turns = 0

        self.last_move = None
        self.incoming_projectiles = None
        self.init_turn()

        print('Fighter [{name}({type_})] initialized'.format(
            name=self.name,
            type_=self.type_), end=' ')
        print(self.BATTLESKILLBOOK)

    def init_battle(self):
        self.load_battle_skills()
        self.score = 0
        self.kills = 0
        self.survive_turns = 0

    def load_battle_skills(self):
        for skill_id in self.SKILLBOOK:
            skill = the_skill(skill_id)(self)
            self.BATTLESKILLBOOK[skill.key] = skill

        for category, equipment in self.equipments.items():
            if category in ['weapon', 'armour', 'jewelry']:
                skill_id = equipment.skill
                skill = the_skill(skill_id)(self)
                self.BATTLESKILLBOOK[skill.key] = skill

    # def init_skills(self):
    #     self.BATTLESKILLBOOK = {'A': the_skill('attack')(self),
    #                             'A2': the_skill('attack2')(self),
    #                             'D': the_skill('defend')(self),
    #                             'P': the_skill('prep')(self)}

    def init_turn(self):
        self.incoming_projectiles = {
            'potion': {'heal': [], 'damage': [], 'fill': [], 'drain': []},
            'arrow': {'heal': [], 'damage': [], 'fill': [], 'drain': []}
        }
        self.last_move = '...'
        if self.is_alive():
            self.survive_turns += 1
            # toImpr move to turns over
            self.gain_score(1)

    def get_available_skills(self):
        available_skills = []
        for skill_key in self.BATTLESKILLBOOK:
            if self.BATTLESKILLBOOK[skill_key].is_available():
                available_skills.append(skill_key)
            else:
                continue
        return available_skills

    # toImpr move to Hero
    def increase_mp(self, amount):
        self.MP += amount

    def gain_score(self, amount):
        self.score += amount

    def set_phase(self, phase_type):
        self.PHASE = phase_type

    def killed_someone(self):
        # toImpr move magical nb to global setting
        # toImpr scoring move to turns over?
        self.gain_score(3)
        self.kills += 1

    def go_die(self, turn):
        self.alive = False
        self.died_turn = turn
        self.lethal_projectiles = self.incoming_projectiles['arrow']['damage']

    def report_status(self):
        print('[{n}]: {hp} HP {mp} MP {s}'
              .format(n=self.name, hp=self.HP, mp=self.MP, s=str(self.BATTLESKILLBOOK.keys())))







