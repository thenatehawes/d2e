class attack_mod:
    """Class which defines attack modifier objects"""

    def __init__(self, mod_range=0, heart=0, surge=0, shield=0, sorcery=0, stealthy=0, status_effect=None, attack_effect=None):
        self.range = mod_range
        self.heart = heart
        self.surge = surge
        self.shield = shield
        self.sorcery = sorcery
        self.stealthy = stealthy
        self.status_effect = []
        self.attack_effect = []

        if status_effect:
            for i in status_effect:
                self.status_effect.append(i)

        if attack_effect:
            for i in attack_effect:
                self.attack_effect.append(i)


    def __add__(self, other):
        output = attack_mod(mod_range=(self.range + other.range),
                            heart=(self.heart + other.heart),
                            surge=(self.surge + other.surge),
                            shield=(self.shield + other.shield),
                            sorcery=(self.sorcery + other.sorcery),
                            stealthy=(self.stealthy + other.stealthy),
                            status_effect=(self.status_effect + other.status_effect),
                            attack_effect=(self.attack_effect + other.attack_effect))
        return output

    def PrintMod(self):
        print('Mod Range:', self.range)
        print('Mod Heart:', self.heart)
        print('Mod Surge:', self.surge)
        print('Mod Shield:', self.shield)
        print('Sorcery:', self.sorcery)
        print('Stealthy:', self.stealthy)
        print('Mod Status:', self.status_effect)
        print('Attack Effect:', self.attack_effect)


class surge_mod(attack_mod):

    def __init__(self, surge_cost, mod_range=0, heart=0, surge=0, shield=0, sorcery=0, stealthy=0, status_effect=None, attack_effect=None):
        self.surge_cost = surge_cost
        super(surge_mod, self).__init__(mod_range=mod_range, heart=heart, surge=surge, shield=shield, sorcery=sorcery, stealthy=stealthy, status_effect=status_effect, attack_effect=attack_effect)

    def PrintMod(self):
        print('Surge Cost:', self.surge_cost)
        super(surge_mod, self).PrintMod(self)