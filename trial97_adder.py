#importing random class and pandas
import random
import json
import pandas as pd
import numpy as np
import re

conflict_types ={
"low_conflict": [["HNNNH","low_conflict", "8"],["NHHHN","low_conflict", "2"]],
"high_conflict": [["HHNHH","high_conflict", "8"],["NNHNN","high_conflict", "2"]]
}

#read trial json
trials_json=pd.read_json("trials.json")

# iterate through all the blocks
for block in trials_json.trials:
	current_block = block
	block_df = pd.DataFrame(current_block, columns=['stimulus','congruency', 'response'])
	block_df['previous_congruency'] = block_df['congruency'].shift()
	block_df["conflict_pair"]=block_df["previous_congruency"]+"-"+block_df["congruency"]
	pair_counts = block_df["conflict_pair"].value_counts()
	match = re.match(r"(.*?)-", pair_counts.idxmin())
	if match:
		conflict_group = match.group(1)
	current_block.insert(0,conflict_types[conflict_group][random.randint(0,1)])
	with open("trials97.json",'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                file_data["trials"].append(current_block)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file)
