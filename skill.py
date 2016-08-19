import random


class Projectile:
    typeDict = {
        0: ['buff'],
        1: ['damage'],
        2: ['damage', 'buff']
    }

    def __init__(self, type_id):
        self.type_ = self.typeDict[type_id]

        if 'damage' in self.type_:
            self.damage = {
                'victim': None,
                'amount': 0
            }
            return

        if 'buff' in self.type_:
            self.buff = {
                'victim': None,
                'buffId': '',
                'remain': 0
            }
            return

    def tick(self):
        if 'damage' in self.type_:
            self.damage['victim'].decrease_hp(self.damage['amount'])
            print('[{v}] get [{dmg}] damage'.format(
                v=self.damage['victim'].name,
                dmg=self.damage['amount']))


def billing(projectile):
    # Enter
    print('Enter billing', end=' ')
    projectile.tick()


def skill_punch(caster, target, type_=1, *args, **kwargs):
    print('[{c}] uses [{s}]'.format(c=caster.name, s='Punch'))

    projectile = Projectile(type_)
    projectile.damage['victim'] = target
    projectile.damage['amount'] = caster.STR * 2 + random.randint(1, caster.dice)

    return projectile


def skill_heal(caster, target, type_=1, *args, **kwargs):
    print('[{c}] uses [{s}]'.format(c=caster.name, s='Heal'))

    projectile = Projectile(type_)
    projectile.damage['victim'] = caster
    projectile.damage['amount'] = -40

    return projectile


DATA_SKILL = {
    'punch': skill_punch,
    'heal': skill_heal
}
