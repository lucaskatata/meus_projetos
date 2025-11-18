# %%
import pandas as pd
from pathlib import Path

pasta = Path(r"C:\Users\lkbio\Downloads\backup-31")

nf = '219367'

for i, c in enumerate(pasta.iterdir()):
    n = c.name.split('-')[0]
    # print(n)
    if nf in n:
        print(f'Posição {i}\n{c}')
