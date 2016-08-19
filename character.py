from dev import *


class Hero:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

        self.level = 1
        self.EXP = 0

        self.__HP = 100
        self.__STR = 10
        self.__AGI = 5
        self.__INT = 5
        self.__STA = 5

        self.HP = 0
        self.STR = 0
        self.AGI = 0
        self.INT = 0
        self.STA = 0

        self.SKB = []

        self.equipment = []
        self.bag = {}

        self.update_attr()

        print('Boss [{name}({type_})] initialized'.format(
            name=self.name,
            type_=self.type_))

    def update_attr(self):
        self.STR = self.__STR
        self.AGI = self.__AGI
        self.INT = self.__INT
        self.STA = self.__STA

        self.HP = self.__HP + self.STA * 1

    def increase_hp(self, amount):
        self.HP += amount

    def decrease_hp(self, amount):
        self.HP -= amount

    def add_exp(self, amount):
        self.EXP += amount
        print('{p} gets {e} EXP'.format(p=self.name, e=amount))
        self.level_up()

    def level_up(self):
        while self.EXP > level_exp[self.level]:
            self.EXP -= level_exp[self.level]
            self.level += 1

            self.__HP += 100
            self.__STR += 2
            self.__AGI += 1
            self.__INT += 1
            self.__STA += 2

            self.update_attr()
            print('\t\t\t\t\t\t\t\t\t\tHERO [{p}] LEVEL UP!'.format(p=self.name))
        return

    def add_item(self, item, n):
        if item in self.bag:
            self.bag[item] += n
        else:
            self.bag[item] = 1
        print('{p} gets {i} x {n}'.format(p=self.name, n=n, i=item))

    def remove_item(self, item, n):
        if self.bag[item] > n + 1:
            self.bag[item] -= n
        elif self.bag[item] == n:
            del self.bag[item]
        else:
            del self.bag[item]
            print('Player-remove_item: negative number -> 0')
        print('{p} drops {i} x {n}'.format(p=self.name, n=n, i=item))

    def add_skills(self, skill_names):
        for skill_name in skill_names:
            self.SKB.append(skill_name)

    def increase_level(self, n):
        self.level += n
        print('{p} level is increased by {n}'.format(p=self.name, n=n))



    def report_status(self):
        print('[{n}] has [{hp}] HP left'.format(n=self.name, hp=self.HP))

    # def use_skill(self, skill_name, enemy):
    #     # skill = DATA_SKILL[skill_name](self, projectile)
    #     # skill.cast_on(enemy)
    #
    #     return DATA_SKILL[skill_name](self, enemy)


class Boss(Hero):
    def __init__(self, name, type_):
        super(Boss, self).__init__(name, type_)
        self.loot = {}
        self.dice = 10

        self.at_creation()

    def at_creation(self):
        self.add_skills(['punch', 'heal'])
        self.add_item('N95', 1)
        self.loot = {
            'EXP': 10,
            'money': 100,
            'item_dict': self.bag
        }

level_exp = {
    1: 20,
    2: 40,
    3: 80,
    4: 160
}

class Player(Hero):
    def __init__(self, name, type_):
        super(Player, self).__init__(name, type_)
        # self.isBanned = False

        self.dice = 20
        self.money = 0


        self.at_creation()

    def at_creation(self):
        self.add_skills(['punch'])

    def change_name(self, new_name):
        self.name = new_name

    def add_money(self, amount):
        self.money += amount
        print('{p} gets {m} money'.format(p=self.name, m=amount))



    def report_wealth(self):
        print('{p} has {e} EXP, {m} money'.format(
            p=self.name,
            e=self.EXP,
            m=self.money
        ))

        print('Bag:\n-----------')
        if self.bag:
            for item in self.bag.keys():
                print('{i} x {n}'.format(i=item, n=self.bag[item]))
        else:
            print('Empty')
        print('-----------')
