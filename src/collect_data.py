import os
import sys
import subprocess
import re
import numpy as np
import pandas as pd
from run_example import graphs

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = f"{CURRENT_DIR}/../log"

def collect_data(file_in, key_words):
    f = open(file_in,'r')
    res = f.read()
    f.close()
    data_lines = re.findall(f"{key_words}.*", res)
    data = list(map(lambda x: eval((x.replace(" seconds", "")).split(" ")[-1]), data_lines))
    return data
if __name__ == '__main__':
    for t in [0,1,4,16,64,256,1024]:
        print(f"num bitwise={t}")
        data={}
        for key_words in ["average normal label size:", "indexing time:", "bitwise index time:", "pruned indexing time:"]:
            data[key_words]=[]
            for g in graphs:
                file_in = f"{LOG_DIR}/{g}_lb{t}.txt"
                data_= collect_data(file_in, key_words)
                data[key_words].append(data_[0])
        print(data)