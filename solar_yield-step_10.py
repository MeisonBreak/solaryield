# === Stage 10: Теги ===
# Project: SolarYield
"""SolarYield — модуль тегов для «панель».

Добавление, удаление и поиск по тегу.
"""

from datetime import date


class PanelTag:
    """Тег, привязанный к панели."""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"PanelTag({self.name!r})"

    def __eq__(self, other):
        return isinstance(other, PanelTag) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class PanelTagStore:
    """Хранилище тегов панели: добавление, удаление, поиск."""

    def __init__(self):
        self._tags = set()

    def add_tag(self, name: str) -> PanelTag:
        tag = PanelTag(name)
        self._tags.add(tag)
        return tag

    def remove_tag(self, name: str) -> bool:
        return self._tags.discard(PanelTag(name)) != False

    def find_tags(self, name: str):
        return [tag for tag in self._tags if tag.name == name]

    def find_panel_tags(self, panel_name: str):
        return [tag for tag in self._tags if tag.name.startswith(panel_name)]
