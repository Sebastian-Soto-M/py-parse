from tika import parser


def main():
    parsed = parser.from_file('assets/index.html')
    print(parsed['content'])


if __name__ == "__main__":
    main()
