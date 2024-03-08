from time import sleep
from icecream import ic


if __name__ == '__main__':
    counter: int = 0

    while True:
        counter += 1
        ic(counter)

        sleep(1)
