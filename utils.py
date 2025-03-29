import json


def dict_list_to_json(dict_list, filename):
    """
    Преобразует список словарей в JSON-строку и сохраняет ее в файл
    """

    try:
        json_str = json.dumps(dict_list)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_str)
            return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Произошла ошибка: {e}")
        return None


def json_to_dict_list(filename):
    """
    Преобразует JSON-строку в список словарей
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            json_str = file.read()
            return json.loads(json_str)
    except (TypeError, ValueError, IOError) as e:
        print(f"Произошла ошибка: {e}")
        return None
