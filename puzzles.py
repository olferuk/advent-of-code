from typing import List

import numpy as np


def load(day: int) -> str:
    with open(f'data/{day:02d}.txt') as f:
        data = f.read()
    return data

def load_lines(day: int) -> List[str]:
    data = load(day)
    return data.strip().split('\n')

def load_tokens(day: int, sep: str='\n') -> List[str]:
    data = load(day)
    return data.strip().split(sep)

def load_array(day: int) -> np.ndarray:
    data = load(day)
    return np.array([line.split() for line in data.strip().split('\n')])
