from format_data import format_data_for_display, format_data_for_excel

people = [
    {
        'given_name': 'Alfonsa',
        'family_name': 'Ruiz',
        'title': 'Senior Software Engineer',
    },
    {
        'given_name': 'Sayid',
        'family_name': 'Khan',
        'title': 'Project Manager',
    },
]

def main():
    print(format_data_for_display(people))
    print(format_data_for_excel(people))


if __name__ == '__main__':
    main()
