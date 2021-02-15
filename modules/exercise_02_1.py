import csv
import argparse

def print_file_content(file):
    """Print content from a file
    
    Keyword arguments:
    :param file:
        path to a file
    """

    with open(file) as f:
        reader = csv.reader(f)

        for row in reader:
            print('Row #' + str(reader.line_num) + " " + str(row))

            if reader.line_num > 5000:
                break

def write_list_to_file(output_file, lst):
    """Write a list to a file.
    
    Keyword arguments:
    :param output_file: 
        path to the new .txt file
    :param lst:
        the list of content that the file will contain
    """
    with open(output_file, 'w') as fo:
        for l in lst:
            for element in l:
                fo.write(str(element) + "\n")

def read_csv(input_file):
    """Read a file put content in a list.

    Keyword arguments:
    :param input_file:
        path to csv-file to read from
    """
    data = []
    with open(input_file) as fo:
        content = fo.readlines()
    for line in content:
        data.append(line.replace("\n", ""))

    print(data)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program prints file content, writes from a list to a file or reads and prints content of a csv file')
    parser.add_argument('file', help='The path to a file you want printed')
    parser.add_argument('outputfile', help='The path to a new txt file with "custom" name')
    parser.add_argument('lst', help='A list of content you want int the "output_file"')
    parser.add_argument('inputfile', help='Reads a file and puts the content in a list and prints the list')
    parser.add_argument('--h', help='This is help')

    args = parser.parse_args()

    print('file:', args.file)
    print('output_file:', args.outputfile)
    print('lst:', args.lst)
    print('inputfile:', args.inputfile)