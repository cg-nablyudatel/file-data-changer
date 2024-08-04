import os
import datetime
import time
#cipher_glitch
def change_file_datetime(file_path, new_datetime):
    try:
        os.utime(file_path, (time.mktime(new_datetime.timetuple()), time.mktime(new_datetime.timetuple())))
        print(f"Дата и время файла '{file_path}' успешно изменены на {new_datetime}")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка изменения даты и времени: {e}")


if __name__ == "__main__":
    file_path = input("Введите путь к файлу: ")
    year = int(input("Введите год (например, 2023): "))
    month = int(input("Введите месяц (от 1 до 12): "))
    day = int(input("Введите день (от 1 до 31): "))
    hour = int(input("Введите час (от 0 до 23): "))
    minute = int(input("Введите минуту (от 0 до 59): "))
    second = int(input("Введите секунду (от 0 до 59): "))

    new_datetime = datetime.datetime(year, month, day, hour, minute, second)
    change_file_datetime(file_path, new_datetime)
