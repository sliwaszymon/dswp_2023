import csv
import datetime

def date_swap(file_name, date_idx, input_format, output_format, new_file):
    with open(new_file, 'w', newline='') as writef:
        with open(file_name, newline='', encoding="utf8",errors="ignore") as readf:
            writer = csv.writer(writef, delimiter=";")
            reader = csv.reader(readf, delimiter=';', quoting=csv.QUOTE_NONE)
            writer.writerow(next(reader, None))
            for line in reader:
                line[date_idx] = datetime.datetime.strptime(line[date_idx], input_format).strftime(output_format)
                writer.writerow(line)

date_swap('zad2.csv', 2, "%Y%m%d", "%Y-%m-%d", 'zad5.csv')