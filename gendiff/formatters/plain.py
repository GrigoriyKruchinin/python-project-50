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


def format_action(action, current_path, old_value, new_value):
    if action == 'added':
        return f"Property '{current_path}' was added with value: {new_value}"
    elif action == 'deleted':
        return f"Property '{current_path}' was removed"
    elif action == 'modified':
        return (
            f"Property '{current_path}' was updated. "
            f"From {old_value} to {new_value}"
        )
    else:
        return None


def make_plain_result_item(item, path=''):
    current_key = item.get('name')
    current_path = f"{path}.{current_key}" if path else current_key
    action = item.get('action')
    old_value = format_value(item.get('old_value'))
    new_value = format_value(item.get('new_value'))

    if action == 'nested':
        children = item.get('children')
        return make_plain_result(children, current_path)
    else:
        return format_action(action, current_path, old_value, new_value)


def make_plain_result(diff, path=''):
    result = []
    for item in diff:
        formatted_item = make_plain_result_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)


def format_diff_plain(data):
    return make_plain_result(data)
