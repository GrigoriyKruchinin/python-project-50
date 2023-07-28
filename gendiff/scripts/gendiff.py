from gendiff import cli
from gendiff.result_diff import generate_and_format_diff


def main():
    args = cli.parse_args()
    diff = generate_and_format_diff(
        args.first_file, args.second_file, args.format
    )
    print(diff)


if __name__ == "__main__":
    main()
