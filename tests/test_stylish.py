from gendiff.formatters.stylish import format_value, make_stylish_result


def test_format_value():
    assert 'null' == format_value(None, 0)
    assert 'true' == format_value(True, 0)
    assert 'string' == format_value('string', 0)
    assert '10' == format_value(10, 0)
    assert '10.0' == format_value(10.0, 0)
    assert {'a': 'b'} == format_value({'a': 'b'}, 0)


def test_make_stylish_result():
    input_diff = [
        {'action': 'unchanged', 'name_key': 'common', 'value': [
            {'action': 'unchanged', 'name_key': 'setting1', 'value': 'Value 1'},
            {'action': 'deleted', 'name_key': 'setting2', 'old_value': 200},
            {'action': 'added', 'name_key': 'setting3', 'new_value': None}
        ]}
    ]
    expected_result = (
        "{\n"
        "    common: {\n"
        "        setting1: Value 1\n"
        "      - setting2: 200\n"
        "      + setting3: null\n"
        "    }\n"
        "}"
    )

    assert make_stylish_result(input_diff) == expected_result
