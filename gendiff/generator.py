def for_add(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def for_delete(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def for_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def for_modified(key, value1, value2):
    return {
        'action': 'modified',
        'name': key,
        'new_value': value2,
        'old_value': value1
    }


def for_nested(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'children': generate(value1, value2)
    }


def generate(data1, data2):
    keys = data1.keys() | data2.keys()
    added = data2.keys() - data1.keys()
    deleted = data1.keys() - data2.keys()

    diff = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in added:
            diff.append(for_add(key, value2))
        elif key in deleted:
            diff.append(for_delete(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(for_nested(key, value1, value2))
        elif value1 != value2:
            diff.append(for_modified(key, value1, value2))
        else:
            diff.append(for_unchanged(key, value1))

    sorted_diff = sorted(diff, key=lambda x: x['name'])

    return sorted_diff
