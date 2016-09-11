import newSkill


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
        self.equipment = {
            'weapon': None,
            'armour': None,
            'jewelry': None
        }

        self.inventory = {}
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

    def get_item(self, item, n):
        if item in self.inventory:
            self.inventory[item] += n
        else:
            self.inventory[item] = 1
        print('{p} gets {i} x {n}'.format(p=self.name, n=n, i=item))

    def drop_item(self, item, n):
        if self.inventory[item] > n + 1:
            self.inventory[item] -= n
        elif self.inventory[item] == n:
            del self.inventory[item]
        else:
            del self.inventory[item]
            print('Player-remove_item: negative number -> 0')
        print('{p} drops {i} x {n}'.format(p=self.name, n=n, i=item))

    def add_skills(self, skill_names):
        self.SKILLBOOK += skill_names

    # def increase_level(self, n):
    #     self.level += n
    #     print('{p} level is increased by {n}'.format(p=self.name, n=n))

    def report_wealth(self):
        print('{p} has {e} EXP, {m} money'.format(
            p=self.name,
            e=self.EXP,
            m=self.money
        ))

        print('Bag:\n-----------')
        if self.inventory:
            for item in self.inventory.keys():
                print('{i} x {n}'.format(i=item, n=self.inventory[item]))
        else:
            print('Empty')
        print('-----------')

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


def the_skill(skill_name):
    """
    Skill caller
    :param skill_name: string
    :return: the skill function
    """
    return getattr(newSkill, 'Skill_' + skill_name)


class Fighter(Hero):
    def __init__(self, name, type_='STR', is_npc=False):
        super(Fighter, self).__init__(name, type_)
        self.PHASE = ''
        self.MP = 0
        self.BATTLESKILLBOOK = {}

        self.is_npc = is_npc
        self.died_turn = 9999
        self.killers = []
        self.score = 0

        self.last_move = None
        self.incoming_projectiles = None
        self.init_turn()

        print('Fighter [{name}({type_})] initialized'.format(
            name=self.name,
            type_=self.type_), end=' ')
        print(self.BATTLESKILLBOOK)

    def init_skills(self):
        self.BATTLESKILLBOOK = {'A': the_skill('attack')(self),
                                'A2': the_skill('attack2')(self),
                                'D': the_skill('defend')(self),
                                'P': the_skill('prep')(self)}

    def init_turn(self):
        self.incoming_projectiles = {
            'potion': {'heal': [], 'damage': [], 'fill': [], 'drain': []},
            'arrow': {'heal': [], 'damage': [], 'fill': [], 'drain': []}
        }
        self.last_move = '...'

    def get_available_skills(self):
        available_skills = []
        for skill_key in self.BATTLESKILLBOOK:
            if self.BATTLESKILLBOOK[skill_key].is_available():
                available_skills.append(skill_key)
            else:
                continue
        return available_skills

    def increase_mp(self, amount):
        self.MP += amount

    def set_phase(self, phase_type):
        self.PHASE = phase_type

    def go_die(self, turn):
        self.alive = False
        self.died_turn = turn
        self.killers = [self.incoming_projectiles['arrow']['damage']]

    def report_status(self):
        print('[{n}]: {hp} HP {mp} MP {s}'
              .format(n=self.name, hp=self.HP, mp=self.MP, s=str(self.BATTLESKILLBOOK.keys())))







