SEP = " "


def format_value(value, spaces_count):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return make_stylish_result(value, spaces_count + 4)
    return value


def make_stylish_result(diff, spaces_count=2):
    indent = SEP * spaces_count
    formatted = []
    for item in diff:
        key_name = item["name_key"]
        current_value = format_value(item.get("value"), spaces_count)
        old_value = format_value(item.get("old_value"), spaces_count)
        new_value = format_value(item.get("new_value"), spaces_count)
        if item["action"] == "unchanged":
            formatted.append(f"{indent}  {key_name}: {current_value}")
        elif item["action"] == "modified":
            formatted.append(f"{indent}- {key_name}: {old_value}")
            formatted.append(f"{indent}+ {key_name}: {new_value}")
        elif item["action"] == "deleted":
            formatted.append(f"{indent}- {key_name}: {old_value}")
        elif item["action"] == "added":
            formatted.append(f"{indent}+ {key_name}: {new_value}")

    return f"{{\n{chr(10).join(formatted)}\n{SEP * (spaces_count - 2)}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
