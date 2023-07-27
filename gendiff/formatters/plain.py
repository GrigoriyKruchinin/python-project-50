def format_value(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_diff_plain(diff, path=''):  # noqa: C901
    result = []
    for item in diff:
        current_key = item.get('name_key')
        current_path = f"{path}.{current_key}" if path else current_key
        action = item.get('action')
        old_value = format_value(item.get('old_value'))
        new_value = format_value(item.get('new_value'))

        if action == 'added':
            result.append(
                f"Property '{current_path}' was added with value: {new_value}"
            )
        elif action == 'deleted':
            result.append(f"Property '{current_path}' was removed")
        elif action == 'modified':
            result.append(f"Property '{current_path}' was updated. "
                          f"From {old_value} to {new_value}")
        elif action == 'unchanged':
            if isinstance(item.get('value'), list):
                result.append(format_diff_plain(item['value'], current_path))

    return '\n'.join(result)
