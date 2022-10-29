from datetime import datetime

EXPECTED_DATE_FORMAT = "%d/%m/%Y"
CUSTOM_DATE_FORMAT = "%d %m %Y"
SPACE_CHAR = " "


def parseData(month_value: str):
    month = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return month.get(month_value)


def generate_expected_str_format(day: str, month: str, year: str):
    return datetime.strptime(day + SPACE_CHAR + str(parseData(month)) + SPACE_CHAR + year, CUSTOM_DATE_FORMAT).strftime(
        EXPECTED_DATE_FORMAT)


def authors(file):
    target_list = []
    f = open(file, "r")
    for i in f:
        if len(i) > 10:
            curItem = i.split("-")[0].rstrip()

            date_part = curItem.split(SPACE_CHAR)
            day = date_part[0][0:len(curItem.split(" ")[0]) - 2]
            month = date_part[1]
            year = date_part[2].lstrip()

            new_data = generate_expected_str_format(day, month, year)

            dictionary = {'original_date': curItem, 'date_modified': new_data}
            target_list.append(dictionary)
    return target_list


print(authors("authors.txt"))
