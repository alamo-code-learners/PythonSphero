from kulka import Kulka
import time
import os


ADDR = os.environ["SPHERO"]


def main():
    with Kulka(ADDR) as kulka:
        blink_rate = 0.001

        for _ in range(10):
            kulka.set_rgb(255, 255, 255)
            time.sleep(blink_rate)
            kulka.set_rgb(0, 0, 0)
            time.sleep(blink_rate)


main()
