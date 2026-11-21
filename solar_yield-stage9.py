# === Stage 9: Поиск по нескольким словам ===
# Project: SolarYield
def normalize_query(text):
    """Нормализует строку запроса: разбивает на токены и убирает лишнее."""
    tokens = []
    for raw in text.replace('"', '').replace('"', '').split():
        if raw.startswith('-'):
            tokens.append(('-' + raw[1:].strip().lower()))
        else:
            tokens.append(raw.strip().lower())
    return tokens


def tokenize_panel(panel):
    """Формирует набор поисковых слов из полей панели."""
    words = {
        panel.get('name', ''),
        panel.get('title', ''),
        str(panel.get('power', '')).lower(),
        str(panel.get('tilt', '')).lower(),
        str(panel.get('installed_date', '')).lower(),
        str(panel.get('location', '')).lower(),
    }
    words = {w for w in words if w}
    return words


def search_panels(panels, query):
    """
    Поиск панелей по нескольким словам с поддержкой исключений.

    Токены вида '-слово' исключают панели, содержащие 'слово' в любом
    из полей. Остальные токены должны присутствовать в панели (AND).
    """
    tokens = normalize_query(query)
    if not tokens:
        return []

    required = [t for t in tokens if not t.startswith('-')]
    excluded = [t[1:] for t in tokens if t.startswith('-')]

    if not required:
        return [p for p in panels if not any(
            ex in tokenize_panel(p) for ex in excluded)]

    result = []
    for panel in panels:
        words = tokenize_panel(panel)
        if all(req in words for req in required):
            if not any(ex in words for ex in excluded):
                result.append(panel)
    return result


def main():
    panels = [
        {'name': 'Север-1', 'power': 400, 'tilt': 30, 'installed_date': '2023-05-01'},
        {'name': 'Юг-2', 'power': 500, 'tilt': 45, 'installed_date': '2024-01-15'},
        {'name': 'Запад-3', 'power': 350, 'tilt': 20, 'installed_date': '2024-02-20'},
    ]

    print('По запросу "power":')
    for p in search_panels(panels, 'power'):
        print(' ', p['name'])

    print('По запросу "power -запад":')
    for p in search_panels(panels, 'power -запад'):
        print(' ', p['name'])

    print('По запросу "tilt 30":')
    for p in search_panels(panels, 'tilt 30'):
        print(' ', p['name'])


if __name__ == '__main__':
    main()
