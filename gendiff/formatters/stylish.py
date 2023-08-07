SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


def format_for_dict(data, spaces_count=2):
    indent = SEPARATOR * spaces_count
    lines = []
    for key, value in data.items():
        formatted_value = format_value(value, spaces_count)
        lines.append(f"{indent}{NONE}{key}: {formatted_value}")
    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (spaces_count - 2)
    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_value(value, spaces_count=0):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        return make_stylish_result(value, spaces_count + 4)
    if isinstance(value, dict):
        return format_for_dict(value, spaces_count + 4)
    return f"{value}"


def make_stylish_result(diff, spaces_count=2):
    indent = SEPARATOR * spaces_count
    lines = []
    for item in diff:
        key_name = item['name']
        old_value = format_value(item.get("old_value"), spaces_count)
        new_value = format_value(item.get("new_value"), spaces_count)
        if item["action"] == "unchanged":
            current_value = format_value(item.get("value"), spaces_count)
            lines.append(f"{indent}{NONE}{key_name}: {current_value}")
        elif item["action"] == "modified":
            lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
            lines.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif item["action"] == "deleted":
            lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
        elif item["action"] == "added":
            lines.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif item['action'] == 'nested':
            children = make_stylish_result(
                item.get("children"), spaces_count + 4
            )
            lines.append(f"{indent}{NONE}{key_name}: {children}")
    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_result(data)
