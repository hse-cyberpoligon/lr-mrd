# Чекер для ЛР по МРД в Astra Linux
Программа связывается с сервером, получает набор заданий, проверяет их выполнение и отсылает на сервер результат выполнения работы

```
main.py     – Входная точка и основной программный цикл
utils.py    – Функции проверки выполнения заданий
variants.py – Наборы вариантов заданий
```



apt install ca-certificates
apt update
apt install python3-venv
python3 -m venv .venv
source .venc/bin/activate
pip install -r requirments.txt
