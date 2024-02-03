import os
import json
from constants import *    
import ccl_bplist
from datetime import datetime
from date_time_encoder import DateTimeEncoder

class FileUtils:

    @staticmethod
    def change_file_type(file_path, new_file_type):
        file_name, file_type = os.path.splitext(file_path)
        os.rename(file_path, f'{file_name}{new_file_type}')
    
    def change_file_ext(file_path, file_type):
        print(file_path, file_path.split(PERIOD), os.path.splitext(file_path))
        file_name = file_path.split(PERIOD)[0]
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

  #  //json_file = json.dumps(bplist_dict(open('../../UserTeamNames.plist', 'rb')), cls=DateTimeEncoder, indent=4)

#with open('../../UserTeamNames.json', 'w') as file:
 #       file.write(json_file)