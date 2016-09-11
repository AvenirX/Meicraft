"""
Skills
"""
from Effect import *


class Skill:
    def __init__(self, caster=None, phase_type='', mp_cost=0, n=-1, alias='', key=''):
        self.caster = caster
        self.mp_cost = mp_cost
        self.phase_type = phase_type
        self.n = n
        self.alias = alias
        self.key = key

        self.target = ''

    def is_available(self):
        return self.caster.MP - self.mp_cost >= 0 and self.n

    def record_move(self):
        self.caster.last_move = self


def the_skill(skill_id):
    """
    Skill caller
    :param skill_id: string currently skill_name
    :return: the skill class
    """
    return globals()['Skill_' + skill_id]


class Skill_prep(Skill):
    def __init__(self, caster, phase_type='P',
                 mp_cost=-1, alias="蓄", key='P'):

        super(Skill_prep, self)\
            .__init__(caster=caster, phase_type=phase_type, mp_cost=mp_cost, alias=alias, key=key)

    def cast(self, *args):
        self.record_move()
        self.caster.set_phase(self.phase_type)
        # toImpr new function create_potion in Effect?
        potion = Potion(skill=self, delta_mp=self.mp_cost*(-1))
        potion.deliver()

        return

    def __repr__(self):
        return '{alias}'.format(alias=self.alias)


class Skill_attack(Skill):
    def __init__(self, caster, phase_type='A',
                 mp_cost=1, damage=1, alias="戳", key='A'):

        super(Skill_attack, self)\
            .__init__(caster=caster, mp_cost=mp_cost, phase_type=phase_type, alias=alias, key=key)
        self.damage = damage

    def cast(self, target):
        self.target = target
        self.record_move()
        self.caster.set_phase(self.phase_type)

        potion = Potion(skill=self, delta_mp=self.mp_cost*(-1))
        arrow = Arrow(skill=self, victim=target, delta_hp=self.damage * (-1))

        potion.deliver()
        arrow.deliver()

        return

    def __repr__(self):
        return '{alias}->{target}'.format(alias=self.alias, target=self.target)


class Skill_defend(Skill):
    def __init__(self, caster, phase_type='D',
                 n=2, alias="挡", key='D'):
        super(Skill_defend, self)\
            .__init__(caster=caster, phase_type=phase_type, n=n, alias=alias, key=key)

    def cast(self, *args):
        self.record_move()
        self.n -= 1
        self.caster.set_phase(self.phase_type)

        return

    def __repr__(self):
        return '{alias}'.format(alias=self.alias, target=self.target)


# Customized skills
# toadd new function skills
class Skill_attack2(Skill_attack):
    def __init__(self, caster,
                 mp_cost=2, damage=2, alias='大力戳', key='A2'):
        """
        Inherit skill from Skill_attack

        :param caster: Fighter
        :param mp_cost: int mp cost for cast this skill
        :param damage: int hp damage of the skill
        :param alias: string skill name
        :param key: string skill key for user input to select, and generate available_skills
        """
        super(Skill_attack2, self)\
            .__init__(caster=caster, mp_cost=mp_cost, damage=damage, alias=alias, key=key)

    def __repr__(self):
        return '{alias}->{target} !!'.format(alias=self.alias, target=self.target)