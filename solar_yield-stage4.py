# === Stage 4: Редактирование записей ===
# Project: SolarYield
import datetime


EDITABLE_PANEL_FIELDS = ("name", "power", "tilt_angle", "install_date")


def edit_panel(panel_id, changes):
    """Редактирование сущности «панель» по идентификатору.

    В changes передается словарь, содержащий только допустимые поля для
    редактирования. Проверка выполняется с помощью EDITABLE_PANEL_FIELDS.
    """
    unknown_fields = set(changes.keys()) - set(EDITABLE_PANEL_FIELDS)
    if unknown_fields:
        raise ValueError(
            "Допустимые поля для редактирования панели: "
            + ", ".join(EDITABLE_PANEL_FIELDS)
            + ". Неизвестные поля: " + ", ".join(sorted(unknown_fields))
        )

    name = changes.get("name")
    if name is not None and not isinstance(name, str):
        raise ValueError("Поле name должно быть строкой")
    if name is not None and not name.strip():
        raise ValueError("Поле name не может быть пустым")

    power = changes.get("power")
    if power is not None:
        if isinstance(power, bool) or not isinstance(power, (int, float)):
            raise ValueError("Поле power должно быть числом")
        if power <= 0:
            raise ValueError("Поле power должно быть положительным числом")

    tilt_angle = changes.get("tilt_angle")
    if tilt_angle is not None:
        if isinstance(tilt_angle, bool) or not isinstance(tilt_angle, (int, float)):
            raise ValueError("Поле tilt_angle должно быть числом")
        if tilt_angle < 0 or tilt_angle > 90:
            raise ValueError("Поле tilt_angle должно быть от 0 до 90")

    install_date = changes.get("install_date")
    if install_date is not None:
        if not isinstance(install_date, datetime.date) or isinstance(
            install_date, datetime.datetime
        ):
            raise ValueError("Поле install_date должно быть объектом datetime.date")

    valid_changes = {
        key: value
        for key, value in changes.items()
        if key in EDITABLE_PANEL_FIELDS and value is not None
    }
    if not valid_changes:
        raise ValueError("Не переданы допустимые поля для редактирования")

    return valid_changes
