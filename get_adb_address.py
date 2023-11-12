import os


def get_adb_address() -> str:
    output = os.popen('adb devices').read()
    line = []
    for l in output.splitlines():
        line.append(l)
    adb_address = line[1].split('\t')[0]
    return adb_address
