import os
from enum import Enum

MAX_CHARS = 10000

Path_type = Enum("Path_type", ["FILE", "DIR"])

def validate(working_directory, path_or_file, path_type): 
    target = os.path.normpath(os.path.join(working_directory, path_or_file))
    match path_type:
        case Path_type.FILE: 
            valid_target_file = os.path.commonpath([working_directory, target]) == working_directory
            if not valid_target_file: 
                raise RuntimeError(f'Error: Cannot execute "{path_or_file}" as it is outside the permitted working directory')
            
            if not os.path.isfile(target): 
                raise RuntimeError(f'Error: File not found or is not a regular file: "{path_or_file}"')
            
            return target

        case Path_type.DIR: 
            valid_target_dir = os.path.commonpath([working_directory, target]) == working_directory
            if not valid_target_dir: 
                raise RuntimeError(f'Error: Cannot list "{path_or_file}" as it is outside the permitted working directory')
            
            if not os.path.isdir(target): 
                raise RuntimeError(f'Error: "{path_or_file}" is not a directory')

            return target