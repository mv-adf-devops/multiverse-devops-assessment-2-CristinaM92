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

def remove_empty_lines(array_input2):
    clean_list = []

    for sublist in array_input2:
        for element in sublist:
            if element != "":
                clean_list.append(sublist)
                break
    return clean_list

def capitalize_names(headers, data):
    first_name_index = headers.index('first_name')
    last_name_index = headers.index('last_name')

    for entry in data:
        entry[first_name_index] = entry[first_name_index].capitalize()
        entry[last_name_index] = entry[last_name_index].capitalize()

    return data

def validate_answer_3(data):
    valid_data = []

    for entry in data:
        answer_3 = entry[5]  # Assuming 'answer_3' is always at index 5

        # Check if answer_3 is a valid numeric value between 1 and 10
        if isinstance(answer_3, int) and 1 <= answer_3 <= 10:
            valid_data.append(entry)

    return valid_data

def output_to_file(output_filename,data):
    with open(output_filename,"w",encoding = "UTF8",newline = "\n") as f:
        writer = csv.writer(f)
        writer.writerows(data)