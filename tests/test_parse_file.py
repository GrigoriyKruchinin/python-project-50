import pytest
from gendiff.parse import parse_data


FILE1_PATH_JSON = "tests/fixtures/file1.json"
FILE1_PATH_YML = "tests/fixtures/file1.yml"
FILE2_PATH_JSON = "tests/fixtures/file2.json"
FILE2_PATH_YML = "tests/fixtures/file2.yml"


def test_parse():
    expected_data_1 = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }

    actual_data_json_1 = parse_data(FILE1_PATH_JSON)
    actual_data_yml_1 = parse_data(FILE1_PATH_YML)

    expected_data_2 = {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }

    actual_data_json_2 = parse_data(FILE2_PATH_JSON)
    actual_data_yml_2 = parse_data(FILE2_PATH_YML)

    assert actual_data_json_1 == expected_data_1
    assert actual_data_yml_1 == expected_data_1
    assert actual_data_json_2 == expected_data_2
    assert actual_data_yml_2 == expected_data_2


def test_unsupported_format():
    with pytest.raises(ValueError):
        parse_data("tests/fixtures/file3.txt")
