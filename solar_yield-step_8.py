# === Stage 8: Сортировка записей ===
# Project: SolarYield
from datetime import date


def sort_panels_by_name(panels, descending=False):
    return sorted(panels, key=lambda p: p["name"], reverse=descending)


def sort_panels_by_install_date(panels, descending=False):
    return sorted(panels, key=lambda p: p["install_date"], reverse=descending)


def sort_panels(panels, field="name", descending=False):
    if field == "install_date":
        return sort_panels_by_install_date(panels, descending=descending)
    return sort_panels_by_name(panels, descending=descending)


def main():
    panels = [
        {
            "name": "Южная",
            "power": 400,
            "tilt": 30,
            "install_date": date(2023, 5, 12),
        },
        {
            "name": "Северная",
            "power": 350,
            "tilt": 15,
            "install_date": date(2022, 9, 3),
        },
        {
            "name": "Западная",
            "power": 300,
            "tilt": 25,
            "install_date": date(2024, 1, 20),
        },
    ]

    print("По названию (возрастание):")
    for panel in sort_panels(panels, "name", descending=False):
        print(f"  {panel['name']}")

    print("По названию (убывание):")
    for panel in sort_panels(panels, "name", descending=True):
        print(f"  {panel['name']}")

    print("По дате монтажа (возрастание):")
    for panel in sort_panels(panels, "install_date", descending=False):
        print(f"  {panel['name']} ({panel['install_date']})")

    print("По дате монтажа (убывание):")
    for panel in sort_panels(panels, "install_date", descending=True):
        print(f"  {panel['name']} ({panel['install_date']})")


if __name__ == "__main__":
    main()
