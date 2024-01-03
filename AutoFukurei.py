# -*- encoding=utf8 -*-
__author__ = "KirisameVanilla"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.settings import Settings
from get_adb_address import get_adb_address as get_adb

Settings.THRESHOLD = 0.8

if not cli_setup():
    adb_address = get_adb()
    auto_setup(devices=[
        f"Android:///{adb_address}?cap_method=javacap&ori_method=adbori",
    ])


def start_Fukurei():
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

        time.sleep(60)
        wait(Template(r"tpl/AwdGet.png", record_pos=(-0.003, -0.182), resolution=(1600, 900)), timeout=240)
        time.sleep(1)
        touch((1300, 700))

        wait(Template(r"tpl/OnceAwdGet.png", record_pos=(0.002, -0.179), resolution=(1600, 900)))
        time.sleep(1)
        touch((1300, 700))

        wait(Template(r"tpl/nxt_1.png", record_pos=(0.393, 0.226), resolution=(1600, 900)))
        time.sleep(1)
        touch((1400, 820))

        wait(Template(r"tpl/nxt_2.png", record_pos=(0.363, 0.24), resolution=(1600, 900)))
        time.sleep(1)
        touch((1400, 820))

        time.sleep(1)
        wait(Template(r"tpl/tapScreen.png", record_pos=(0.002, 0.191), resolution=(1600, 900)))
        time.sleep(1)
        touch((1400, 820))

        clear_up_temp()


def clear_up_temp():
    # delete running temp pics
    temp_pics = [p for p in os.listdir() if p.endswith('.jpg')]
    for pic in temp_pics:
        os.remove(pic)


if __name__ == '__main__':
    start_Fukurei()
