def for_add(key, value):
    return {
        'action': 'added',
        'name_key': key,
        'new_value': format_nested_value(value)
    }


def for_delete(key, value):
    return {
        'action': 'deleted',
        'name_key': key,
        'old_value': format_nested_value(value)
    }


def for_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name_key': key,
        'value': format_nested_value(value)
    }


def for_modified(key, value1, value2):
    return {
        'action': 'modified',
        'name_key': key,
        'new_value': format_nested_value(value2),
        'old_value': format_nested_value(value1)
    }


def for_nested(key, value1, value2):
    if isinstance(value1, dict) and isinstance(value2, dict):
        return for_unchanged(key, generate_diff(value1, value2))

    if isinstance(value1, dict) or isinstance(value2, dict):
        value1 = value1 or {}
        value2 = value2 or {}
        return for_modified(key, value1, value2)

    if value1 != value2:
        return for_modified(key, value1, value2)

    return for_unchanged(key, value1)


def format_nested_value(value):
    if isinstance(value, dict):
        return generate_diff(value, value)
    return value


def generate_diff(file1, file2):
    keys = file1.keys() | file2.keys()
    added = file2.keys() - file1.keys()
    deleted = file1.keys() - file2.keys()

    diff = []

    for key in keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key in added:
            diff.append(for_add(key, value2))
        elif key in deleted:
            diff.append(for_delete(key, value1))
        else:
            diff.append(for_nested(key, value1, value2))

    sorted_diff = sorted(diff, key=lambda x: x['name_key'])

    return sorted_diff
