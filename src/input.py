from extract import get_input, remove_duplicates

def main():
    filename = 'results.csv'
    input = get_input(filename)
    input_deduped = remove_duplicates(input) 
    print(input_deduped)

if  __name__ == '__main__':
    main()