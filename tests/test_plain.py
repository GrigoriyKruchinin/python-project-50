from gendiff.formatters.plain import format_diff_plain, format_value


def test_format_value():
    assert format_value("hello") == "'hello'"
    assert format_value(42) == "42"
    assert format_value(3.14) == "3.14"
    assert format_value(True) == "true"
    assert format_value(False) == "false"
    assert format_value(None) == "null"
    assert format_value({"key": "value"}) == "[complex value]"
    assert format_value([1, 2, 3]) == "[complex value]"
    assert format_value([1, [2, 3], 4]) == "[complex value]"
    assert format_value({"key": {"nested_key": "value"}}) == "[complex value]"
    assert format_value([]) == "[complex value]"
    assert format_value({}) == "[complex value]"


def test_format_diff_plain():
    input_diff = [
        {
            'action': 'unchanged',
            'name_key': 'common',
            'value': [
                {'action': 'unchanged',
                 'name_key': 'setting1',
                 'value': 'Value 1'},
                {'action': 'deleted',
                 'name_key': 'setting2',
                 'old_value': 200},
                {'action': 'added',
                 'name_key': 'setting3',
                 'new_value': None},
                {'action': 'modified',
                 'name_key': 'setting4',
                 'old_value': False,
                 'new_value': [{'action': 'added', 'name_key': 'setting5', 'new_value': 'boo'}]}  # noqa: E501
            ]
        }
    ]

    expected_result = (
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was added with value: null\n"
        "Property 'common.setting4' was updated. From false to [complex value]"
    )

    assert format_diff_plain(input_diff) == expected_result
