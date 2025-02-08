from variants import variants
from transliterate import translit # type: ignore
from utils    import *
import requests, time, os # type: ignore
import json

GRP = False # GENERATE_RANDOM_PERMISSIONS
SWW = True  # SHOW_WHATS_WRONG

def request_task(surname, name):
    print("Запрос заданий для выполнения...")
    url = "http://172.18.4.200:8080/api/start"
    payload = {
        "username":   surname + "_" + name,
        "pnet_login": "",
        "lab":        "Мандатное разграничение доступа Astra Linux",
        "lab_slug":   "mandatnoe-razgranichenie-dostupa-astra-linux"
    }
    payload = json.dumps(payload).encode('utf-8')

    response = requests.request("GET", url, data=payload)
    response.encoding = 'utf-8'
    response = json.loads(response.text)
    return response

def finish_task(surname, name):
    url = "http://172.18.4.200:8080/api/end"
    payload = {
        "username":   surname + "_" + name,
        "pnet_login": "",
        "lab":        "Мандатное разграничение доступа Astra Linux",
        "lab_slug":   "mandatnoe-razgranichenie-dostupa-astra-linux"
    }
    payload = json.dumps(payload).encode('utf-8')
    response = requests.request("POST", url, data=payload)
    response.encoding = 'utf-8'
    response = json.loads(response.text)
    return response

def generate_personal_task(files, surname):
    for f in files:
        for k in ['path', 'owner', 'group']:
            f[k]  = f[k].replace('SURNAME', translit(surname.lower(),'ru', reversed=True))
        if GRP:
            f['permissions'] = random_permissions() 
    return files

def main():
    os.system('clear')
    surname     = input("Введите Фамилию: ")
    name        = input("Введите Имя:     ")
    response    = request_task(surname, name) # response    = {'variant': 1, 'tasks' : [1, 2, 3, 4, 5]}
    if 'variant' not in response.keys() or 'tasks' not in response.keys():
        print("Ошибка получения заданий для выполнения!")
        exit()
    files       = generate_personal_task(variants[response['variant']-1], surname)
    max_result  = len(response['tasks']) * len(files)
    time_passed = 0
    result      = 0


    while True:
        os.system('clear')
        print(f"{surname} {name}, Вариант {response['variant']}")
        print(f"Тебе надо выполнить задания:\n{response['tasks']}")
        print(f"Прошло времени: {time_passed//60:02}:{time_passed%60:02}")
        print(f"Текущий балл:   {result:02}/{max_result:02}")
        print(f"======================================")
            
        result = 0
        for f in files:
            if "1" in response['tasks']:
                if check_1_exist(f['path'], f['type']):
                    result += 1
                else:
                    if SWW:
                        print(f"Объект: {f['path']}\nОшибка: Объект не существует")
                    break
            if "2" in response['tasks']:
                if check_2_perms(f['path'], f['permissions']):
                    result += 1
                else:
                    if SWW:
                        print(f"Объект: {f['path']}\nОшибка: Неверные права доступа")
                        print(f"Должно быть: {f['permissions']}")
                    break
            if "3" in response['tasks']:
                if check_3_owner(f['path'], f['owner']):
                    result += 1
                else:
                    if SWW:
                        print(f"Объект: {f['path']}\nОшибка: Неверный владелец объекта")
                        print(f"Должно быть: {f['owner']}")
                    break
            if "4" in response['tasks']:
                if check_4_group(f['path'], f['group']):
                    result += 1
                else:
                    if SWW:
                        print(f"Объект: {f['path']}\nОшибка: Неверная группа объекта")
                        print(f"Должно быть: {f['group']}")
                    break
            if "5" in response['tasks']:
                if check_5_privacy(f['path'], f['privacy_label']):
                    result += 1
                else:
                    if SWW:
                        print(f"Объект: {f['path']}\nОшибка: Неверный уровень конфиденциальности")
                        print(f"Должно быть: {f['privacy_label']}")
                    break
            if "6" in response['tasks']:
                if check_6_integrity(f['path'], f['integrity']):
                    result += 1
                else:
                    if SWW:
                        print(f"Объект: {f['path']}\nОшибка: Неверный уровень целостности")
                        print(f"Должно быть: {f['integrity']}")
                    break
            if "7" in response['tasks']:
                if check_7_categories(f['path'], f['categories']):
                    result += 1
                else:
                    if SWW:
                        print(f"Объект: {f['path']}\nОшибка: Неверно присвоены категории")
                        print(f"Должно быть: {f['categories']}")
                    break
            if "8" in response['tasks']:
                if check_8_flags(f['path'], f['flags']):
                    result += 1
                else:
                    if SWW:
                        print(f"Объект: {f['path']}\nОшибка: Неверно присвоены специальные флаги")
                        print(f"Должно быть: {f['flags']}")
                    break
        if max_result == result:
            break
        time.sleep(1)
        time_passed += 1
        

    print(f"Лабораторная работа завершена!")
    print(f"Итоговый балл: {result} из {max_result}")
    response = finish_task(surname, name)
    print(f"Ответ сервера: {response['message']}")
    exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\nВыполнение работы прервано!")






