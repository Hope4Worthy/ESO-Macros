import pynput
import time

mouse = pynput.mouse.Controller()
key = pynput.keyboard.Controller()

# wait times #
LA_wait_time = 0.40
global_wait_time = 0.58
cycle_time = LA_wait_time + global_wait_time
bar_swap_wait = 0.25

# ult parameters #
ult_correction_factor = 1.10
ult_per_cycle = 3 * cycle_time * ult_correction_factor
ult_cost = 70
ult_per_swap = 3 * bar_swap_wait
potion_gain = 20
current_ult = ult_cost

# loop parameters #
num_cycles = 185
execute = num_cycles * 0.75
igonre_dots = num_cycles * 0.85

# counters #
merciless_counter = 1 # Merciless Resolve
current_bar = 1 # 1 - front | 2 - back
potion_counter = 45
cycle_counter = 0
skill_block_1 = 20
skill_block_2 = 12
skill_block_3 = 22


def set_counters():
    global skill_block_1, skill_block_2, skill_block_3, merciless_counter, cycle_counter, num_cycles, potion_counter, current_ult, ult_per_cycle, ult_cost
    skill_block_1 += 1
    skill_block_2 += 1
    skill_block_3 += 1
    merciless_counter += 1

    potion_counter += cycle_time
    current_ult += ult_per_cycle

    cycle_counter += 1
    if(cycle_counter >= num_cycles):
        key.press('a')
        time.sleep(2)
        key.release('a')
        exit()

def cast(skill, bar):
    global current_bar,bar_swap_wait,potion_counter, current_ult, ult_per_swap, potion_gain,merciless_counter
    if current_bar != bar:
        key.tap('t')
        current_bar = bar
        potion_counter += bar_swap_wait
        current_ult += ult_per_swap
        time.sleep(bar_swap_wait)

    # potion #
    if(potion_counter >= 45) :
        key.tap('q')
        current_ult += potion_gain
        potion_counter = 0

    # synergy #
    key.tap('x')

    mouse.click(pynput.mouse.Button.left)
    time.sleep(LA_wait_time)

    key.tap(skill)

    set_counters()

    if(skill == 'r'):
        current_ult = 0
    if(skill == '2' and bar == 1):
        merciless_counter = 0
    time.sleep(global_wait_time)

def channel_cast(skill, bar, channel_time):
    global current_bar,bar_swap_wait,potion_counter, current_ult, ult_per_swap, potion_gain,merciless_counter
    if current_bar != bar:
        key.tap('t')
        current_bar = bar
        potion_counter += bar_swap_wait
        current_ult += ult_per_swap
        time.sleep(bar_swap_wait)

    # potion #
    if(potion_counter >= 45) :
        key.tap('q')
        current_ult += potion_gain
        potion_counter = 0

    # synergy #
    key.tap('x')

    mouse.click(pynput.mouse.Button.left)
    time.sleep(LA_wait_time)

    key.tap(skill)
    time.sleep(channel_time)

    set_counters()

    if(skill == 'r'):
        current_ult = 0
    if(skill == '2' and bar == 1):
        merciless_counter = 0
    time.sleep(global_wait_time)
def wobble():
    wobble_time = 0.05
    key.press('w')
    time.sleep(wobble_time)
    key.release('w')
    key.press('s')
    time.sleep(wobble_time)
    key.release('s')
time.sleep(2) # setup time

for i in range(num_cycles):

    # cast skills #
    if((merciless_counter >= 5) and (cycle_counter < execute)):
        if((current_ult > ult_cost)):
            cast('r', 1)
        cast('2', 1)
    if(skill_block_1 >= 19):
        cast('3', 1)
        cast('4', 1)
        skill_block_1 = 0
    if((skill_block_2) >= 11 and (cycle_counter < igonre_dots)):
        cast('1', 2)
        time.sleep(0.05)
        cast('2', 2)
        wobble()
        skill_block_2 = 0
    if((skill_block_3) >= 20 and (cycle_counter < igonre_dots)):
        cast('3', 2)
        cast('4', 2)
        time.sleep(0.05)
        cast('5', 2)
        skill_block_3 = 0
    if(cycle_counter >= execute):
        if(merciless_counter >= 10):
            if((current_ult > ult_cost)):
                cast('r', 1)
            cast('1', 1)
            merciless_counter = 0
        cast('5', 1)
    else:
        cast('1', 1)

# put mouse here before running incase you have to cancel to avoid messing up the program
#
#
#
#
#