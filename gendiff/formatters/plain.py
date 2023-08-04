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


def make_plain_result(diff, path=''):
    result = []
    for item in diff:
        current_key = item.get('name')
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
                result.append(make_plain_result(item['value'], current_path))

    return '\n'.join(result)


def format_diff_plain(data):
    return make_plain_result(data)
