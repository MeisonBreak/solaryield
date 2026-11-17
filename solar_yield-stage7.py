# === Stage 7: Фильтрация записей ===
# Project: SolarYield
from datetime import date


def filter_by_power(records, min_power=None, max_power=None):
    result = []
    for record in records:
        power = float(record.get("мощность", 0))
        if min_power is not None and power < min_power:
            continue
        if max_power is not None and power > max_power:
            continue
        result.append(record)
    return result


def filter_by_date_range(records, start_date=None, end_date=None):
    result = []
    for record in records:
        install_date = record.get("дата монтажа")
        if install_date is None:
            continue
        current = date.fromisoformat(str(install_date).split("T")[0])
        if start_date is not None and current < start_date:
            continue
        if end_date is not None and current > end_date:
            continue
        result.append(record)
    return result


def filter_panel_records(records, min_power=None, max_power=None,
                         start_date=None, end_date=None):
    filtered_by_power = filter_by_power(records, min_power, max_power)
    filtered_by_date = filter_by_date_range(
        filtered_by_power, start_date, end_date)
    return filtered_by_date
