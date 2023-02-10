import csv
def read_file_to_list(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines

def read_csv_to_map(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = row[1]
    return data
