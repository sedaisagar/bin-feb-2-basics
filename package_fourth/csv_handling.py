# Comma Separated Values

# Reading & writing CSV files with csv.reader & csv.writer

import csv

# data_to_write = [
#     ['Name', 'Department', 'Birthday Month'],
#     ['John Smith', 'Accounting', 'November'],
#     ['Erica Meyers', 'IT', 'March']
# ]

# with open('employee_birthdays.csv', mode='w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
    
#     # Writing a single row (e.g., the header)
#     # csv_writer.writerow(data_to_write[0]) 

#     # Writing multiple rows at once
#     csv_writer.writerows(data_to_write)



# with open('employee_birthdays.csv', mode='r', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             # Each row is a list of strings
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')


# with open('employee_birthdays.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)


import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

