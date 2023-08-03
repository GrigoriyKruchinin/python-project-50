SEPARATOR = " "
ADD = '+ '
DELETE = '- '
UNCHANGED = '  '


def format_value(value, spaces_count):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        return make_stylish_result(value, spaces_count + 4)
    return f'{value}'


def make_stylish_result(diff, spaces_count=2):
    indent = SEPARATOR * spaces_count
    formatted_diff = []
    for item in diff:
        key_name = item["name_key"]
        old_value = format_value(item.get("old_value"), spaces_count)
        new_value = format_value(item.get("new_value"), spaces_count)
        if item["action"] == "unchanged":
            current_value = format_value(item.get("value"), spaces_count)
            formatted_diff.append(f"{indent}{UNCHANGED}{key_name}: {current_value}")
        elif item["action"] == "modified":
            formatted_diff.append(f"{indent}{DELETE}{key_name}: {old_value}")
            formatted_diff.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif item["action"] == "deleted":
            formatted_diff.append(f"{indent}{DELETE}{key_name}: {old_value}")
        elif item["action"] == "added":
            formatted_diff.append(f"{indent}{ADD}{key_name}: {new_value}")

    formatted_string = '\n'.join(formatted_diff)
    end_indent = SEPARATOR * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
