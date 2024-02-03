from os import listdir, remove
from os.path import isfile, join
from pathlib import Path
from constants import *    
from file_utils import FileUtils

import json
from date_time_encoder import DateTimeEncoder

def convert_files_to_plist():
    files = [join(PLAIN_TXT_FILES_PATH, file) for file in  listdir(PLAIN_TXT_FILES_PATH) if isfile(join(PLAIN_TXT_FILES_PATH, file))]
    for file in files:
        FileUtils.change_file_type(file, PLIST_FILE_EXT)

def convert_files_to_json():
    files = [join(PLAIN_TXT_FILES_PATH, file) for file in  listdir(PLAIN_TXT_FILES_PATH) if isfile(join(PLAIN_TXT_FILES_PATH, file))]
    for file in files:
        print(file)
        file_obj = open(file, READ_FILE_BYTES)
        json_path = FileUtils.change_file_ext(file, JSON_FILE_EXT)
        json_file = json.dumps(FileUtils.bplist_dict(file_obj), cls=DateTimeEncoder, indent=4)
        remove(file)
        with open(json_path, WRITE_FILE) as f:
            f.write(json_file)

def convert_files():
    convert_files_to_plist()
    convert_files_to_json()

if __name__ == '__main__':
    convert_files()
    
