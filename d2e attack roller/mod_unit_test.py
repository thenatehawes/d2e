from d2e_mods import attack_mod, surge_mod
from d2e_die import dieside

print("#####################################")
print("# Checking Classes: attack_mod, surge_mod")
print("#####################################")
cum_result = True
test = 0

# Add some attack_mods
mod1 = attack_mod(heart=2, mod_range=2)
mod2 = attack_mod(heart=1, surge=1)
mod3 = attack_mod(shield=-1, attack_effect=['blast'])
mod4 = attack_mod(attack_effect=['breath'])
mod5 = attack_mod(heart=3, attack_effect=['blast'])
mod6 = attack_mod(status_effect=['poison'])
mod7 = attack_mod(mod_range=4, status_effect=['immobilized'])

smod1 = surge_mod(1, heart=2)
smod2 = surge_mod(2, status_effect=['weakened'])

# Test 1
answer = attack_mod(heart=3, mod_range=2, surge=1)
result = (mod1 + mod2) == answer
print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

# Test 2
answer = attack_mod(shield=-1, attack_effect=['blast', 'breath'])
result = (mod3 + mod4) == answer
print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

# Test 3
answer = attack_mod(heart=-3, shield=-1, attack_effect=[])
result = (mod3 - mod5) == answer
print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

# Test 4
testmod = attack_mod()
testmod += mod1
testmod += mod6
testmod += mod7

answer = attack_mod(heart=2, mod_range=6, status_effect=['poison', 'immobilized'])
result = (testmod) == answer
print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

# Test 5
testmod += smod2

answer = attack_mod(heart=2, mod_range=6, status_effect=['poison', 'immobilized', 'weakened'])
result = (testmod) == answer
print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

die1 = dieside(side_range=2, heart=3, surge=1)

answer = attack_mod(heart=5, mod_range=4, surge=1)
result = (mod1 + die1) == answer
print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

test = die1 + mod1  # mod1 + die1 works
attack_mod.PrintMod(test)
# mod3 = mod1 + mod2

# print(mod3.heart)

# smod1 = surge_mod(1, heart=3)

# mod4 = mod1 + smod1
# mod5 = smod1 + mod1
# # print(mod5.surge_cost)
