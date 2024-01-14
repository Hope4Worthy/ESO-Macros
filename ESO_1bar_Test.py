import pynput
import time

mouse = pynput.mouse.Controller()
key = pynput.keyboard.Controller()

# loop parameters #
num_cycles = 250
execute = num_cycles * 0.75

# wait times #
LA_wait_time = 0.20
global_wait_time = 0.80
cycle_time = LA_wait_time + global_wait_time
potion_cycle_time = 45 / cycle_time

# ult parameters #
ult_correction_factor = 0.98
ult_per_cycle = 3 * cycle_time * ult_correction_factor
ult_cost = 70
potion_gain = 20
current_ult = ult_cost


# cast flags #
cast_flag_2 = False 
cast_flag_3 = False 
cast_flag_4 = False 
cast_flag_r = False 

# counters #
counter_1 = 1 # Merciless Resolve

time.sleep(2) # setup time

for i in range(num_cycles):

      # potion #
    if(i % potion_cycle_time == 0) :
        key.tap('q')
        current_ult += potion_gain

    # synergy #
    key.tap('x')

    # set cast flags #
    if(counter_1 % 6 == 0):
        cast_flag_2 = True
        counter_1 = 1
    if(i % 19 == 0):
        cast_flag_3 = True
    if(i % 19 == 0):
        cast_flag_4 = True
    if(current_ult >= ult_cost):
        cast_flag_r = True

    # light attack #
    mouse.click(pynput.mouse.Button.left)
    time.sleep(LA_wait_time)
    
    # cast skills #
    if(cast_flag_r and cast_flag_2):
        key.tap('r')
        cast_flag_r = False
        current_ult = 0
    elif(cast_flag_2):
        key.tap('2')
        cast_flag_2 = False
    elif(cast_flag_3):
        key.tap('3')
        cast_flag_3 = False
        counter_1 += 1
    elif(cast_flag_4):
        key.tap('4')
        cast_flag_4 = False
        counter_1 += 1
    elif(i > execute):
        key.tap('5')
        counter_1 += 1
    else:
        key.tap('1')
        counter_1 += 1

    # wait for global cooldown
    current_ult += ult_per_cycle
    time.sleep(global_wait_time)
