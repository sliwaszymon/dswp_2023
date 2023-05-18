import os
import csv

def process_txt_files(directory, output_csv):
    with open(output_csv, 'w', newline='') as csvf:
        writer = csv.writer(csvf, delimiter=';')
        cols = False
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.txt'):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r') as txtf:
                        if not cols:
                            cols = txtf.readline()
                            writer.writerow(cols.removesuffix('\n').split(','))
                        else:
                            txtf.readline()
                        for line in txtf:
                            writer.writerow(line.removesuffix('\n').split(','))
                        
process_txt_files('data_for_lab_10', 'zad2.csv')