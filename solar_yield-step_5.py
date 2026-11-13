# === Stage 5: Связанная сущность ===
# Project: SolarYield
from datetime import date


class Reading:
    def __init__(self, panel_id, value, measured_at):
        self.panel_id = panel_id
        self.value = value
        self.measured_at = measured_at

    def __repr__(self):
        return (f"Reading(panel_id={self.panel_id}, "
                f"value={self.value}, measured_at={self.measured_at})")
