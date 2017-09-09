class attack_result:

    def __init__(self):
        self.raw_attack = None
        self.raw_defense = None
        self.attack_mod = None
        self.surge_mod = None
        self.final_result = None

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
    def set_raw_attack(self, dieside):
        delta = self.raw_attack - dieside  #needed to update final_result
        self.raw_attack += dieside
        # update final_result

    @raw_defense.setter
    def set_raw_defense(self, dieside):
        delta = self.raw_defense - dieside  #needed to update final_result
        self.raw_defense += dieside
        # update final_result

    @attack_mod.setter
    def set_attack_mod(self, mod):
        delta = self.attack_mod - mod  #needed to update final_result
        self.attack_mod = mod
        # update final_result


class final_result:

    def __init__(self):
        self.damage_dealt = 0
        self.surge_spent = 0
        self.surge_unspent = 0
        self.miss = False
        self.excess_range = 0
