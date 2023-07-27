from gendiff.formatters.json import format_diff_json


def test_format_diff_json():
    input_diff = [
        {
            'action': 'unchanged',
            'name_key': 'common',
            'value': [
                {'action': 'unchanged', 'name_key': 'setting1',
                 'value': 'Value 1'},
                {'action': 'deleted', 'name_key': 'setting2', 'old_value': 200},
                {'action': 'added', 'name_key': 'setting3', 'new_value': None},
                {
                    'action': 'modified',
                    'name_key': 'setting4',
                    'old_value': False,
                    'new_value': [
                        {'action': 'added', 'name_key': 'setting5',
                         'new_value': 'boo'}
                    ],
                },
            ],
        }
    ]

    expected_result = (
        '[\n'
        '    {\n'
        '        "action": "unchanged",\n'
        '        "name_key": "common",\n'
        '        "value": [\n'
        '            {\n'
        '                "action": "unchanged",\n'
        '                "name_key": "setting1",\n'
        '                "value": "Value 1"\n'
        '            },\n'
        '            {\n'
        '                "action": "deleted",\n'
        '                "name_key": "setting2",\n'
        '                "old_value": 200\n'
        '            },\n'
        '            {\n'
        '                "action": "added",\n'
        '                "name_key": "setting3",\n'
        '                "new_value": null\n'
        '            },\n'
        '            {\n'
        '                "action": "modified",\n'
        '                "name_key": "setting4",\n'
        '                "old_value": false,\n'
        '                "new_value": [\n'
        '                    {\n'
        '                        "action": "added",\n'
        '                        "name_key": "setting5",\n'
        '                        "new_value": "boo"\n'
        '                    }\n'
        '                ]\n'
        '            }\n'
        '        ]\n'
        '    }\n'
        ']'
    )

    assert format_diff_json(input_diff) == expected_result
