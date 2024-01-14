import pynput
import time

mouse = pynput.mouse.Controller()
key = pynput.keyboard.Controller()

# wait times #
LA_wait_time = 0.25
global_wait_time = 0.85
cycle_time = LA_wait_time + global_wait_time
bar_swap_wait = 0.35

# ult parameters #
ult_correction_factor = 0.98
ult_per_cycle = 3 * cycle_time * ult_correction_factor
ult_cost = 70
potion_gain = 20
current_ult = ult_cost

# loop parameters #
run_time = 3.66 # in minutes
num_cycles = int((run_time*60) / cycle_time)
execute = num_cycles * 0.75

# cast flags #
cast_flag_2f = False 
cast_flag_3f = False 
cast_flag_4f = False 
cast_flag_r = False 

cast_flag_1b = False 
cast_flag_2b = False 
cast_flag_3b = False 
cast_flag_4b = False 
cast_flag_5b = False 

# counters #
counter_1 = 1 # Merciless Resolve
current_bar = 1 # 1 - front | 2 - back
potion_counter = 45

def cast(skill, bar):
    global current_bar
    global bar_swap_wait
    global potion_counter
    global counter_1
    if current_bar != bar:
        key.tap('t')
        current_bar = bar
        potion_counter += bar_swap_wait
        time.sleep(bar_swap_wait)
    counter_1 += 1
    key.tap(skill)

time.sleep(2) # setup time

for i in range(num_cycles):

    # potion #
    if(potion_counter >= 45) :
        key.tap('q')
        current_ult += potion_gain
        potion_counter = 0

    # synergy #
    key.tap('x')

    # light attack #
    mouse.click(pynput.mouse.Button.left)
    time.sleep(LA_wait_time)

    # set cast flags #
    if(counter_1 % 6 == 0): #merciless resolve
        cast_flag_2f = True
        counter_1 = 1
    if(i % 18 == 0):
        cast_flag_3f = True
    if(i % 18 == 0):
        cast_flag_4f = True
    if(current_ult >= ult_cost):
        cast_flag_r = True
    if(i % 10 == 0):
        cast_flag_1b = True
    if(i % 10 == 0):
        cast_flag_2b = True
    if(i % 18 == 0):
        cast_flag_3b = True
    if(i % 18 == 0):
        cast_flag_4b = True
    if(i % 18 == 0):
        cast_flag_5b = True
    
    # cast skills #
    if(cast_flag_r and cast_flag_2f):
        cast('r', 1)
        cast_flag_r = False
        current_ult = 0
        counter_1 -= 1
    elif(cast_flag_2f):
        cast('2', 1)
        cast_flag_2f = False
        counter_1 -= 1
    elif(cast_flag_3f):
        cast('3', 1)
        cast_flag_3f = False
    elif(cast_flag_4f):
        cast('4', 1)
        cast_flag_4f = False
    elif(cast_flag_1b):
        cast('1', 2)
        cast_flag_1b = False
    elif(cast_flag_2b):
        cast('2', 2)
        cast_flag_2b = False
    elif(cast_flag_3b):
        cast('3', 2)
        cast_flag_3b = False
    elif(cast_flag_4b):
        cast('4', 2)
        cast_flag_4b = False
    elif(cast_flag_5b):
        cast('5', 2)
        cast_flag_5b = False
    elif(i > execute):
        cast('5', 1)
    else:
        cast('1', 1)

    # wait for global cooldown
    potion_counter += cycle_time
    current_ult += ult_per_cycle
    time.sleep(global_wait_time)