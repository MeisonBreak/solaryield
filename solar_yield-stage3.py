# === Stage 3: Хранилище в памяти ===
# Project: SolarYield
import uuid
from datetime import date


class Panel:
    def __init__(self, name, power, tilt, install_date):
        self.id = str(uuid.uuid4())
        self.name = name
        self.power = power
        self.tilt = tilt
        self.install_date = install_date

    def __repr__(self):
        return f"Panel(id={self.id!r}, name={self.name!r})"


class PanelStore:
    def __init__(self):
        self._panels = {}

    def add(self, panel):
        self._panels[panel.id] = panel
        return panel

    def get(self, panel_id):
        return self._panels.get(panel_id)

    def list(self):
        return list(self._panels.values())


if __name__ == "__main__":
    store = PanelStore()

    panel1 = Panel("Панель-Север", power=400, tilt=30, install_date=date(2024, 5, 12))
    panel2 = Panel("Панель-Юг", power=550, tilt=25, install_date=date(2024, 6, 3))

    store.add(panel1)
    store.add(panel2)

    print(f"Добавлено панелей: {len(store.list())}")
    print(panel1)
    print(panel2)

    found = store.get(panel1.id)
    print(f"Найдена по id: {found.name}, мощность {found.power} Вт")

    missing = store.get("00000000-0000-0000-0000-000000000000")
    print(f"Отсутствует: {missing}")

    for p in store.list():
        print(f"  {p.name}: {p.power} Вт, угол {p.tilt}°, монтаж {p.install_date}")
