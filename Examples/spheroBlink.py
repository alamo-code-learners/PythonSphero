from kulka import Kulka
import random
import time
import os


ADDR = os.environ["SPHERO"]


def main():
    with Kulka(ADDR) as kulka:
        kulka.set_inactivity_timeout(3600)
        blink_rate = 1

        for _ in range(5):
            blink_rate = abs(blink_rate - 0.05)
            kulka.set_rgb(random.randint(0, 255), random.randint(0, 255),
                          random.randint(0, 255))
            time.sleep(blink_rate)
            kulka.set_rgb(0, 0, 0)
            time.sleep(blink_rate)

main()
