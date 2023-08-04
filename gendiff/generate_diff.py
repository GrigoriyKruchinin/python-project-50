from gendiff.parser import parse_data_from_file
from gendiff.generator import generate
from gendiff.formatters.choice_formatter import format_diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parse_data_from_file(file_path1)
    data2 = parse_data_from_file(file_path2)
    diff = generate(data1, data2)
    return format_diff(diff, formatter)
