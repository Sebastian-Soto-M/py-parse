from datetime import datetime


def parse_date(date):
    # Original date example = "D:20230116165046+01'00'"
    # Format the date string by removing 'D:' and replacing "'" with ""
    formatted_date = date[2:][:8]
    # Parse and convert to ISO 8601 format
    return datetime.strptime(formatted_date, '%Y%m%d').isoformat()


def build_csv_string(table: list[list[str]]) -> str:
    csv = ""
    for row in table:
        items = ", ".join([i for i in row if i is not None])
        csv += items+'\n'
    return csv
