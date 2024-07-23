from typing import Callable

from art import text2art
from datetime import datetime
from os import system, name
from time import time, sleep
from math import floor

clear: Callable[[], int] = lambda: system("cls" if name == "nt" else "clear")


def main():
    while True:
        clear()
        now = datetime.fromtimestamp(floor(time()))
        print(text2art(datetime.strftime(now, "%H:%M:%S")))
        sleep(1)


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        clear()
        exit()
