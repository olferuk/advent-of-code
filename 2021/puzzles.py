import requests
import numpy as np


def download_puzzle(day: int, year: int = 2015) -> str:
    headers = {
        "cookie": (
            'session=53616c7465645f5f59ee1a2b43d34f4327c8c09d04478ed9e8acd1782d780899f0d695b78b0f53d303783ae43df6384c'
        )
    }
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", headers=headers
    )
    return response.text


def load(day: int) -> str:
    with open(f'data/{day:02d}.txt') as f:
        data = f.read()
    return data

def load_lines(day: int) -> str:
    data = load(day)
    return data.strip().split('\n')

def load_tokens(day: int, sep: str='\n') -> str:
    data = load(day)
    return data.strip().split(sep)

def load_array(day: int) -> str:
    data = load(day)
    return np.array([line.split() for line in data.strip().split('\n')])
