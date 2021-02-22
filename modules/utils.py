import os

def get_file_names(folderpath,out="output.txt"):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""

    with open(out, "w") as outp:
        dirs = os.listdir(folderpath)
        for filename in dirs:
            path_name = os.path.join( filename)
            outp.write(str(path_name) + "\n")

def get_all_file_names(folderpath,out="output.txt"):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    for root, subdirs, files in os.walk(folderpath):
        with open(folderpath+out, 'a') as file_obj:
            for file in files:
                file_obj.write(file + "\n")

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for files in file_names:
        with open(files):
            print(files.readline().rstrip("\n"))

def print_emails(file_names_2):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for files in file_names_2:
        with open(files) as f:
            find_line = f.readlines()
            for line in find_line:
                if "@"  in line:
                    print(line)

def write_headlines(md_files, out="output.txt"):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    for file in md_files:
        with open(file) as f:
            lines=f.readlines()
            for line in lines:
                if '#' in line :
                    with open  (out, 'a') as o:
                        o.write(line)