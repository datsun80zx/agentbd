import os
from config import MAX_CHARS, validate, Path_type

def get_file_content(working_directory, file_path): 
    working_abs_path = os.path.abspath(working_directory)
    try: 
        """
        target_file = os.path.normpath(os.path.join(working_abs_path, file_path))
        if not os.path.isfile(target_file): 
            return f'Error: File not found or is not a regular file: "{file_path}"'

        valid_target_file = os.path.commonpath([working_abs_path, target_file]) == working_abs_path
        if not valid_target_file: 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 
        """
        target_file = validate(working_abs_path, file_path, Path_type.FILE)
        with open(target_file, "r") as f: 
            file_content_string = f.read(MAX_CHARS)
            if f.read(1): 
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e: 
        return f'Error: {e}'
   