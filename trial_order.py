#------This script generates a random order of stimuli with the rules of the predefined methods-----

#importing random class
import random
import json
# global variables to be manipulated
stimulus_set = []
relay = 0

# FP and HN groups separated for avoiding contingency and feature integration confounds
fp_con_list = [["FFFFF","no_conflict", "1"],["PPPPP","no_conflict", "9"]]
fp_inc_list = [["FPPPF","low_conflict", "9"],["PFFFP","low_conflict", "1"],["FFPFF","high_conflict", "9"],["PPFPP","high_conflict", "1"]]
hn_con_list = [["HHHHH","no_conflict", "2"],["NNNNN","no_conflict", "8"]]
hn_inc_list = [["HNNNH","low_conflict", "8"],["NHHHN","low_conflict", "2"],["HHNHH","high_conflict", "8"],["NNHNN","high_conflict", "2"]]

# Grouping congruent and incongruent stimuli together in the same stimulus group
fp_group = [fp_con_list,fp_inc_list]
hn_group = [hn_con_list,hn_inc_list]

def stimulus_finder(group):
    global stimulus_set
    congruency = random.randint(0,len(group)-1) #randomly choosing from congruent or incongruent stimuli (50-50%)
    stimulus = random.randint(0,len(group[congruency])-1) # randomly choosing a stimulus from the list (25% low conflict, 25% high conflict, 50% no conflict)
    stimulus_set.append(group[congruency][stimulus])


def group_relay():
    # kindergarden way to switch between fp and hn groups
    global relay
    if relay == 0:
        stimulus_finder(fp_group)
        relay = 1
    else:
        stimulus_finder(hn_group)
        relay = 0

def set_factory(times):
    stimulus_set = []
    for i in range(times):
        group_relay()
trial_rate = []
trial_count=576
def factor():
    global trial_rate
    global trial_count
    set_factory(trial_count)
    nc_count = 0
    lc_count = 0
    hc_count = 0
    for i in stimulus_set:
        nc_count += i.count("no_conflict")
        lc_count += i.count("low_conflict")
        hc_count += i.count("high_conflict")
    nc = nc_count/trial_count
    lc = lc_count/trial_count
    hc = hc_count/trial_count
    trial_rate = [nc,lc,hc]

match_count = 0
while True:
    if trial_rate==[0.5,0.25,0.25]:
        match_count +=1
        print("Match found: {}".format(match_count))
        with open("trials.json",'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["trials"].append(stimulus_set)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file)

    stimulus_set = []
    factor()
