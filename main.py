'''    
       CS 6065, Spring 2020
       Docker Project Assignment
       Cloud Computing
       -- Sparsh Priyadarshi
       -- priyadsh@mail.uc.edu
'''
# DEPENDENCIES
from pathlib import Path
import re
import socket

# UTILITY CLASSES
class Outter:
    """ Convenience Class -- Output to console and file both """
    
    out_file_path = None
    fout = None
    
    def __init__(self, out_file_path):
        self.out_file_path = out_file_path
        self.fout = open(self.out_file_path, 'w') 

    def output(self, content):
        print(content)                  # console print
        self.fout.write(content + '\n') # file write 

    # !!!ALWAYS!!! call this to close file handles
    def commit(self):
        try:
            self.fout.close()
        except:
            print("ERROR: could not close file handle for output...")
            raise

# INITIALIZATIONS
pattern = re.compile('\w+', re.IGNORECASE)  # Matches any alphanumeric words  
target_path = Path('/home/data')            # input directory
target_output_path = Path('/home/output')   # output file
output = ''
grandtotal_word_count = 0
max_count = -1
file_max_count = ''

# PATHS SANITY CHECKS
if not target_path.exists() or not target_output_path.exists():
    print("/home/data <AND/OR> /home/output/result.txt Paths NOT FOUND... ")
    print("EXITING PROGRAM")
    exit(1)

# INITIALIZE OUTPUT COMPONENT FOR CONSOLE AND FILE ROUTING
outter = Outter(target_output_path.joinpath(Path('result.txt')))

# INPUT FILES ARE .txt FILES
text_file_paths = sorted(target_path.glob('*.txt'))

# WORDCOUNT CALCULATIONS
outter.output("Files and their Word Counts at Path: /home/data :-")
for text_file_path in text_file_paths:
    this_filename = str(text_file_path).split('/')[-1]

    with open(text_file_path) as f:
        read_data = f.read()
        matches = [ match for match in pattern.finditer(read_data)]
        word_count = len(matches)
        if word_count > max_count:
            max_count = word_count
            file_max_count = this_filename
        outter.output(str(this_filename) + ", WORD COUNT = " + str(word_count))

        grandtotal_word_count += word_count

outter.output("...GRAND TOTAL WORD COUNT = " + str(grandtotal_word_count))
outter.output("...FILE WITH MAX WORD COUNT(" + str(max_count) +") = " + str(file_max_count))

# IP CALCULATIONS
host_ip = socket.gethostbyname(socket.gethostname())
outter.output("THIS MACHINE'S IP ADDRESS: " + str(host_ip))

outter.output("DONE, check " + str(target_output_path.joinpath(Path('result.txt')).absolute())  + " for output")

# ENSURE FILE IS WRITTEN AND CLOSED
outter.commit() 

# ...BYE WORLD

