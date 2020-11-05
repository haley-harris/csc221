#! python3
# removes header from all CSV files in the current working dir

import csv, os

os.makedirs('header-removed', exist_ok=True)

for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue

    print('Removing header from ' + csv_filename + ' ...')

    csv_rows = []
    csv_file_obj = open(csv_filename)
    reader_obj = csv.reader(csv_file_obj)

    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue
        csv_rows.append(row)
    
    csv_file_obj.close()

    # write out csv file
    csv_file_obj = open(os.path.join('header-removed', csv_filename), 'w',
                        newline='')

    csv_writer = csv.writer(csv_file_obj)

    for row in csv_rows:
        csv_writer.writerow(row)
    
    csv_file_obj.close()