# === Stage 2: Проверка полей ===
# Project: SolarYield
from datetime import date


def normalize_text(value):
    text = value.strip()
    if text.lower() == "":
        raise ValueError("Название не может быть пустым.")
    return text


def normalize_power(value):
    number = float(value)
    if number <= 0:
        raise ValueError("Мощность должна быть положительным числом.")
    return number


def normalize_angle(value):
    number = float(value)
    if number < 0 or number > 90:
        raise ValueError("Угол наклона должен быть от 0 до 90 градусов.")
    return number


def normalize_date(value):
    text = value.strip()
    formats = ["%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"]
    for fmt in formats:
        try:
            return date(*map(int, text.split(fmt[0])))
        except (ValueError, TypeError):
            continue
    raise ValueError("Дата монтажа должна быть в формате ДД.ММ.ГГГГ или ГГГГ-ММ-ДД.")


def validate_panel(name, power, angle, install_date):
    panel_name = normalize_text(name)
    panel_power = normalize_power(power)
    panel_angle = normalize_angle(angle)
    panel_date = normalize_date(install_date)
    return panel_name, panel_power, panel_angle, panel_date
