import os
import json
from constants import *    
import ccl_bplist
from datetime import datetime
from date_time_encoder import DateTimeEncoder

class FileUtils:
    TEAM_NAMES_FILE='/UserTeamNames.json'
    TEAM_FILE='/Team_{team_id}.json'
    REGULAR_SEASON_DATA_FILE='/RegularSeasonData.json'
    POST_SEASON_DATA_FILE='/PostSeasonData.json'
    CY_YOUNG_STATS='./current_mlb_stats/cy_young_winner_stats.csv'
    MVP_STATS='./current_mlb_stats/mvp_stats.csv'
    BATTING_HOF_STATS='./current_mlb_stats/hof_batting.json'
    PITCHING_HOF_STATS='./current_mlb_stats/hof_pitching.json'
    PYMONGO_CONFIG='./config/password.json'
    PYMONGO_PASS='mongodb_password'
    LEAGUE_JSON_PATH="./seasons/league.json"
    DIVISIONS_DATA_FILE='/AllLeaguesData.json'
    PERIOD='.'
    PLIST_FILE_EXT='.plist'
    JSON_FILE_EXT='.json'
    READ_FILE_BYTES='rb'
    READ_FILE='r'
    WRITE_FILE='w'
    PLAIN_TXT_FILES_PATH='./app_data'

    @DeprecationWarning
    def get_mongo_password() -> str:
        mongo_config = FileUtils.read_json_file(FileUtils.PYMONGO_CONFIG)
        return mongo_config.get(FileUtils.PYMONGO_PASS)

    def read_json_file(file_path: str) -> dict:
        json_obj = {}
        with open(file_path, FileUtils.READ_FILE) as file:
            file_str = file.read()
            json_obj = json.loads(file_str)
        return json_obj
        
    @staticmethod
    def change_file_type(file_path: str, new_file_type: str) -> None:
        file_name, file_type = os.path.splitext(file_path)
        os.rename(file_path, f'{file_name}{new_file_type}')
    
    @staticmethod
    def change_file_ext(file_path: str, file_type: str) -> str:
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
        files = [os.path.join(FileUtils.PLAIN_TXT_FILES_PATH, file) for file in  os.listdir(FileUtils.PLAIN_TXT_FILES_PATH) if os.path.isfile(os.path.join(FileUtils.PLAIN_TXT_FILES_PATH, file))]
        for file in files:
            if 'DS_STORE' not in file:
                FileUtils.change_file_type(file, FileUtils.PLIST_FILE_EXT)
            
    
    @staticmethod
    def convert_files_to_json():
        files = [os.path.join(FileUtils.PLAIN_TXT_FILES_PATH, file) for file in  os.listdir(FileUtils.PLAIN_TXT_FILES_PATH) if os.path.isfile(os.path.join(FileUtils.PLAIN_TXT_FILES_PATH, file))]
        for file in files:
            if 'DS_Store' not in file:
                file_obj = open(file, FileUtils.READ_FILE_BYTES)
                json_path = FileUtils.change_file_ext(file, FileUtils.JSON_FILE_EXT)
                json_file = json.dumps(FileUtils.bplist_dict(file_obj), cls=DateTimeEncoder, indent=4)
                os.remove(file)
                with open(json_path, FileUtils.WRITE_FILE) as f:
                    f.write(json_file)
  #  //json_file = json.dumps(bplist_dict(open('../../UserTeamNames.plist', 'rb')), cls=DateTimeEncoder, indent=4)

#with open('../../UserTeamNames.json', 'w') as file:
 #       file.write(json_file)