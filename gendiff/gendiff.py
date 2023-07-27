from gendiff.parse import parse_data
from gendiff.generate_diff import generate_diff
from gendiff.formatters.choice_formatter import format_diff


def generate_and_format_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)
    diff = generate_diff(data1, data2)
    return format_diff(diff, formatter)
