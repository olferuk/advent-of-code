import requests


def download_puzzle(day: int, year: int = 2015) -> str:
    headers = {
        "cookie": (
            "session=53616c7465645f5ff03d703ef925a9ab24f0b63de34f0e158adf5c3daa11fccbd8b42a4ed6fc2b4"
            "df3642de5f8c3be5e"
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
