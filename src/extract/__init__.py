import csv


def get_input(filename):
   rows = []
   try:

        with open(filename, 'r') as f:
            csvreader = csv.reader(f)
            for line in csvreader:
                rows.append(line)
                
   except OSError as e:

        print(f"Unable to open {filename}: {e}")

        raise 
    
   return rows

def remove_duplicates(array_input):
    unique_rows = []
    user_ids = []

    for row in array_input:
        user_id = row[0]
        if user_id not in user_ids:
            user_ids.append(user_id)
            unique_rows.append(row)
    return unique_rows