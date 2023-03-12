#!/usr/bin/env python3
# Quick Fix File Name Replacement, replaces the first certain text section in all input files in a directory
# written by Jonáš Schröder in 2023.

import logging
import os


logging.basicConfig(level=logging.INFO)

__version__ = 0.2
verstr = "QFFNR ver. {}, by Jonáš Schröder".format(__version__)
print(verstr+"\n"+"-"*len(verstr)+"\n")

file_ending = ".txt" #this is the extension of all files that this will process
to_be_replaced = "2-0"
replaced_with = "1-1"

if __name__ == "__main__":
    selected_files = [f for f in os.listdir() if f.endswith(file_ending)]
    if not selected_files:
        logging.error(f"{os.getcwd()} does not contain any {file_ending} files")
        quit()
    print(selected_files)

    for log_file in selected_files:
        with open(log_file, 'r+') as file:
            logging.info("Processing file {}".format(log_file))
            contents = file.read()
            file.seek(0)
            new_contents = contents.replace(to_be_replaced, replaced_with, 1)
            file.write(new_contents)
            file.truncate()
    logging.info("Export finished. Normal termination")
    quit()
