#!/usr/bin/env python3
# Quick Fix File Name Replacement, replaces the first certain text section in all input files in a directory

import logging
import os


# Settings
file_ending = ".txt" #this is the extension of all files that this will process
to_be_replaced = "2-0"
replaced_with = "1-1"


#  Configure logging
logging.basicConfig(level=logging.INFO)

__version__ = "0.3 / 25.08.2023"
print(f"\n  -- QFFNR {__version__} by Jonáš Schröder --\n")

if __name__ == "__main__":
    selected_files = [f for f in os.listdir() if f.endswith(file_ending)]
    if not selected_files:
        logging.error(f"  {os.getcwd()} -- There are no {file_ending} files\n")
        quit()
    print(f"\n{os.getcwd()}\n{selected_files}\n")

    for log_file in selected_files:
        with open(log_file, 'r+') as file:
            logging.info(f"  Processing file  :  {log_file}")
            contents = file.read()
            file.seek(0)
            new_contents = contents.replace(to_be_replaced, replaced_with, 1)
            file.write(new_contents)
            file.truncate()
    logging.info("\n  -- finished --\n")
    quit()
