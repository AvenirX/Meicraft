"""
Effect

Order:
    Projectile: Potion Arrow
    Delta: d_buff, d_mp, d_hp
    Effect: bless, curse; fill, drain; heal, damage;
"""


# Passing effects from skill to victim
class Projectile:
    def __init__(self, skill, victim=None, **deltas):
        self.skill = skill
        self.victim = victim

        self.tag = ''
        self.owner = self.skill.caster
        self.someone_may_die = False

        self.delta_hp = 0
        self.delta_mp = 0
        self.delta_buff = None

        if deltas:
            for delta, value in deltas.items():
                setattr(self, delta, value)
                if delta == 'delta_hp':
                    self.tag = 'heal' if value > 0 else 'damage'
                elif delta == 'delta_mp':
                    self.tag = 'fill' if value > 0 else 'drain'
                else:
                    print('pj asgn dlt ???')

    def deliver(self):
        if self.victim == self.skill.caster:
            category = 'potion'
        else:
            category = 'arrow'

        self.victim.incoming_projectiles[category][self.tag].append(self)


# Projectile to opponent
class Arrow(Projectile):
    def __init__(self, skill, victim, **deltas):
        super(Arrow, self).__init__(skill=skill, victim=victim, **deltas)

    def billing(self):
        if self.victim.PHASE == 'P':
            self.victim.increase_hp(self.delta_hp * 2)
            self.victim.increase_mp(self.delta_mp)

        if self.victim.PHASE == 'A':
            self.victim.increase_hp(self.delta_hp)
            self.victim.increase_mp(self.delta_mp)

        if self.victim.HP <= 0:
            self.someone_may_die = True

    def __repr__(self):
        return '{caster}({skill}) -> {target}' \
            .format(caster=self.skill.caster.name,
                    skill=self.skill.alias,
                    target=self.victim.name)


# Projectile to self
class Potion(Projectile):
    def __init__(self, skill, **deltas):
        super(Potion, self).__init__(skill=skill, victim=skill.caster, **deltas)

    def billing(self):
        self.victim.increase_mp(self.delta_mp)
        self.victim.increase_hp(self.delta_hp)

    def __repr__(self):
        return '->{caster}({skill})<-' \
            .format(caster=self.skill.caster.name, skill=self.skill.alias)


