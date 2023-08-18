import subprocess
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f'{CURRENT_DIR}/../log', exist_ok=True)

GRAPH_DIR="~/data"
graphs = ["Epinions1", "Slashdot", "DBLP", "Youtube"]
if __name__ == '__main__':
    t = 1024
    for g in graphs:
        out_file = f"{CURRENT_DIR}/../log/{g}_lb{t}.txt"
        in_file = f"{GRAPH_DIR}/{g}_sym.bin"
        print(g)
        cmd = f"{CURRENT_DIR}/../bin/construct_index {in_file} a.out >> {out_file}"
        subprocess.call(cmd, shell=True)