# -*- encoding=utf8 -*-
__author__ = "KirisameVanilla"

from airtest.core.api import *
from airtest.core.settings import Settings
Settings.LOG_DIR = "./"

auto_setup(__file__)

if __name__=='__main__':
    touch(Template(r"tpl/tpl1698334081332.png", record_pos=(0.221, 0.053), resolution=(1600, 900)))
    time.sleep(1)
    touch(Template(r"tpl/tpl1698334112870.png", record_pos=(0.171, 0.139), resolution=(1600, 900)))
    touch(Template(r"tpl/tpl1698334829236.png", record_pos=(-0.079, 0.122), resolution=(1600, 900)),duration=10)
    while True:
        time.sleep(1)
        wait(Template(r"tpl/tpl1698334177633.png", record_pos=(0.249, 0.228), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/tpl1698334177633.png", record_pos=(0.249, 0.228), resolution=(1600, 900)))
        wait(Template(r"tpl/tpl1698334294552.png", record_pos=(0.339, 0.216), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/tpl1698334294552.png", record_pos=(0.339, 0.216), resolution=(1600, 900)))
        wait(Template(r"tpl/tpl1698335094699.png", record_pos=(-0.003, -0.182), resolution=(1600, 900)),timeout=240)
        time.sleep(1)
        touch(Template(r"tpl/tpl1698335094699.png", record_pos=(-0.003, -0.182), resolution=(1600, 900)))
        wait(Template(r"tpl/tpl1698335194421.png", record_pos=(0.002, -0.179), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/tpl1698335194421.png", record_pos=(0.002, -0.179), resolution=(1600, 900)))
        wait(Template(r"tpl/tpl1698336982880.png", record_pos=(0.393, 0.226), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/tpl1698336982880.png", record_pos=(0.393, 0.226), resolution=(1600, 900)))

        wait(Template(r"tpl/tpl1698336273325.png", record_pos=(0.363, 0.24), resolution=(1600, 900)))
        assert_not_exists(Template(r"tpl/tpl1698464484711.png", record_pos=(0.339, -0.129), resolution=(1600, 900)), "End")

        time.sleep(1)
        touch(Template(r"tpl/tpl1698336273325.png", record_pos=(0.363, 0.24), resolution=(1600, 900)))
        wait(Template(r"tpl/tpl1698335301968.png", record_pos=(0.002, 0.191), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/tpl1698335301968.png", record_pos=(0.002, 0.191), resolution=(1600, 900)))




