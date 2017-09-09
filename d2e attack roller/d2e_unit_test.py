from d2e_attack import attack
from d2e_die import dieside
from d2e_mods import attack_mod, surge_mod

attack_dice = ['blue', 'red']
defense_dice = ['gray', 'brown']

first_attack = attack(attack_dice, defense_dice, 3)

att_res = attack.RollAttack(first_attack)

print('#################')
print('# Random Rolls 1')
print('#################')
print('')
print('#--Attack--#')
dieside.PrintDie(att_res.raw_attack)
print('')
print('#--Defense--#')
dieside.PrintDie(att_res.raw_defense)
print('')

attack_mod1 = attack_mod(heart=3)
attack_mod2 = attack_mod(status_effect=['poison'])
attack_mod3 = attack_mod(shield=-2)
attack_mod4 = attack_mod(sorcery=2)
attack_mods = [attack_mod1, attack_mod2, attack_mod3, attack_mod4]

surge_mod1 = surge_mod(1, shield=-2)
surge_mod2 = surge_mod(2, heart=4)
surge_mod3 = surge_mod(1, status_effect=['stunned'], attack_effect=['blast'])
surge_mods = [surge_mod1, surge_mod2, surge_mod3]

second_attack = attack(attack_dice, defense_dice, 3, attack_mods, surge_mods)

att_res = attack.RollAttack(second_attack)

print('#################')
print('# Random Rolls 2')
print('#################')
print('')
print('#--Attack--#')
dieside.PrintDie(att_res.raw_attack)
print('')
print('#--Defense--#')
dieside.PrintDie(att_res.raw_defense)
