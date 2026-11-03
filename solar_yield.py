# === Stage 1: Каркас модуля ===
# Project: SolarYield
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Panel:
    name: str
    power_kw: float
    tilt_deg: float
    install_date: date

    def describe(self) -> str:
        return (
            f"Панель «{self.name}»"
            f", мощность {self.power_kw} кВт, "
            f"наклон {self.tilt_deg}°, монтаж {self.install_date}"
        )


def make_demo_panels() -> list[Panel]:
    return [
        Panel("Южная сторона", 4.0, 30.0, date(2023, 5, 12)),
        Panel("Западная сторона", 3.2, 40.0, date(2023, 9, 3)),
    ]


def main() -> None:
    panels = make_demo_panels()
    print("SolarYield — учёт выработки солнечных панелей")
    print("=" * 45)
    for panel in panels:
        print(panel.describe())


if __name__ == "__main__":
    main()
