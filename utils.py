import os
from pathlib import Path


def check_1_exist(path, type):
    result = False
    if type == 'f':
        result = os.path.isfile(path)
    elif type == 'd':
        result = os.path.isdir(path)
    else:
        raise ValueError
    return result


def check_2_perms(path, correct_permissions):
    if not os.path.exists(path):
        return False
    real_permissions = oct(os.stat(path).st_mode)[-3:]
    result = False
    if real_permissions == correct_permissions:
        result = True
    return result


def check_3_owner(path, correct_owner):
    if not os.path.exists(path):
        return False
    try:
        real_owner = Path(path).owner() # TODO: Check if implemented on Astra
    except NotImplementedError:
        real_owner = ""
    print(real_owner)
    result = False
    if real_owner == correct_owner:
        result = True

    return result


def check_4_group(path, correct_group):
    if not os.path.exists(path):
        return False
    try:
        real_owner = Path(path).owner() # TODO: Check if implemented on Astra
    except NotImplementedError:
        real_owner = ""

    result = False
    if real_owner == correct_owner:
        result = True

    return result