import os, random
import subprocess
from pathlib import Path


def random_permissions():
    r07 = lambda: str(random.randint(0, 7)) 
    return r07() + r07() + r07()


def get_mrd_properties(path):
    # 0 - метка безопасности 1 - уровень целостности 2 - [категории]  3 - [флаги]
    if not os.path.exists(path):
        raise FileNotFoundError
    properties = subprocess.check_output(['pdp-ls', '-Md', path], text=True)
    properties = properties.split()[-2].split(':')
    properties[2] = [] if properties[2] == 'Нет' else properties[2].split(',')
    properties[3] = [] if properties[3] == '0x0' else properties[3].split(',')
    return properties


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
    result = True if real_permissions == correct_permissions else False

    return result


def check_3_owner(path, correct_owner):
    if not os.path.exists(path):
        return False
    
    real_owner = Path(path).owner()
    result = True if real_owner == correct_owner else False

    return result


def check_4_group(path, correct_group):
    if not os.path.exists(path):
        return False
    
    real_owner = Path(path).owner()
    result = True if real_owner == correct_group else False

    return result


def check_5_privacy(path, correct_privacy):
    if not os.path.exists(path):
        return False
    
    real_privacy = get_mrd_properties(path)[0]
    result = True if real_privacy == correct_privacy else False
    
    return result

def check_6_integrity(path, correct_integrity):
    if not os.path.exists(path):
        return False
    
    real_integrity = get_mrd_properties(path)[1]
    result = True if real_integrity == correct_integrity else False

    return result

def check_7_categories(path, correct_categories):
    if not os.path.exists(path):
        return False
    
    result = True
    real_categories = get_mrd_properties(path)[2]
    result = True if set(real_categories) == set(correct_categories) else False

    return result

def check_8_flags(path, correct_flags):
    if not os.path.exists(path):
        return False
    
    result = True
    real_flags = get_mrd_properties(path)[3]
    result = True if set(real_flags) == set(correct_flags) else False

    return result