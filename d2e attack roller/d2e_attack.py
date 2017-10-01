from d2e_die import dieside, die
from d2e_mods import attack_mod, surge_mod
from d2e_attack_result import attack_result


class attack:

    def __init__(self, attack_dice, defense_dice, attack_range, attack_mod=[], surge_abilities=[], sorcery_first=True):
        self.attack_dice = []
        self.defense_dice = []
        self.attack_mod = []
        self.surge_abilities = []
        self.attack_range = attack_range
        self.sorcery_first = sorcery_first

        for i in range(len(attack_dice)):
            tmp_die = die(attack_dice[i])
            self.attack_dice.append(tmp_die)

        for i in range(len(defense_dice)):
            tmp_die = die(defense_dice[i])
            self.defense_dice.append(tmp_die)

        for i in range(len(attack_mod)):
            self.attack_mod.append(attack_mod[i])

        for i in range(len(surge_abilities)):
            self.surge_abilities.append(surge_abilities[i])

    def RollAttack(self, attack_override=[], defense_override=[]):
        ###########################################
        # Step 1: Declare Target & Weapon
        ###########################################
        # This doesn't really have to happen, let's load existing attack mods,
        # surge mods, and make the attack_result object
        att_res = attack_result()

        cum_mod = attack_mod()
        for i in self.attack_mod:
            cum_mod += i

        surge_ability_list = []
        for i in self.surge_abilities:
            surge_ability_list.append(i)
            cum_mod += i  # NOTE: This is for testing only, disable this

        print("Printing Cumulative Mod")
        attack_mod.PrintMod(cum_mod)

        ###########################################
        # Step 2: Roll Dice
        ###########################################

        att_cum = dieside()

        if not attack_override:
            #  If attack_override is empty, then actually roll
            for i in range(len(self.attack_dice)):
                att_cum += die.roll(self.attack_dice[i])
        else:
            #  Don't do a random roll
            for i in range(len(self.attack_dice)):
                att_cum += die.roll(self.attack_dice[i], attack_override[i])

        att_res.raw_attack = att_cum
        def_cum = dieside()

        if not defense_override:
            #  If defense_override is empty, then actually roll
            for i in range(len(self.defense_dice)):
                def_cum += die.roll(self.defense_dice[i])
        else:
            #  Don't do a random roll
            for i in range(len(self.defense_dice)):
                def_cum += die.roll(self.defense_dice[i], defense_override[i])

        att_res.raw_defense = def_cum

        return att_res
        ###########################################
        # Step 3: Check Range, Use sorcery/surge abilities that grant range if nec.
        ###########################################
        
        range_needed = self.attack_range - (cum_mod.range + att_cum.range)

        while range_needed > 0:
            # Attack will miss without sorcery/surge abilities

            if self.sorcery_first==True:

                if cum_mod.sorcery > range_needed:
                    # spend range_needed sorcery, update range_needed
                    range_needed = -1
                elif cum_mod.sorcery > 0:
                    # spend cum_mod.sorcery, update range_needed
                    range_needed = -1
                else:
                    # no sorcery, break
                    range_needed = -1
            else:
                range_needed = -1

            


        ###########################################
        # Step 4: Use surge abilities
        ###########################################

        ###########################################
        # Step 5: Calculate results
        ###########################################

        ###########################################
        # Step 6: Return attack_result object
        ###########################################
