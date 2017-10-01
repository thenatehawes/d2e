from d2e_die import die, dieside

print("#####################################")
print("# Checking Classes: die, dieside")
print("#####################################")
cum_result = True
test = 0
# Add w/ an uninitialized
a_1 = dieside()
a_2 = dieside(side_range=1, heart=2, surge=1, shield=0, miss=False)
a_ans = dieside(side_range=1, heart=2, surge=1, shield=0, miss=False)
a_result = (a_1 + a_2) == a_ans
print("Test", str(test) + ":", str(a_result))
test += 1
cum_result = cum_result and a_result

# Add w/ a miss
b_1 = dieside(miss=True)
b_2 = dieside(side_range=1, heart=2, surge=1, shield=0, miss=False)
b_ans = dieside(side_range=0, heart=0, surge=0, shield=0, miss=True)
b_result = (b_1 + b_2) == b_ans
print("Test", str(test) + ":", str(b_result))
test += 1
cum_result = cum_result and b_result

# Try another add including some negative numbers
c_1 = dieside(side_range=2, heart=-1, surge=5, shield=-2, miss=False)
c_2 = dieside(side_range=1, heart=2, surge=1, shield=0, miss=False)
c_ans = dieside(side_range=3, heart=1, surge=6, shield=-2, miss=False)
c_result = (c_1 + c_2) == c_ans
print("Test", str(test) + ":", str(c_result))
test += 1
cum_result = cum_result and c_result

# Try a plus-equal
b_2 += c_1
d_ans = dieside(side_range=3, heart=1, surge=6, shield=-2, miss=False)
d_result = b_2 == d_ans
print("Test", str(test) + ":", str(d_result))
test += 1
cum_result = cum_result and d_result

# Try a subtraction
e_ans = dieside(side_range=0, heart=0, surge=0, shield=-0, miss=False)
e_result = (c_2 - a_2) == e_ans
print("Test", str(test) + ":", str(e_result))
test += 1
cum_result = cum_result and e_result

# -= with a miss
f_ans = dieside(side_range=0, heart=0, surge=0, shield=-0, miss=True)
b_1 -= a_2
f_result = b_1 == f_ans
print("Test", str(test) + ":", str(f_result))
test += 1
cum_result = cum_result and f_result

# Try a wrong die string
try:
    d_4 = die('spam')
    result = False
except ValueError:
    result = True

print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

# roll a die
d_1 = die('red')
d_2 = die('black')

roll_output = d_1.roll(0)
answer = dieside(0, 2, 0, 0, False)
result = roll_output == answer
print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

roll_output = die.roll(d_2, 2)
answer = dieside(0, 0, 0, 2, False)
result = roll_output == answer
print("Test", str(test) + ":", str(result))
test += 1
cum_result = cum_result and result

shield_cum = 0
N = 5000
for i in range(N):
    side = d_2.roll()
    shield_cum += side.shield

shield_cum = shield_cum / N

if (shield_cum > 2.2333333) or (shield_cum < 2.1):
    print('Random test failure expected 2.1667, actual', shield_cum)
    result = False
else:
    result = True

print("Test", str(test) + ":", str(result), 'mean:', shield_cum)
test += 1
cum_result = cum_result and result

if cum_result:
    print('All Tests Passed')
else:
    print('Not All Tests Passed')