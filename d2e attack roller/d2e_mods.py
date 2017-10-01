from d2e_die import base_stats, dieside
import copy

class attack_mod(base_stats):
    """Class which defines attack modifier objects"""

    def __init__(self, mod_range=0, heart=0, surge=0, shield=0, sorcery=0, stealthy=0, status_effect=None, attack_effect=None):
        base_stats.__init__(self, mod_range, heart, surge, shield)
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
        output = base_stats.__add__(self, other)
        output.__class__ = attack_mod

        if type(other) is dieside:
            output.sorcery = self.sorcery
            output.stealthy = self.stealthy
            output.status_effect = self.status_effect
            output.attack_effect = self.attack_effect
            return output

        output.sorcery = self.sorcery + other.sorcery
        output.stealthy = self.stealthy + other.stealthy
        output.status_effect = self.status_effect + other.status_effect
        output.attack_effect = self.attack_effect + other.attack_effect

        return output

    def __iadd__(self, other):
        base_stats.__iadd__(self, other)

        if type(other) is dieside:
            return self

        self.sorcery += self.sorcery
        self.stealthy += self.stealthy
        self.status_effect = self.status_effect + other.status_effect
        self.attack_effect = self.attack_effect + other.attack_effect

        return self

    def __sub__(self, other):
        output = base_stats.__sub__(self, other)
        output.__class__ = attack_mod

        if type(other) is dieside:
            return output

        output.sorcery = self.sorcery - other.sorcery
        output.stealthy = self.stealthy - other.stealthy
        output.attack_effect = copy.copy(self.attack_effect)
        output.status_effect = copy.copy(self.status_effect)

        if other.status_effect:
            for i in other.status_effect:
                if i in output.status_effect:
                    output.status_effect.remove(i)

        if other.attack_effect:
            for i in other.attack_effect:
                if i in output.attack_effect:
                    output.attack_effect.remove(i)

        return output

    def __isub__(self, other):
        base_stats.__isub__(self, other)

        if type(other) is dieside:
            return self

        self.sorcery -= other.sorcery
        self.stealthy -= other.sorcery

        if other.status_effect:
            for i in other.status_effect:
                if i in self.status_effect:
                    self.status_effect.remove(i)

        if other.attack_effect:
            for i in other.attack_effect:
                if i in self.attack_effect:
                    self.attack_effect.remove(i)

        return self

    def PrintMod(self):
        print('Mod Range:', self.range)
        print('Mod Heart:', self.heart)
        print('Mod Surge:', self.surge)
        print('Mod Shield:', self.shield)
        print('Sorcery:', self.sorcery)
        print('Stealthy:', self.stealthy)
        print('Mod Status:', self.status_effect)
        print('Attack Effect:', self.attack_effect)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class surge_mod(attack_mod):

    def __init__(self, surge_cost, mod_range=0, heart=0, surge=0, shield=0, sorcery=0, stealthy=0, status_effect=None, attack_effect=None):
        self.surge_cost = surge_cost
        attack_mod.__init__(self, mod_range=mod_range, heart=heart, surge=surge, shield=shield, sorcery=sorcery, stealthy=stealthy, status_effect=status_effect, attack_effect=attack_effect)

    def PrintMod(self):
        print('Surge Cost:', self.surge_cost)
        super(surge_mod, self).PrintMod(self)

    def __add__(self, other):
        output = attack_mod.__add__(self, other)

        if type(other) is surge_mod:
            output.__class__ = surge_mod
            output.surge_cost = self.surge_cost + other.surge_cost

    def __iadd__(self, other):
        attack_mod.__iadd__(self, other)
        if type(other) is surge_mod:
            self.surge_cost += other.surge_cost
