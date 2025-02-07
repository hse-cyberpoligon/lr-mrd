import os

def check_1_existence(path, type):
    result = False
    if type == 'f':
        result = os.path.isfile(path)
    elif type == 'd':
        result = os.path.isdir(path)
    else:
        raise ValueError
    return result

def check_2_permissions(path, permissions):
    real_permissions = oct(os.stat(path).st_mode)[-3:]
    result = False
    if real_permissions == permissions:
        result = True
    return result

def check_3_owner(path, owner):
    real_permissions = oct(os.stat(path).st_mode)[-3:]
    result = False
    if real_permissions == permissions:
        result = True

    return result
