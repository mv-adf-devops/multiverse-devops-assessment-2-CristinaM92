from extract import *

def main():
    filename = 'results.csv'
    input = get_input(filename)
    input_deduped = remove_duplicates(input) 
    removed_blanks = remove_empty_lines(input_deduped)
    capitalised_names = capitalize_names(removed_blanks)
    valid_ans_3 = validate_answer_3(capitalised_names)
    output_to_file("clean_results.csv",valid_ans_3)

    

if  __name__ == '__main__':
    main()