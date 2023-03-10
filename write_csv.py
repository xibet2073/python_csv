import csv

with open('csv/employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    employee_writer.writerow(['Mila Brown', 'IT', 'October'])
    employee_writer.writerow(['Nataly Portman', 'IT', 'July'])
