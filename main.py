import requests, os

fio = input()

url = "http://172.18.4.200:8080/start"
payload = {
  "username": fio,
  "lab": "Мандатное разграничение доступа Astra Linux",
}
surname = fio.split()[0]
response = requests.get(url, params=payload)

files = [
    {
        'path'         : '/{:s}/Секретно',
        'type'         : 'd',
        'permissions'  : '',
        'owner'        : '',
        'group'        : '',
        'privacy_label': '',
        'integrity'    : '',
        'categories'   : '',
        'flags'        : ''
    },

]

print(f"У тебя вариант {response['variant']}")
print(f"Тебе надо выполнить задания {response['tasks']}")

tasks = response["tasks"]
total_sum = 0
















if "ssh" in tasks:
    print("ВВеди флаг полученный от взлома ssh:")
    while True:
        if input("Флаг:") == flag1:
            print("Флаг введен верно!")
            total_sum +=1
            break
        else:
            print("Флаг введен не верно")
elif "ftp" in tasks:
    print("ВВеди флаг полученный от взлома ftp:")
    while True:
        if input("Флаг:") == flag2:
            print("Флаг введен верно!")
            total_sum +=1
            break
        else:
            print("Флаг введен не верно")


elif total_sum == 2:
    print("Задание выполнено")