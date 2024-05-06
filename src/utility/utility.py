from random import randrange
from time import sleep


def random_sleep(min_sec: float, max_sec: float) -> None:
    sleep(randrange(int(min_sec * 1000), int(max_sec * 1000)) / 1000)
