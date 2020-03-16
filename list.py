import os
import time
import warnings


_SYSFS_ROOT = "/sys/class/gpio"

def _list_gpio():
    for fn in os.listdir(_SYSFS_ROOT):
        if not fn.startswith('gpio'):
            continue
        if fn.startswith('gpiochip'):
            continue
        temp = int(fn.replace('gpio',''))
        print(temp)

