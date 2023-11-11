# -*- encoding=utf8 -*-
__author__ = "KirisameVanilla"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.settings import Settings

Settings.THRESHOLD = 0.8
os.system('adb devices')
if not cli_setup():
    auto_setup(devices=[
        "Android:///emulator-5554?cap_method=javacap&ori_method=adbori",
    ])

if __name__ == '__main__':
    wait(Template(r"tpl/Challenge.png", record_pos=(0.249, 0.228), resolution=(1600, 900)))
    time.sleep(1)
    if not exists(Template(r"tpl/LevelAddUp.png", record_pos=(-0.079, 0.122), resolution=(1600, 900))):
        touch((800, 200))
        time.sleep(1)

    # Switch to the highest level
    touch((670, 670), times=2)

    while True:
        time.sleep(1)
        wait(Template(r"tpl/Challenge.png", record_pos=(0.249, 0.228), resolution=(1600, 900)))
        time.sleep(1)
        # touch Challenge
        touch((1180, 810))
        time.sleep(1)
        wait(Template(r"tpl/title.png", record_pos=(0.206, -0.217), resolution=(1600, 900)))
        if not exists(Template(r"tpl/RecordStart.png", record_pos=(0.339, 0.216), resolution=(1600, 900))):
            touch((1400, 700))
            time.sleep(1)
        wait(Template(r"tpl/RecordStart.png", record_pos=(0.339, 0.216), resolution=(1600, 900)))
        time.sleep(1)
        touch((1335, 785))
        wait(Template(r"tpl/AwdGet.png", record_pos=(-0.003, -0.182), resolution=(1600, 900)), timeout=240)
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
