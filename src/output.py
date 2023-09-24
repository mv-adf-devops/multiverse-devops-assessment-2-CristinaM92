from extract import *

def main():
    out_file = "clean_results.csv"
    out_data = get_input(out_file)
    # iterate over the data, from existing sub-module which is used to read the clean_results.csv file
    # for each line print this to the terminal
    for line in out_data:
        print(line)
    # below is what could be used to print the clean results in a fixed width format
    # please refer to functions in src/extract/__init__.py
    #fixed_width(out_file)

if __name__ == "__main__":
    main()