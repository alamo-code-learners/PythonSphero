# -*- coding: utf-8 -*-
from kulka import Kulka
import os

"""
Sphero jest zawstydzone! Uruchom ten program i zobacz jak kuleczka
się czerwieni.
"""


ADDR = os.environ["SPHERO"]


with Kulka(ADDR) as kulka:
    for czerwony in range(0, 255, 20):
        kulka.set_rgb(czerwony, 0, 0)

print "koniec."
