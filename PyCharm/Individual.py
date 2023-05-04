#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
from datetime import date


def add_man():
    """
    Добавление людей
    """

    name = input("Фамилия и инициалы? ")
    post = input("Телефон? ")
    year = input("Год рождения? ")
    year = year.split(".")
    year = date(int(year[0]), int(year[1]), int(year[2]))

    # Создать словарь.
    man = {
        'name': name,
        'tel': post,
        'date': year,
    }

    # Добавить словарь в список.
    return man


def list_man(people):
    """
    Вывод людей
    """

    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 12
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
            "№",
            "Ф.И.О.",
            "Телефон",
            "Год рождения"
        )
    )
    print(line)

    for idx, man in enumerate(people, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                idx,
                man.get('name', ''),
                man.get('tel', ''),
                str(man.get('date', 0))
            )
        )
    print(line)


def select_man(arr, person):
    """
    Вывод конкретных людей
    """
    result = []
    for employee in arr:
        if employee.get('name', person).lower() == person.lower():
            result.append(employee)

    # Возвратить список выбранных работников.
    return result


def display_man(staff):
    if staff:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 12
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
                "№",
                "Ф.И.О.",
                "Телефон",
                "Год рождения"
            )
        )
        print(line)
        for idx, worker in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                    idx,
                    worker.get('name', ''),
                    worker.get('tel', ''),
                    str(worker.get('date', 0))
                )
            )
        print(line)
    else:
        print("Список пуст")

def help_man():
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("select <имя> - запросить людей с этим именем;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    print("load - загрузить данные из файла;")
    print("save - сохранить данные в файл;")

def save_workers(file_name, staff):
    """
    Сохранить всех работников в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(staff, fout, ensure_ascii=False, indent=4, default=str)


def load_workers(file_name):
    """
    Загрузить всех работников из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    people = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == "add":
           people.append(add_man())
           if len(people) > 1:
               people.sort(key=lambda item: item.get('tel', ''))

        elif command == 'list':
           display_man(people)

        elif command.startswith('select'):
            parts = command.split(' ', maxsplit=1)
            period = parts[1]
            select = select_man(people, period)
            display_man(select)

        elif command.startswith("save "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            save_workers(file_name, people)

        elif command.startswith("load "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            people = load_workers(file_name)

        elif command == 'help':
           help_man()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == '__main__':
    main()