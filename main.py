from variants import variant_1
from utils    import *
import requests, time, os


def request_task(fio):
    url = "http://172.18.4.200:8080/start"
    payload = {
        "username": fio,
        "lab": "Мандатное разграничение доступа Astra Linux",
    }
    response = requests.get(url, params=payload)
    return response

def generate_personal_task(files, surname):
    for f in files:
        for k in f.keys():
            f[k]  = f[k].replace('SURNAME', surname)
    return files

def main():
    surname     = input("Введите вашу Фамилию: ")
    name        = input("Введите ваше Имя: ")
    response    = {'variant': 1, 'tasks' : [1, 2, 3]} # response = request_task(fio)
    files       = generate_personal_task(variant_1, surname)
    max_result  = len(response['tasks']) * len(files)
    time_passed = 0
    result      = 0


    while True:
        os.system('clear')
        print(f"{surname} {name}, Вариант {response['variant']}")
        print(f"Тебе надо выполнить задания {response['tasks']}")
        print(f"Прошло времени: {time_passed//60:02}:{time_passed%60:02}")
        print(f"Текущий балл: {result} из {max_result}")
        print(f"======================================")

        result = 0
        for f in files:
            if 1 in response['tasks']:
                if check_1_exist(f['path'], f['type']):
                    result += 1
                else:
                    print(f"Объект: {f['path']}\nОшибка: Объект не существует")
                    break
            if 2 in response['tasks']:
                if check_2_perms(f['path'], f['permissions']):
                    result += 1
                else:
                    print(f"Объект: {f['path']}\nОшибка: Неверные права доступа")
                    break
            if 3 in response['tasks']:
                if check_3_owner(f['path'], f['owner']):
                    result += 1
                else:
                    print(f"Объект: {f['path']}\nОшибка: Неверный владелец объекта")
                    break
            if 4 in response['tasks']:
                if check_4_group(f['path'], f['group']):
                    result += 1
                else:
                    print(f"Объект: {f['path']}\nОшибка: Неверная группа объекта")
                    break
        if max_result == result:
            break
        time.sleep(1)
        time_passed += 1

    print(f"Лабораторная работа завершена!")
    print(f"Итоговый балл: {result} из {max_result}")
    exit()




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\nВыполнение работы прервано!")






