import datetime


def get_current_date():
    """
    Получает текущую дату.

    Returns:
    datetime.date: Текущая дата.
    """
    return datetime.date.today()


def add_days_to_date(base_date, days_to_add):
    """
    Добавляет указанное количество дней к заданной дате.

    Args:
    base_date (datetime.date): Исходная дата.
    days_to_add (int): Количество дней для добавления.

    Returns:
    datetime.date: Новая дата после добавления дней.
    """
    return base_date + datetime.timedelta(days=days_to_add)


def format_date(date, format_str="%Y-%m-%d"):
    """
    Форматирует дату в строку с использованием указанного формата.

    Args:
    date (datetime.date): Дата для форматирования.
    format_str (str): Формат строки даты (по умолчанию "%Y-%m-%d").

    Returns:
    str: Отформатированная строка даты.
    """
    return date.strftime(format_str)


def calculate_date_difference(date1, date2):
    """
    Вычисляет разницу между двумя датами.

    Args:
    date1 (datetime.date): Первая дата.
    date2 (datetime.date): Вторая дата.

    Returns:
    datetime.timedelta: Разница между двумя датами.
    """
    return date1 - date2


def is_leap_year(year):
    """
    Проверяет, является ли указанный год високосным.

    Args:
    year (int): Год для проверки.

    Returns:
    bool: True, если год високосный, иначе False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
