import os
import json
from constants import *    
import ccl_bplist
from datetime import datetime
from date_time_encoder import DateTimeEncoder

class FileUtils:

    def read_json_file(file_path):
        json_obj = {}
        with open(file_path, READ_FILE) as file:
            file_str = file.read()
            json_obj = json.loads(file_str)
        return json_obj
        
    @staticmethod
    def change_file_type(file_path, new_file_type):
        file_name, file_type = os.path.splitext(file_path)
        os.rename(file_path, f'{file_name}{new_file_type}')
    
    @staticmethod
    def change_file_ext(file_path, file_type):
        print(file_path, file_path.split(PERIOD), os.path.splitext(file_path))
        file_name = os.path.splitext(file_path)[0]
        return f'{file_name}{file_type}'

    @staticmethod
    def clean_archive(d):
        if type(d) in [dict, ccl_bplist.NsKeyedArchiverDictionary]:
            return {k:FileUtils.clean_archive(v) for k,v in d.items() if not str(k).startswith('$')}
        elif type(d) == ccl_bplist.NsKeyedArchiverList:
            return [FileUtils.clean_archive(i) for i in d]
        else:
            return d

    @staticmethod
    def bplist_dict(fobj):
        """Convert a bplist file object to python dict"""
        plist = ccl_bplist.load(fobj)
        ccl_bplist.set_object_converter(ccl_bplist.NSKeyedArchiver_common_objects_convertor)
        archive = ccl_bplist.deserialise_NsKeyedArchiver(plist)
        return FileUtils.clean_archive(archive)

    @staticmethod
    def convert_files_to_plist():
        files = [os.path.join(PLAIN_TXT_FILES_PATH, file) for file in  os.listdir(PLAIN_TXT_FILES_PATH) if os.path.isfile(os.path.join(PLAIN_TXT_FILES_PATH, file))]
        for file in files:
            FileUtils.change_file_type(file, PLIST_FILE_EXT)
    
    @staticmethod
    def convert_files_to_json():
        files = [os.path.join(PLAIN_TXT_FILES_PATH, file) for file in  os.listdir(PLAIN_TXT_FILES_PATH) if os.path.isfile(os.path.join(PLAIN_TXT_FILES_PATH, file))]
        for file in files:
            print(file)
            if 'DS_Store' not in file:
                file_obj = open(file, READ_FILE_BYTES)
                json_path = FileUtils.change_file_ext(file, JSON_FILE_EXT)
                json_file = json.dumps(FileUtils.bplist_dict(file_obj), cls=DateTimeEncoder, indent=4)
                print(json_path, file)
                os.remove(file)
                with open(json_path, WRITE_FILE) as f:
                    f.write(json_file)
  #  //json_file = json.dumps(bplist_dict(open('../../UserTeamNames.plist', 'rb')), cls=DateTimeEncoder, indent=4)

#with open('../../UserTeamNames.json', 'w') as file:
 #       file.write(json_file)