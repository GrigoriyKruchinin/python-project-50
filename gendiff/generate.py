def for_add(key, value):
    return {
        'action': 'added',
        'name_key': key,
        'new_value': value
    }


def for_delete(key, value):
    return {
        'action': 'deleted',
        'name_key': key,
        'old_value': value
    }


def for_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name_key': key,
        'value': value
    }


def for_modified(key, value1, value2):
    return {
        'action': 'modified',
        'name_key': key,
        'new_value': value2,
        'old_value': value1
    }


def for_nested(key, value1, value2):
    if isinstance(value1, dict) and isinstance(value2, dict):
        return for_unchanged(key, generate(value1, value2))

    if value1 != value2:
        return for_modified(key, value1, value2)

    return for_unchanged(key, value1)


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
        else:
            diff.append(for_nested(key, value1, value2))

    sorted_diff = sorted(diff, key=lambda x: x['name_key'])

    return sorted_diff
