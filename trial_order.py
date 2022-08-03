import random

stimulus_set = []
relay = 0
fp_con_list = [["FFFFF","no_conflict", "1"],["PPPPP","no_conflict", "9"]]
fp_inc_list = [["FPPPF","low_conflict", "9"],["PFFFP","low_conflict", "1"],["FFPFF","high_conflict", "9"],["PPFPP","high_conflict", "1"]]
hn_con_list = [["HHHHH","no_conflict", "2"],["NNNNN","no_conflict", "8"]]
hn_inc_list = [["HNNNH","low_conflict", "8"],["NHHHN","low_conflict", "2"],["HHNHH","high_conflict", "8"],["NNHNN","high_conflict", "2"]]

fp_group = [fp_con_list,fp_inc_list]
hn_group = [hn_con_list,hn_inc_list]

print(len(hn_inc_list))
def stimulus_finder(group):
    global stimulus_set
    congruency = random.randint(0,len(group)-1)
    stimulus = randqom.randint(0,len(group[congruency])-1)
    stimulus_set.append(group[congruency][stimulus])


def group_relay():
    global relay
    if relay == 0:
        stimulus_finder(fp_group)
        relay = 1
    else:
        stimulus_finder(hn_group)
        relay = 0

def set_factory(total):
    for i in range(total):
        group_relay()

set_factory(588)
print(stimulus_set)
