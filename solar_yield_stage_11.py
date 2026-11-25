# === Stage 11: Группировка ===
# Project: SolarYield
def group_panels_by_power(panels):
    groups = {}
    for panel in panels:
        power = panel["power"]
        groups.setdefault(power, []).append(panel)
    return groups


def count_panels_by_power(panels):
    counts = {}
    for panel in panels:
        power = panel["power"]
        counts[power] = counts.get(power, 0) + 1
    return counts


def summarize_by_power(panels):
    summary = {}
    for panel in panels:
        power = panel["power"]
        entry = summary.setdefault(power, {"count": 0, "total_power": 0.0})
        entry["count"] += 1
        entry["total_power"] += panel["power"]
    return summary


def format_power_report(summary):
    lines = []
    for power in sorted(summary):
        entry = summary[power]
        lines.append(f"Мощность {power} кВт: {entry['count']} панелей, суммарно {entry['total_power']} кВт")
    return "\n".join(lines)


def power_report(panels):
    summary = summarize_by_power(panels)
    return format_power_report(summary)


if __name__ == "__main__":
    sample = [
        {"name": "Панель А", "power": 400, "tilt": 30, "install_date": "2024-01-15"},
        {"name": "Панель Б", "power": 400, "tilt": 35, "install_date": "2024-02-20"},
        {"name": "Панель В", "power": 550, "tilt": 30, "install_date": "2024-03-10"},
        {"name": "Панель Г", "power": 400, "tilt": 40, "install_date": "2024-04-05"},
    ]
    print(power_report(sample))
