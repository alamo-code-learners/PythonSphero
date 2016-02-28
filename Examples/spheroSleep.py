from kulka import Kulka
import os


ADDR = os.environ["SPHERO"]


with Kulka(ADDR) as kulka:
    kulka.sleep()
