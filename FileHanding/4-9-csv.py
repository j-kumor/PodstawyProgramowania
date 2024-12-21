import csv

FILENAME = 'it_company.csv'


def read_designers(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Job Title'] == 'Graphic Designer':
                print(f"{row['First Name']} {row['Last Name']}, {row['Email']}")


def main():
    read_designers(FILENAME)


if __name__ == '__main__':
    main()
