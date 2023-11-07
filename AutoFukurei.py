# -*- encoding=utf8 -*-
__author__ = "KirisameVanilla"

from airtest.core.api import *
from airtest.core.settings import Settings
import os
Settings.LOG_DIR = "./"

auto_setup(__file__)

if __name__=='__main__':
    wait(Template(r"tpl/Special.png", record_pos=(0.221, 0.053), resolution=(1600, 900)))
    time.sleep(1)
    touch(Template(r"tpl/Special.png", record_pos=(0.221, 0.053), resolution=(1600, 900)))
    time.sleep(1)
    touch(Template(r"tpl/Fukurei.png", record_pos=(0.171, 0.139), resolution=(1600, 900)))
    wait(Template(r"tpl/Challenge.png", record_pos=(0.249, 0.228), resolution=(1600, 900)))
    time.sleep(1)
    if not exists(Template(r"tpl/LevelAddUp.png", record_pos=(-0.079, 0.122), resolution=(1600, 900))):
        touch((800,200))
        time.sleep(1)

    touch(Template(r"tpl/LevelAddUp.png", record_pos=(-0.079, 0.122), resolution=(1600, 900)),duration=10)
    while True:
        time.sleep(1)
        wait(Template(r"tpl/Challenge.png", record_pos=(0.249, 0.228), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/Challenge.png", record_pos=(0.249, 0.228), resolution=(1600, 900)))
        wait(Template(r"tpl/title.png", record_pos=(0.206, -0.217), resolution=(1600, 900)))
        if not exists(Template(r"tpl/RecordStart.png", record_pos=(0.339, 0.216), resolution=(1600, 900))):
            touch((1400,700))
            time.sleep(1)
        wait(Template(r"tpl/RecordStart.png", record_pos=(0.339, 0.216), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/RecordStart.png", record_pos=(0.339, 0.216), resolution=(1600, 900)))
        wait(Template(r"tpl/AwdGet.png", record_pos=(-0.003, -0.182), resolution=(1600, 900)),timeout=240)
        time.sleep(1)
        touch(Template(r"tpl/AwdGet.png", record_pos=(-0.003, -0.182), resolution=(1600, 900)))
        wait(Template(r"tpl/OnceAwdGet.png", record_pos=(0.002, -0.179), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/OnceAwdGet.png", record_pos=(0.002, -0.179), resolution=(1600, 900)))
        wait(Template(r"tpl/nxt_2.png", record_pos=(0.393, 0.226), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/nxt_2.png", record_pos=(0.393, 0.226), resolution=(1600, 900)))
        wait(Template(r"tpl/nxt_1.png", record_pos=(0.363, 0.24), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/nxt_1.png", record_pos=(0.363, 0.24), resolution=(1600, 900)))
        wait(Template(r"tpl/tapScreen.png", record_pos=(0.002, 0.191), resolution=(1600, 900)))
        time.sleep(1)
        touch(Template(r"tpl/tapScreen.png", record_pos=(0.002, 0.191), resolution=(1600, 900)))
        
        # delete running temp pics
        temp_pics = [p for p in os.listdir() if p.endswith('.jpg')]
        for pic in temp_pics:
            os.remove(pic)
