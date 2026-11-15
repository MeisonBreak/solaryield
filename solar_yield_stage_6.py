# === Stage 6: Генерация идентификаторов ===
# Project: SolarYield
"""SolarYield — генерация уникальных идентификаторов с префиксом проекта и проверкой коллизий."""

import uuid
from datetime import datetime

PROJECT_ID_PREFIX = "SY"
IDENTIFIER_NAMESPACE = "solyield.identifiers"


def generate_unique_identifier(name: str, *, counter: dict | None = None,
                                max_attempts: int = 10000) -> str:
    """Генерирует уникальный идентификатор с префиксом проекта.

    Идентификатор формируется из префикса проекта, короткого хеша имени
    сущности и случайного суффикса из пространства имён проекта.
    При столкновении с уже существующим идентификатором (через коллбэк
    ``counter``) генерация повторяется, пока уникальность не будет достигнута.
    """
    short_hash = hash(name) % 100000
    base = f"{PROJECT_ID_PREFIX}{short_hash:05d}"

    for _ in range(max_attempts):
        candidate = base + uuid.uuid4().hex[:8]
        if counter is not None:
            if candidate in counter:
                continue
        return candidate


def ensure_unique(name: str, existing: set[str] | None = None) -> str:
    """Генерирует уникальный идентификатор, гарантируя отсутствие коллизий.

    ``existing`` — множество уже выданных идентификаторов. Если передано,
    используется для проверки коллизий; иначе генерируется уникальный
    идентификатор через ``uuid`` с повторными попытками.
    """
    if existing is None:
        return generate_unique_identifier(name)

    short_hash = hash(name) % 100000
    base = f"{PROJECT_ID_PREFIX}{short_hash:05d}"

    for _ in range(10000):
        candidate = base + uuid.uuid4().hex[:8]
        if candidate not in existing:
            existing.add(candidate)
            return candidate
        continue

    raise RuntimeError("Не удалось сгенерировать уникальный идентификатор")


def register_identifier(name: str, identifier: str,
                        registry: dict[str, str] | None = None) -> None:
    """Регистрирует идентификатор сущности в словаре-реестре.

    Если реестр не передан, создаётся новый. Ключ — имя сущности,
    значение — сгенерированный уникальный идентификатор.
    """
    if registry is None:
        registry = {}
    registry[name] = identifier


def unique_timestamp() -> str:
    """Возвращает строку-идентификатор, основанный на текущем времени."""
    return f"{PROJECT_ID_PREFIX}{datetime.now().strftime('%Y%m%d%H%M%S%f')}"


if __name__ == "__main__":
    registry: dict[str, str] = {}
    identifiers = [
        generate_unique_identifier("Панель-Юг-1"),
        generate_unique_identifier("Панель-Север-2"),
        ensure_unique("Панель-Юг-1", set(registry.values())),
        register_identifier("Инвертор-Основной", unique_timestamp()),
    ]

    for name, value in identifiers:
        print(f"{name:20} -> {value}")
