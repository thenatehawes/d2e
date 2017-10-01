from d2e_mods import attack_mod
from d2e_die import dieside


class attack_result:

    def __init__(self):
        self.final_result = final_result()
        self.raw_attack = dieside()
        self.raw_defense = dieside()
        self.attack_mod = attack_mod()
        self.surge_mod = []

    @property
    def raw_attack(self):
        return self.__raw_attack

    @property
    def raw_defense(self):
        return self.__raw_defense

    @property
    def attack_mod(self):
        return self.__attack_mod

    @raw_attack.setter
    def raw_attack(self, dieside_obj):
        if hasattr(self, 'raw_attack'):
            delta = dieside_obj - self.raw_attack  #needed to update final_result
        else:
            delta = dieside_obj
        self.__raw_attack = dieside_obj
        # update final_result
        self.final_result.range += delta.range
        self.final_result.damage_dealt += delta.heart
        self.final_result.surge += delta.surge
        self.final_result.miss = delta.miss

    @raw_defense.setter
    def raw_defense(self, dieside_obj):
        if hasattr(self, 'raw_defense'):
            delta = dieside_obj - self.raw_defense  #needed to update final_result
        else:
            delta = dieside_obj
        self.__raw_defense = dieside_obj
        # update final_result
        self.final_result

    @attack_mod.setter
    def attack_mod(self, mod):
        if hasattr(self, 'attack_mod'):
            delta = mod- self.attack_mod  #needed to update final_result
        else:
            delta = mod
        self.__attack_mod = mod
        # update final_result


class final_result(attack_mod):

    def __init__(self):
        attack_mod.__init__(self)
        self.damage_dealt = 0
        self.spent_surge = 0

