import pytest
from gendiff.generator import (
    generate, for_add, for_delete, for_unchanged, for_modified, for_nested
)


def test_for_add():
    result = for_add('key1', 123)
    assert result == {'action': 'added',
                      'name': 'key1',
                      'new_value': 123}


def test_for_delete():
    result = for_delete('key2', 'old')
    assert result == {'action': 'deleted',
                      'name': 'key2',
                      'old_value': 'old'}


def test_for_unchanged():
    result = for_unchanged('key3', 'value3')
    assert result == {'action': 'unchanged',
                      'name': 'key3',
                      'value': 'value3'}


def test_for_modified():
    result = for_modified('key4', 'old', 123)
    assert result == {'action': 'modified',
                      'name': 'key4',
                      'new_value': 123,
                      'old_value': 'old'}


def test_for_nested_dict():
    old_dict = {'a': 1, 'b': 2}
    new_dict = {'a': 1, 'b': 3, 'c': 4}
    result = for_nested('key5', old_dict, new_dict)
    assert result == {
        'action': 'nested',
        'name': 'key5',
        'children': [
            {'action': 'unchanged', 'name': 'a', 'value': 1},
            {'action': 'modified', 'name': 'b', 'new_value': 3, 'old_value': 2},
            {'action': 'added', 'name': 'c', 'new_value': 4}
        ]
    }


@pytest.fixture
def file1():
    return {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
        }
    }


@pytest.fixture
def file2():
    return {
        'common': {
            'setting1': 'Value 1',
            'setting3': None,
        }
    }


@pytest.fixture
def expected_result():
    return [
        {
            'action': 'nested',
            'name': 'common',
            'children': [
                {'action': 'unchanged', 'name': 'setting1', 'value': 'Value 1'},
                {'action': 'deleted', 'name': 'setting2', 'old_value': 200},
                {'action': 'added', 'name': 'setting3', 'new_value': None},
            ],
        },
    ]


def test_generate(file1, file2, expected_result):
    result = generate(file1, file2)
    assert result == expected_result
