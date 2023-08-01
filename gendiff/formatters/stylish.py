SEPARATOR = " "


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
    indent = SEPARATOR * spaces_count
    fprmatted_diff = []
    for item in diff:
        key_name = item["name_key"]
        current_value = format_value(item.get("value"), spaces_count)
        old_value = format_value(item.get("old_value"), spaces_count)
        new_value = format_value(item.get("new_value"), spaces_count)
        if item["action"] == "unchanged":
            fprmatted_diff.append(f"{indent}  {key_name}: {current_value}")
        elif item["action"] == "modified":
            fprmatted_diff.append(f"{indent}- {key_name}: {old_value}")
            fprmatted_diff.append(f"{indent}+ {key_name}: {new_value}")
        elif item["action"] == "deleted":
            fprmatted_diff.append(f"{indent}- {key_name}: {old_value}")
        elif item["action"] == "added":
            fprmatted_diff.append(f"{indent}+ {key_name}: {new_value}")

    formatted_string = '\n'.join(fprmatted_diff)
    end_indent = SEPARATOR * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
